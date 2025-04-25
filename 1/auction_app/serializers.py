from .models import Auction, Feedback, Bid, UserProfile, Car, Brand, Model
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', ]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['brand_name', ]


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['model_name', ]


class CarSerializer(serializers.ModelSerializer):
    seller = UserProfileSimpleSerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    model = ModelSerializer(read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'brand', 'description', 'model', 'year', 'mileage', 'price',
                  'images', 'seller', ]


class AuctionSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    end_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    car = CarSerializer(read_only=True)

    class Meta:
        model = Auction
        fields = ['id', 'car', 'start_time', 'end_time', 'start_price', 'min_price', ]
                  


class BidSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = Bid
        fields = ['id', 'auction', 'created_at', 'buyer', 'amount', ]


class FeedbackSerializer(serializers.ModelSerializer):
    seller = UserProfileSimpleSerializer(read_only=True)
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    buyer = UserProfileSimpleSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = ['id',  'rating', 'comment', 'created_at',  'seller', 'buyer', ]









