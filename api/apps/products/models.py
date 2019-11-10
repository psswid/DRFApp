from django.db import models
from api.apps.core.models import BaseModel


class Product(BaseModel):

    name = models.CharField(db_index=True, max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def _str_(self):
        return self.name