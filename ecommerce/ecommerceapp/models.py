from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Dress(models.Model):
    GENDER_CHOICES = [
        ('Mens', 'Mens'),
        ('Womens', 'Womens'),
        ('Kids', 'Kids'),
    ]
    CATEGORY_CHOICES = [
        ('BOHEMIAN_OUTFIT', 'Bohemian Outfit'),
        ('BOHO_MEN_STYLE', 'Boho Men Style'),
        ('COACHELLA_OUTFIT', 'Coachella Outfit'),
        ('BOHO_CHIC_MEN', 'Boho Chic Men'),
        ('MENS_RABE_OUTFIT', 'Men\'s Rabe Outfit'),
        ('BOHO_HIPPY', 'Boho Hippie'),
    ]

    SIZE_CHOICES = [
        ('small', 'S'),
        ('medium', 'M'),
        ('large', 'L'),
        ('xlarge', 'XL'),
        ('xxlarge', 'XXL'),
    ]


    name = models.CharField(max_length=255)
    desc=models.TextField(null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) 
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50, choices=SIZE_CHOICES)
    image = models.ImageField(upload_to='dresses/')
    add_img1 = models.ImageField(upload_to='additional_dresses/', null=True)
    add_img2 = models.ImageField(upload_to='additional_dresses/', null=True)
    add_img3 = models.ImageField(upload_to='additional_dresses/', null=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

class Wishlist(models.Model):
    dress=models.ForeignKey(Dress,on_delete=models.CASCADE)
    

# class User(AbstractBaseUser):
#     email = models.EmailField()
#     title=models.CharField(max_length=5,null=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     password=models.CharField(max_length=8)
#     is_user = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     dob=models.DateField(null=True)
#     country=models.CharField(max_length=100,null=True)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    title = models.CharField(max_length=5, null=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_user = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    dob = models.DateField(null=True)
    country = models.CharField(max_length=100, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin