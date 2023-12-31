from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300)
    logo = models.CharField(max_length=300)
    slug = models.CharField(max_length=300,unique=True)
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=300)
    logo = models.CharField(max_length=300)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.CharField(max_length=300,unique=True)

    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    url = models.URLField(max_length=1000)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    url = models.URLField(max_length=1000)
    rank = models.IntegerField()
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    rank = models.IntegerField()
    slug = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    post = models.CharField(max_length=300)
    star = models.IntegerField(default=5)
    comment = models.TextField()
    def __str__(self):
        return self.name

LABELS = (('new','new'),('hot','hot'),('sale','sale'),('','default'))
STOCK = (('In stock','In stock'),('Out of stock','Out of stock'))
class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    discounted_price = models.IntegerField(default = 0)
    image = models.ImageField(upload_to='media')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    slug = models.TextField(unique = True)
    description = models.TextField(blank = True)
    specification = models.TextField(blank=True)
    labels = models.CharField(choices=LABELS,max_length=50)
    stock = models.CharField(choices=STOCK,max_length=50)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name

class ProductReview(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    review = models.TextField(blank = True)
    star = models.IntegerField(default=5)
    slug = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Cart(models.Model):
    username = models.CharField(max_length=300)
    slug = models.TextField()
    quantity = models.IntegerField(default=1)
    items = models.ForeignKey(Product, on_delete=models.CASCADE)
    total = models.IntegerField()
    checkout = models.BooleanField(default=False)


    def __str__(self):
        return self.username


class Information(models.Model):
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=300)
    phone = models.CharField(max_length=20)


    def __str__(self):
        return self.address


# class Checkout(models.Model):
#     firstname = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     mobile_no = models.IntegerField()
#     address = models.TextField()
#     country = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zip_code = models.IntegerField()
#     amount = models.IntegerField()


