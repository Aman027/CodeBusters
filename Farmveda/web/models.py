from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 50)
    category = models.CharField(max_length = 25)
    price = models.IntegerField(blank=True)
    #seller = models.ForeignKey()
    #flag to differentiate crawled data from signed up data
    crawled = models.BooleanField(default=False)    
    rating = models.FloatField(default=0)
    quantity = models.CharField(max_length = 50)
    #feedback = models.OneToOneField(Feedback)

