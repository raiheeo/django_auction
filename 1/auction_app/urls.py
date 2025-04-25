from rest_framework import routers
from .views import *
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users_list'),
router.register(r'auctions', AuctionViewSet, basename='auction_list'),
router.register(r'bids', BidViewSet, basename='bid_list'),
router.register(r'feedbacks', FeedbackViewSet, basename='feedback_list')
router.register(r'brands', BidViewSet, basename='brand_list'),
router.register(r'models', ModelViewSet, basename='model_list'),
router.register(r'cars', CarViewSet, basename='car_list'),
