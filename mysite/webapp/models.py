from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.db.models import CASCADE


class AccountManager(BaseUserManager):
    def create_user(self, email, password):
        user = self.model(email=email, password=password)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email_):
        print(email_)
        return self.get(email=email_)

class Account(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField('Full name', max_length=100)
    gender = models.CharField('Gender', max_length=10, blank=True)
    phoneNumber = models.CharField('Phone number', max_length=20)
    email = models.EmailField('Email', unique=True)
    #password = models.CharField('Password', max_length=25)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField('Superuser', default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.id) + ' \t' + self.email

    def get_short_name(self):
        return self.email

    def natural_key(self):
        return self.email

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        ordering = ['id']

# class Order(models.Model):
#     customerID = models.ForeignKey('Account', on_delete=models.CASCADE)
#     order_date = models.DateField('Order date')
#     status = models.CharField('Status', max_length=15)
#     comment = models.TextField('Comment')
#
#     def __str__(self):
#         return str(self.id)
#
#     class Meta:
#         verbose_name = 'Order'
#         verbose_name_plural = 'Orders'

class Product(models.Model):
    name = models.CharField('Product name', max_length=30)
    price = models.PositiveIntegerField('Price')
    description = models.TextField('Description', blank=True)
    amount = models.PositiveIntegerField('Amount')
    image = models.ImageField('Image', upload_to='photos/%Y/%m/%d/', blank=True)
    size = models.IntegerField('Size of image', default=100)

    def __str__(self):
        return str(self.id) + " " + self.name

class Order_Product(models.Model):
    productCode = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    customerID = models.ForeignKey('Account', on_delete=models.CASCADE, null=True)
    order_date = models.DateTimeField('Order date', auto_now_add=True)
    status = models.CharField('Status', max_length=15, default='Completed')
    comment = models.TextField('Comment', null=True)
    amount = models.PositiveSmallIntegerField('Amount', default=1)
    sum = models.PositiveIntegerField('Final price')

    def __str__(self):
        return str(self.customerID.id) + " " + str(self.productCode.id)

class ContactUs(models.Model):
    name = models.CharField('Name', max_length=30)
    phoneNumber = models.CharField('Phone number', max_length=20)
    email = models.EmailField('Email')
    message = models.TextField('Message')

    def __str__(self):
        return str(self.id) + " " + self.name

    class Meta:
        verbose_name = 'Contact us'
        verbose_name_plural = 'Contact us'

class Subscriber(models.Model):
    email = models.EmailField('Email')
    def __str__(self):
        return str(self.id) + " " + self.email

class Cart(models.Model):
    product=models.ForeignKey(Product, on_delete=CASCADE)
    owner=models.ForeignKey(Account, on_delete=CASCADE)







