from rest_framework import serializers
from milk.models import (User, Milk, Subscription, MilkCategory,
                         MilkCompany, MilkCompanyCategory, Order, Payment, Country, State, City, DeliveryTime,
                         FarmerProduct, DailyNeedProduct, DailyPCategory, AddToCart)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivated."
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials."
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password both."
            raise exceptions.ValidationError(msg)
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfilePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['profile_photo','id']

class MilkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milk
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class MilkCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkCategory
        fields = '__all__'


class MilkCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkCompany
        fields = '__all__'


class MilkCompanyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkCompanyCategory
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class DeliveryTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryTime
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['address','address2','postal_code','state','city']

class FarmerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerProduct
        fields = '__all__'


class DailyNeedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyNeedProduct
        fields = '__all__'


class DailyPCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPCategory
        fields = '__all__'


class AddToCartSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = AddToCart
        fields = ("id", "qty", "status", "user_id", "milk_id")
