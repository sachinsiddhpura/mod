from django.db import models
from django.core.validators import RegexValidator
import os
import random
import string
# Create your models here.
MILK_AVAILABLE = (
    ('L','L'),
    ('ML','ML'),
    ('Bages','Bages')
)

SUBSCRIPTION_TYPE =(
    ('Weekly','Weekly'),
    ('Daily','Daily'),
    ('Weekend','Weekend')
)

MILK_CATEGORY =(
    ('Organic','Organic'),
    ('Routine','Routine')
)

DAILYP_CATEGORY =(
    ('Dairy','Dairy'),
    ('Bakery','Bakery'),
    ('Grocery','Grocery')
)

def upload_profile_photo(instance,filename):
    print(instance)
    new_filename=random.randint(1,40000000000)
    name,ext=get_file_ext(filename)
    final_filename='{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return 'user/{new_filename}/{final_filename}'.format(new_filename=new_filename,final_filename=final_filename)

def get_file_ext(filepath):
    base_name=os.path.basename(filepath)
    name,ext=os.path.splitext(base_name)
    return name,ext
class User(models.Model):
    user_id             =models.IntegerField(unique=True)
    user_first_name     =models.CharField(max_length=120)
    user_last_name      =models.CharField(max_length=120)
    mobile_number       =models.CharField(max_length=10,validators=[
                                         RegexValidator(r'^\d{1,10}$')])
    email               =models.EmailField()
    profile_photo       =models.ImageField(blank=True, null=True,upload_to=upload_profile_photo)
    address =models.TextField(blank=True,null=True)
    address2= models.TextField(blank=True, null=True)
    postal_code=models.IntegerField(blank=True,null=True)
    state=models.CharField(max_length=40,blank=True, null=True)
    city=models.CharField(max_length=40,blank=True, null=True)
    status              =models.BooleanField(default=True)
    class Meta:
        verbose_name = ('Users')

    def __str__(self):
        return  self.user_first_name


class Milk(models.Model):
    milk_name           =models.CharField(max_length=120)
    milk_id             =models.IntegerField()
    milk_company_category_id    =models.CharField(max_length=120,unique=True)
    price               =models.IntegerField()
    image               =models.ImageField(upload_to='prodcuts/%Y/%m/%d',blank=True)
    available           =models.CharField(max_length=120,choices=MILK_AVAILABLE,default='L')
    description         =models.TextField()
    manufacture_date    =models.DateTimeField(auto_now=True)
    expired_date        =models.DateTimeField(auto_now_add=True)
    status              =models.BooleanField()

    class Meta:
        verbose_name = ('Milk_Product')

    def __str__(self):
        return self.milk_name

class Subscription(models.Model):
    user_id         =models.ForeignKey(User,related_name='subscription',on_delete=models.CASCADE)
    payment_id      =models.IntegerField()
    subscription_type   =models.CharField(max_length=120,choices=SUBSCRIPTION_TYPE,default='Daily')
    

    class Meta:
        verbose_name = ('Subsription')

    def __str__(self):
        return self.subscription_type

class MilkCompany(models.Model):
    name            =models.CharField(max_length=120)
    gst_no          =models.CharField(max_length=15, validators=
                            [RegexValidator(r'^\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[Z]{1}[A-Z\d]{1}$')])
    join_date       =models.DateTimeField(auto_now=True)
    leave_date      =models.DateTimeField(auto_now_add=True)
    status          =models.BooleanField()

    class Meta:
        verbose_name = ('Milk_Company')

    def __str__(self):
        return self.name

class MilkCategory(models.Model):
    milk_category       =models.CharField(max_length=120,choices=MILK_CATEGORY,default='Routine')
    c_id                =models.IntegerField()
    status              =models.BooleanField()

    class Meta:
        verbose_name = ('Milk_Category')

    def __str__(self):
        return self.milk_category

class MilkCompanyCategory(models.Model):
    milk_category_id        =models.ForeignKey(MilkCategory,on_delete=models.CASCADE)
    milk_company_id         =models.ForeignKey(MilkCompany,related_name='milk_company',on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Milk_Company_Category')

    def __str__(self):
        return str(self.milk_company_id)

class Order(models.Model):
    user_id             =models.ForeignKey(User,related_name='order',on_delete=models.CASCADE)
    milk_id             =models.ForeignKey(Milk,on_delete=models.CASCADE)
    quantity            =models.IntegerField()
    price               =models.IntegerField()
    status              =models.BooleanField()

    class Meta:
        verbose_name = ('Order')

    def __str__(self):
        return str(self.milk_id)

class Payment(models.Model):
    user_id         =models.ForeignKey(User,related_name='payment',on_delete=models.CASCADE)
    payment_id      =models.CharField(max_length=120)
    order_id        =models.ForeignKey(Order,on_delete=models.CASCADE)
    payment         =models.IntegerField()
    payment_status  =models.BooleanField()
    status          =models.BooleanField()

    class Meta:
        verbose_name = ('Payment')

    def __str__(self):
        return str(self.payment_id)

class Country(models.Model):
    country_name        =models.CharField(max_length=120)
    country_code        =models.IntegerField(unique=True)
    status              =models.BooleanField()

    class Meta:
        verbose_name = ('Country')

    def __str__(self):
        return self.country_name

class State(models.Model):
    state_name          =models.CharField(max_length=120)
    country_id          =models.ForeignKey(Country,on_delete=models.CASCADE)
    status              =models.BooleanField()

    class Meta:
        verbose_name = ('State')

    def __str__(self):
        return self.state_name

class City(models.Model):
    city_name           =models.CharField(max_length=120)
    state_id            =models.ForeignKey(State,on_delete=models.CASCADE)
    status              =models.BooleanField()

    class Meta:
        verbose_name = ('City')

    def __str__(self):
        return self.city_name

class DeliveryTime(models.Model):
    user_id             =models.ForeignKey(User,related_name='delivery',on_delete=models.CASCADE)
    time                =models.DateTimeField(auto_now=True)
    status              =models.BooleanField()

    class Meta:
        verbose_name = ('Delivery_Time')

    def __str__(self):
        return str(self.time)



class FarmerProduct(models.Model):
    name                =models.CharField(max_length=120)
    price               =models.IntegerField()
    quantity            =models.IntegerField()
    image               =models.ImageField(upload_to='prodcuts/fm/%Y/%m/%d',blank=True)
    available           =models.CharField(max_length=120,choices=MILK_AVAILABLE,default='L')
    description         =models.TextField()
    manufacture_date    =models.DateTimeField(auto_now=True)
    expired_date        =models.DateTimeField(auto_now_add=True)
    status              =models.BooleanField()

    class Meta:
        verbose_name = ('Farmer_Products')

    def __str__(self):
        return self.name

class DailyPCategory(models.Model):
    dailyp_category     =models.CharField(max_length=120,choices=DAILYP_CATEGORY,default='Routine')
    d_id                =models.IntegerField()
    status              =models.BooleanField()

    class Meta:
        verbose_name = ('DailyP_Category')

    def __str__(self):
        return self.dailyp_category

class DailyNeedProduct(models.Model):
    name                =models.CharField(max_length=120)
    price               =models.IntegerField()
    quantity            =models.IntegerField()
    image               =models.ImageField(upload_to='prodcuts/fm/%Y/%m/%d',blank=True)
    '''available           =models.CharField(max_length=120,choices=MILK_AVAILABLE,default='L')'''
    p_category          =models.ForeignKey(DailyPCategory,on_delete=models.CASCADE)
    description         =models.TextField()
    manufacture_date    =models.DateTimeField(auto_now=True)
    expired_date        =models.DateTimeField(auto_now_add=True)
    status              =models.BooleanField()

    class Meta:
        verbose_name = ('Daily_Need_Products')

    def __str__(self):
        return self.name


class AddToCart(models.Model):
    user_id=models.ForeignKey(User,related_name='addtocart',on_delete=models.CASCADE)
    qty=models.IntegerField()
    milk_id=models.ForeignKey(Milk,related_name='milk',on_delete=models.CASCADE)
    status=models.BooleanField()
    class Meta:
        verbose_name = ('Add_To_Cart')

    def __str__(self):
        return self.user_id