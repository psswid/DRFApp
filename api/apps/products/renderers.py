from api.apps.core.renderers import ApiJSONRender


class ProductJSONRenderer(ApiJSONRender):
    object_label = "product"
    pagination_object_label = "products"
    pagination_count_label = "productsCount"
