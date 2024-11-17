from django.db import models

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