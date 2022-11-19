from django.db import models


class Item(models.Model):
    CHOICE = (
        ("rub", 'RUB'),
        ("usd", 'USD'),
    )
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    currency = models.CharField(max_length=3, choices=CHOICE, default="rub")

    def __str__(self):
        return f'name: {self.name} price{self.price}'

class Order(models.Model):
    CHOICE = (
        ("rub", 'RUB'),
        ("usd", 'USD'),
    )

    items = models.ManyToManyField(Item)
    date = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(max_length=3, choices=CHOICE, default="rub")
    price = models.IntegerField()

    def __str__(self):
        return f'id: {self.id} price: {self.price} item: {self.items.all}'