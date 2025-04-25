from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField



UserStatusChoices = (
    ('owner', 'owner'),
    ('salesman', 'salesman'),
    ('buyer', 'buyer')
)


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True, validators=[MinValueValidator(18),
                                                                              MaxValueValidator(80)])
    profile_picture = models.ImageField(upload_to='user_image/', null=True, blank=True)
    role = models.CharField(max_length=16, choices=UserStatusChoices, default='buyer')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'
    
class Brand(models.Model):
    brand_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.brand_name


class Model(models.Model):
    model_name = models.CharField(max_length=64)
    brand_model = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name



class Auction(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)
    start_price = models.PositiveSmallIntegerField()
    min_price = models.PositiveSmallIntegerField()
    AUCTION_CHOICES = (
        ('active', 'active'),
        ('completed', 'completed'),
        ('cancelled', 'cancelled')
    )
    status = models.CharField(max_length=32, choices=AUCTION_CHOICES, default='active')

    def __str__(self):
        return f'{self.car}, {self.start_time}'

class Feedback(models.Model):
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='salesman')
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='feedback_buyer')
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                                                                    null=True, blank=True)

    def __str__(self):
        return f'{self.buyer}'
    

class Bid(models.Model):
    amount = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now=True)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.amount}'


    
class Car(models.Model):
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    year = models.DateField(auto_now=True)
    mileage = models.PositiveSmallIntegerField()
    price = models.PositiveSmallIntegerField()
    description = models.TextField()
    images = models.ImageField(upload_to='cars_images', null=True, blank=True)
    FUEL_CHOICES = (
        ('petrol', 'petrol'),
        ('electro', 'electro'),
        ('gas', 'gas')
    )
    fuel_type = MultiSelectField(choices=FUEL_CHOICES, max_length=32, max_choices=2)
    TRANSMISSION_CHOICES = (
        ('automaton', 'automaton'),
        ('mechanics', 'mechanics')
    )
    transmission = models.CharField(max_length=32, choices=TRANSMISSION_CHOICES, default='automaton')

    def __str__(self):
        return f'{self.brand}, {self.model}'























