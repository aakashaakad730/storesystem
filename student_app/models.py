from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='profilepic.jpg',upload_to='student_app/images/',blank=True)
    loaction = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.user.username



class CategoryModel(models.Model):
    category_name = models.CharField(max_length=20)
    description = models.CharField(max_length=40)

    def __str__(self):
        return self.category_name
    
class ProductModel(models.Model):
    product_name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    cost_price = models.DecimalField(max_digits=6,decimal_places=2)
    MRP = models.DecimalField(max_digits=6,decimal_places=2)
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class ProductList(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='student_app/images/',blank=True)
    
    def __str__(self):
        return self.title