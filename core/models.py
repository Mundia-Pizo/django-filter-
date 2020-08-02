from django.db import models

CHOICES = (
    ('lady', 'LADIES'),
     ('baby', 'BABIES'),
     ('men', 'MEN')
)
class Item(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField()
    discount_price = models.FloatField()
    slug = models.SlugField()
    category = models.CharField(max_length=5, choices=CHOICES)

    def __str__(self):
        return self.title
