from django.contrib import admin

# Register your models here.
from .models import ( User,Milk,Subscription,MilkCategory,
                MilkCompany,MilkCompanyCategory,Order,Payment,Country,State,City,DeliveryTime,
                FarmerProduct,DailyNeedProduct,DailyPCategory)

admin.site.register(User)
admin.site.register(Milk)
admin.site.register(Subscription)
admin.site.register(MilkCategory)
admin.site.register(MilkCompany)
admin.site.register(MilkCompanyCategory)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(DeliveryTime)
admin.site.register(FarmerProduct)
admin.site.register(DailyNeedProduct)
admin.site.register(DailyPCategory)
