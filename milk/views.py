from rest_framework.parsers import FileUploadParser
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
import json
from .models import (User, Milk, Subscription, MilkCategory,
                     MilkCompany, MilkCompanyCategory, Order, Payment, Country, State, City, DeliveryTime,
                     Address, FarmerProduct, DailyNeedProduct, DailyPCategory, AddToCart)

from .serializers import (UserSerializer, MilkSerializer, SubscriptionSerializer, MilkCategorySerializer, MilkCompanySerializer,
                          MilkCompanyCategorySerializer, OrderSerializer, PaymentSerializer, CountrySerializer, StateSerializer,
                          CitySerializer, DeliveryTimeSerializer, AddressSerializer, FarmerProductSerializer,
                          LoginSerializer, DailyNeedProductSerializer, DailyPCategorySerializer, AddToCartSerializer,ProfilePhotoSerializer)
from rest_framework.views import APIView
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)

# User

class ProfilePhotoUpload(APIView):
    parser_class = (FileUploadParser,)
    def post(self,request,*args,**kwargs):
        try:
            user=User.objects.get(id=request.data['id'])
            profile_serializer=ProfilePhotoSerializer(user,data=request.data)
            if profile_serializer.is_valid():
                profile_serializer.save()
                return Response(profile_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as NE:
            return Response({"message":"Not Exist","status":status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'user_id'


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'user_id'


class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'user_id'

# Milk


class MilkListView(generics.ListAPIView):
    queryset = Milk.objects.all()
    serializer_class = MilkSerializer


class MilkCreateView(generics.CreateAPIView):
    queryset = Milk.objects.all()
    serializer_class = MilkSerializer


class MilkUpdateView(generics.UpdateAPIView):
    queryset = Milk.objects.all()
    serializer_class = MilkSerializer
    lookup_field = 'milk_id'


class MilkDeleteView(generics.DestroyAPIView):
    queryset = Milk.objects.all()
    serializer_class = MilkSerializer
    lookup_field = 'milk_id'


class MilkRetrieveView(generics.RetrieveAPIView):
    queryset = Milk.objects.all()
    serializer_class = MilkSerializer
    lookup_field = 'milk_id'

# Subscription


class SubscriptionListView(generics.ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class SubscriptionCreateView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class SubscriptionUpdateView(generics.UpdateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    lookup_field = 'payment_id'


class SubscriptionDeleteView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    lookup_field = 'payment_id'


class SubscriptionRetrieveView(generics.RetrieveAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    lookup_field = 'payment_id'

# MilkCategory


class MilkCategoryListView(generics.ListAPIView):
    queryset = MilkCategory.objects.all()
    serializer_class = MilkCategorySerializer


class MilkCategoryCreateView(generics.CreateAPIView):
    queryset = MilkCategory.objects.all()
    serializer_class = MilkCategorySerializer


class MilkCategoryUpdateView(generics.UpdateAPIView):
    queryset = MilkCategory.objects.all()
    serializer_class = MilkCategorySerializer
    lookup_field = 'c_id'


class MilkCategoryDeleteView(generics.DestroyAPIView):
    queryset = MilkCategory.objects.all()
    serializer_class = MilkCategorySerializer
    lookup_field = 'c_id'


class MilkCategoryRetrieveView(generics.RetrieveAPIView):
    queryset = MilkCategory.objects.all()
    serializer_class = MilkCategorySerializer
    lookup_field = 'c_id'

# MilkCompany


class MilkCompanyListView(generics.ListAPIView):
    queryset = MilkCompany.objects.all()
    serializer_class = MilkCompanySerializer


class MilkCompanyCreateView(generics.CreateAPIView):
    queryset = MilkCompany.objects.all()
    serializer_class = MilkCompanySerializer


class MilkCompanyUpdateView(generics.UpdateAPIView):
    queryset = MilkCompany.objects.all()
    serializer_class = MilkCompanySerializer
    lookup_field = 'name'


class MilkCompanyDeleteView(generics.DestroyAPIView):
    queryset = MilkCompany.objects.all()
    serializer_class = MilkCompanySerializer
    lookup_field = 'name'


class MilkCompanyRetrieveView(generics.RetrieveAPIView):
    queryset = MilkCompany.objects.all()
    serializer_class = MilkCompanySerializer
    lookup_field = 'name'

# MilkCompanyCategory


class MilkCompanyCategoryListView(generics.ListAPIView):
    queryset = MilkCompanyCategory.objects.all()
    serializer_class = MilkCompanyCategorySerializer


class MilkCompanyCategoryCreateView(generics.CreateAPIView):
    queryset = MilkCompanyCategory.objects.all()
    serializer_class = MilkCompanyCategorySerializer


class MilkCompanyCategoryUpdateView(generics.UpdateAPIView):
    queryset = MilkCompanyCategory.objects.all()
    serializer_class = MilkCompanyCategorySerializer
    lookup_field = 'milk_category_id'


class MilkCompanyCategoryDeleteView(generics.DestroyAPIView):
    queryset = MilkCompanyCategory.objects.all()
    serializer_class = MilkCompanyCategorySerializer
    lookup_field = 'milk_category_id'


class MilkCompanyCategoryRetrieveView(generics.RetrieveAPIView):
    queryset = MilkCompanyCategory.objects.all()
    serializer_class = MilkCompanyCategorySerializer
    lookup_field = 'milk_category_id'

# Order


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'user_id'


class OrderDeleteView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'user_id'


class OrderRetrieveView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'user_id'

# Payment


class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentUpdateView(generics.UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    lookup_field = 'user_id'


class PaymentDeleteView(generics.DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    lookup_field = 'user_id'


class PaymentRetrieveView(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    lookup_field = 'user_id'

# Country


class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryCreateView(generics.CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryUpdateView(generics.UpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'country_code'


class CountryDeleteView(generics.DestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'country_code'


class CountryRetrieveView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'country_code'

# State


class StateListView(generics.ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class StateCreateView(generics.CreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class StateUpdateView(generics.UpdateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    lookup_field = 'state_name'


class StateDeleteView(generics.DestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    lookup_field = 'state_name'


class StateRetrieveView(generics.RetrieveAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    lookup_field = 'state_name'

# City


class CityListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityCreateView(generics.CreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityUpdateView(generics.UpdateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'city_name'


class CityDeleteView(generics.DestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'city_name'


class CityRetrieveView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'city_name'

# DeliveryTime


class DTListView(generics.ListAPIView):
    queryset = DeliveryTime.objects.all()
    serializer_class = DeliveryTimeSerializer


class DTCreateView(generics.CreateAPIView):
    queryset = DeliveryTime.objects.all()
    serializer_class = DeliveryTimeSerializer


class DTUpdateView(generics.UpdateAPIView):
    queryset = DeliveryTime.objects.all()
    serializer_class = DeliveryTimeSerializer
    lookup_field = 'user_id'


class DTDeleteView(generics.DestroyAPIView):
    queryset = DeliveryTime.objects.all()
    serializer_class = DeliveryTimeSerializer
    lookup_field = 'user_id'


class DTRetrieveView(generics.RetrieveAPIView):
    queryset = DeliveryTime.objects.all()
    serializer_class = DeliveryTimeSerializer
    lookup_field = 'user_id'

# FarmerProduct


class FPListView(generics.ListAPIView):
    queryset = FarmerProduct.objects.all()
    serializer_class = FarmerProductSerializer


class FPCreateView(generics.CreateAPIView):
    queryset = FarmerProduct.objects.all()
    serializer_class = FarmerProductSerializer


class FPUpdateView(generics.UpdateAPIView):
    queryset = FarmerProduct.objects.all()
    serializer_class = FarmerProductSerializer
    lookup_field = 'name'


class FPDeleteView(generics.DestroyAPIView):
    queryset = FarmerProduct.objects.all()
    serializer_class = FarmerProductSerializer
    lookup_field = 'name'


class FPRetrieveView(generics.RetrieveAPIView):
    queryset = FarmerProduct.objects.all()
    serializer_class = FarmerProductSerializer
    lookup_field = 'name'

# DailyNeedProduct


class DPListView(generics.ListAPIView):
    queryset = DailyNeedProduct.objects.all()
    serializer_class = DailyNeedProductSerializer


class DPCreateView(generics.CreateAPIView):
    queryset = DailyNeedProduct.objects.all()
    serializer_class = DailyNeedProductSerializer


class DPUpdateView(generics.UpdateAPIView):
    queryset = DailyNeedProduct.objects.all()
    serializer_class = DailyNeedProductSerializer
    lookup_field = 'name'


class DPDeleteView(generics.DestroyAPIView):
    queryset = DailyNeedProduct.objects.all()
    serializer_class = DailyNeedProductSerializer
    lookup_field = 'name'


class DPRetrieveView(generics.RetrieveAPIView):
    queryset = DailyNeedProduct.objects.all()
    serializer_class = DailyNeedProductSerializer
    lookup_field = 'name'

# DailyPCategory


class DPCListView(generics.ListAPIView):
    queryset = DailyPCategory.objects.all()
    serializer_class = DailyPCategorySerializer


class DPCCreateView(generics.CreateAPIView):
    queryset = DailyPCategory.objects.all()
    serializer_class = DailyPCategorySerializer


class DPCUpdateView(generics.UpdateAPIView):
    queryset = DailyPCategory.objects.all()
    serializer_class = DailyPCategorySerializer
    lookup_field = 'd_id'


class DPCDeleteView(generics.DestroyAPIView):
    queryset = DailyPCategory.objects.all()
    serializer_class = DailyPCategorySerializer
    lookup_field = 'd_id'


class DPCRetrieveView(generics.RetrieveAPIView):
    queryset = DailyPCategory.objects.all()
    serializer_class = DailyPCategorySerializer
    lookup_field = 'd_id'

# AddtoCart View


class AddToCartView(APIView):
    def post(self, request):
        try:
            serializer = AddToCartSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            user = AddToCart.objects.filter(
                user_id=data['user_id'], milk_id=data['milk_id'])
            price = Milk.objects.get(id=request.data['milk_id'])
            price = price.price
            if user.exists():
                user.update(qty=data['qty'])
            else:
                user = AddToCart.objects.create(
                    user_id=data['user_id'], qty=data['qty'], status=data['status'], milk_id=data['milk_id'])
            return Response({"data": serializer.data, "price": price, "status": 201})
        except Exception as e:
            print(e)
            return Response({"error": "Server Error", "status": 500})

    def delete(self, request):
        try:
            print(request.data)
            user_id = request.data['user_id']
            milk_id = request.data['milk_id']

            print(user_id,milk_id)
            cart = AddToCart.objects.filter(user_id=user_id, milk_id=milk_id)
            if cart.exists():
                cart.delete()
            else:
                return Response({"date": "Not Found", "status": 404})
            return Response({"date": "Deleted", "status": 204})
            # return JsonResponse({"message": "user id `{}` Milk ID `{}` has been deleted.".format(user_id,milk_id)},status=204)
        except Exception as e:
            print("Error",e)
            return Response({"error": "Server Error", "status": 500})

    def get(self, request):
        try:
            carddata = []
            cart = AddToCart.objects.all()

            serializer = AddToCartSerializer(cart, many=True)
            for i in serializer.data:
                price = Milk.objects.get(id=i['milk_id']).price
                name = Milk.objects.get(id=i['milk_id']).milk_name
                carddata.append({"id": i["id"], "qty": i["qty"], "status": i["status"],
                                 "user_id": i["user_id"], "milk_id": i["milk_id"], "price": price, "milk_name": name})
            return Response({"data": carddata, "status": 200})
        except Exception as e:
            print(e)
            return Response({"error": "Server Error", "status": 500})
