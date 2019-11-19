from rest_framework import serializers, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.apps.products.models import Product
from api.apps.users.models import User

from .models import Cart, CartItem, Order, OrderItem
from .serializers import (CartItemSerializer, CartSerializer,
                          OrderItemSerializer, OrderSerializer)
from .tasks import send_order_email


class CartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows carts to be viewed or edited.
    """

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    @action(detail=True, methods=["post", "put"])
    def add_to_cart(self, request, pk=None):
        """Add an item to a user's cart.
        Adding to cart is disallowed if there is not enough inventory for the
        product available. If there is, the quantity is increased on an existing
        cart item or a new cart item is created with that quantity and added
        to the cart.
        Parameters
        ----------
        request: request
        Return the updated cart.
        Json
        {
            "product_id": "1",
            "quantity": "2"
        }
        """
        cart = self.get_object()
        try:
            product = Product.objects.get(pk=request.data["product_id"])
            quantity = int(request.data["quantity"])
        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND)

        existing_cart_item = CartItem.objects.filter(cart=cart, product=product).first()
        # before creating a new cart item check if it is in the cart already
        # and if yes increase the quantity of that item
        if existing_cart_item:
            existing_cart_item.quantity += quantity
            existing_cart_item.save()
        else:
            new_cart_item = CartItem(cart=cart, product=product, quantity=quantity)
            new_cart_item.save()

        # return the updated cart to indicate success
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    @action(detail=True, methods=["post", "put"])
    def remove_from_cart(self, request, pk=None):
        """Remove an item from a user's cart.
        Like on the Everlane website, customers can only remove items from the
        cart 1 at a time, so the quantity of the product to remove from the cart
        will always be 1. If the quantity of the product to remove from the cart
        is 1, delete the cart item. If the quantity is more than 1, decrease
        the quantity of the cart item, but leave it in the cart.
        Parameters
        ----------
        request: request
        Return the updated cart.
        """
        cart = self.get_object()
        try:
            product = Product.objects.get(pk=request.data["product_id"])
        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND)

        try:
            cart_item = CartItem.objects.get(cart=cart, product=product)
        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND)

        # if removing an item where the quantity is 1, remove the cart item
        # completely otherwise decrease the quantity of the cart item
        if cart_item.quantity == 1:
            cart_item.delete()
        else:
            cart_item.quantity -= 1
            cart_item.save()

        # return the updated cart to indicate success
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class CartItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cart items to be viewed or edited.
    """

    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or created.
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        """Add info and perform checks before saving an Order.
        Before creating an Order, there is a check on the customer's cart items.
        If the cart item quantity causes the product's available inventory to
        dip below zero, a validation error is raised.If there is enough inventory to support the order, an Order is created
        and cart items are used to make order items. After that the cart is
        cleared.
        NOTE: Cart items are not deleted. When the cart is cleared the cart items
        still exist but are disassociated from the cart. The cart is empty so
        that the user can add new things to it, but cart items are preserved as
        they could be helpful in drawing insights from customer behavior or making
        suggestions. For example, what they have put in their cart previously,
        what other similar products might she/he like, etc.
        Parameters
        ----------
        serializer: OrderSerialiazer
            Serialized representation of Order we are creating.
        """

        try:
            purchaser_id = self.request.data["owner"]
            user = User.objects.get(pk=purchaser_id)
        except:
            raise serializers.ValidationError("User was not found")
        cart = user.cart
        # find the order total using the quantity of each cart item and the product's price
        cart_items = cart.items.all()
        order_total = 0
        for item in cart_items:
            item_quantity = item.quantity
            item_product_price = item.product.price
            item_total = item_quantity * item_product_price
            order_total += item_total

        order = serializer.save(owner=user, total=order_total)
        order_items = []
        for cart_item in cart.items.all():
            order_items.append(
                OrderItem(
                    order=order, product=cart_item.product, quantity=cart_item.quantity
                )
            )
            cart_item.product.save()

        OrderItem.objects.bulk_create(order_items)
        # use clear instead of delete since it removes all objects from the
        # related object set. It doesnot delete the related objects it just
        # disassociates them, which is what we want in order to empty the cart
        # but keep cart items in the db for customer data analysis
        cart.items.clear()

        send_order_email(order, order_items)

    def create(self, request, *args, **kwargs):
        """Override the creation of Order objects.
        Parameters
        ----------
        request: dict
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class OrderItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows order items to be viewed or edited.
    """

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
