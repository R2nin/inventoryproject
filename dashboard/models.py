from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Papelaria', 'Papelaria'),
    ('Eletronico', 'Eletronico'),
    ('Alimento', 'Alimento'),
)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, default='Papelaria', null=True)
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.name}-{self.quantity}-{self.category}'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'