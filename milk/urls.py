from django.urls import path,include
from .views import( UserListView,UserCreateView,UserUpdateView, MilkListView,MilkCreateView,MilkUpdateView,
            SubscriptionCreateView,SubscriptionListView,SubscriptionUpdateView,MilkCategoryCreateView,
            MilkCategoryListView,MilkCategoryUpdateView,MilkCompanyCreateView,MilkCompanyListView,MilkCompanyUpdateView,
            MilkCompanyCategoryCreateView,MilkCompanyCategoryListView,MilkCompanyCategoryUpdateView,
            OrderCreateView,OrderListView,OrderUpdateView,PaymentUpdateView,PaymentCreateView,PaymentListView,
            CountryCreateView,CountryListView,CountryUpdateView,StateCreateView,StateListView,StateUpdateView,
            CityCreateView,CityListView,CityUpdateView,DTCreateView,DTListView,DTUpdateView,
            FPCreateView,FPListView,FPUpdateView,UserDeleteView,MilkCategoryDeleteView,MilkDeleteView,SubscriptionDeleteView,
            MilkCompanyCategoryDeleteView,MilkCompanyDeleteView,OrderDeleteView,PaymentDeleteView,CountryDeleteView,
            StateDeleteView,DTDeleteView,FPDeleteView,CityDeleteView,UserRetrieveView,MilkRetrieveView,SubscriptionRetrieveView,
            MilkCategoryRetrieveView,MilkCompanyRetrieveView,MilkCompanyCategoryRetrieveView,OrderRetrieveView,
            PaymentRetrieveView,CountryRetrieveView,StateRetrieveView,CityRetrieveView,DTRetrieveView,
            FPRetrieveView,DPListView,DPCreateView,DPUpdateView,DPDeleteView,DPRetrieveView,DPCListView,
            DPCCreateView,DPCUpdateView,DPCDeleteView,DPCRetrieveView,AddToCartView,ProfilePhotoUpload

)
app_name = 'api'

urlpatterns = [
    #User
    path('user/',UserListView.as_view(), name="user-list"),
    path('usercreate',UserCreateView.as_view(), name="user-create"),
    path('userupdate/<int:user_id>',UserUpdateView.as_view(),name='user-update'),
    path('userdelete/<int:user_id>',UserDeleteView.as_view(),name='user-delete'),
    path('userretrieve/<int:user_id>',UserRetrieveView.as_view(),name='user-retrieve'),

    #Milk
    path('milk/',MilkListView.as_view(), name="milk-list"),
    path('milkcreate',MilkCreateView.as_view(), name="milk-create"),
    path('milkupdate/<int:milk_id>',MilkUpdateView.as_view(),name='milk-update'),
    path('milkdelete/<int:milk_id>',MilkDeleteView.as_view(),name='milk-delete'),
    path('milkretrieve/<int:milk_id>',MilkRetrieveView.as_view(),name='milk-retrieve'),

    #Subscription
    path('sub/',SubscriptionListView.as_view(), name="sub-list"),
    path('subcreate',SubscriptionCreateView.as_view(), name="sub-create"),
    path('subupdate/<int:payment_id>',SubscriptionUpdateView.as_view(),name='sub-update'),
    path('subdelete/<int:payment_id>',SubscriptionDeleteView.as_view(),name='sub-delete'),
    path('subretrieve/<int:payment_id>',SubscriptionRetrieveView.as_view(),name='sub-retrieve'),

    #MilkCategory
    path('mc/',MilkCategoryListView.as_view(), name="mc-list"),
    path('mccreate',MilkCategoryCreateView.as_view(), name="mc-create"),
    path('mcupdate/<int:c_id>',MilkCategoryUpdateView.as_view(),name='mc-update'),
    path('mcdelete/<int:c_id>',MilkCategoryDeleteView.as_view(),name='mc-delete'),
    path('mcretrieve/<int:c_id>',MilkCategoryRetrieveView.as_view(),name='mc-retrieve'),

    #MilkCompany
    path('mco/',MilkCompanyListView.as_view(), name="mco-list"),
    path('mcocreate',MilkCompanyCreateView.as_view(), name="mco-create"),
    path('mcoupdate/<slug:name>',MilkCompanyUpdateView.as_view(),name='mco-update'),
    path('mcodelete/<slug:name>',MilkCompanyDeleteView.as_view(),name='mco-delete'),
    path('mcoretrieve/<slug:name>',MilkCompanyRetrieveView.as_view(),name='mco-retrieve'),

    #MilkCompanyCategory
    path('mcoc/',MilkCompanyCategoryListView.as_view(), name="mcoc-list"),
    path('mcoccreate',MilkCompanyCategoryCreateView.as_view(), name="mcoc-create"),
    path('mcocupdate/<int:milk_category_id>',MilkCompanyCategoryUpdateView.as_view(),name='mcoc-update'),
    path('mcocdelete/<int:milk_category_id>',MilkCompanyCategoryDeleteView.as_view(),name='mcoc-delete'),
    path('mcocretrieve/<int:milk_category_id>',MilkCompanyCategoryRetrieveView.as_view(),name='mcoc-retrieve'),

    #Order
    path('order/',OrderListView.as_view(), name="order-list"),
    path('ordercreate',OrderCreateView.as_view(), name="order-create"),
    path('orderupdate/<int:user_id>',OrderUpdateView.as_view(),name='order-update'),
    path('orderdelete/<int:user_id>',OrderDeleteView.as_view(),name='order-delete'),
    path('orderretrieve/<int:user_id>',OrderRetrieveView.as_view(),name='order-retrieve'),

    #Payment
    path('payment/',PaymentListView.as_view(), name="payment-list"),
    path('paymentcreate',PaymentCreateView.as_view(), name="payment-create"),
    path('paymentupdate/<int:user_id>',PaymentUpdateView.as_view(),name='payment-update'),
    path('paymentdelete/<int:user_id>',PaymentDeleteView.as_view(),name='payment-delete'),
    path('paymentretrieve/<int:user_id>',PaymentRetrieveView.as_view(),name='payment-retrieve'),

    #Country
    path('country/',CountryListView.as_view(), name="country-list"),
    path('countrycreate',CountryCreateView.as_view(), name="country-create"),
    path('countryupdate/<int:country_code>',CountryUpdateView.as_view(),name='country-update'),
    path('countrydelete/<int:country_code>',CountryDeleteView.as_view(),name='country-delete'),
    path('countryretrieve/<int:country_code>',CountryRetrieveView.as_view(),name='country-retrieve'),

    #State
    path('state/',StateListView.as_view(), name="state-list"),
    path('statecreate',StateCreateView.as_view(), name="state-create"),
    path('stateupdate/<slug:state_name>',StateUpdateView.as_view(),name='state-update'),
    path('statedelete/<slug:state_name>',StateDeleteView.as_view(),name='state-delete'),
    path('stateretrieve/<slug:state_name>',StateRetrieveView.as_view(),name='state-retrieve'),

    #City
    path('city/',CityListView.as_view(), name="city-list"),
    path('citycreate',CityCreateView.as_view(), name="city-create"),
    path('cityupdate/<slug:city_name>',CityUpdateView.as_view(),name='city-update'),
    path('citydelete/<slug:city_name>',CityDeleteView.as_view(),name='city-delete'),
    path('cityretrieve/<slug:city_name>',CityRetrieveView.as_view(),name='city-retrieve'),

    #DeliveryTime
    path('dt/',DTListView.as_view(), name="dt-list"),
    path('dtcreate',DTCreateView.as_view(), name="dt-create"),
    path('dtupdate/<int:user_id>',DTUpdateView.as_view(),name='dt-update'),
    path('dtdelete/<int:user_id>',DTDeleteView.as_view(),name='dt-delete'),
    path('dtretrieve/<int:user_id>',DTRetrieveView.as_view(),name='dt-retrieve'),

    #FarmerProduct
    path('fp/',FPListView.as_view(), name="fp-list"),
    path('fpcreate',FPCreateView.as_view(), name="fp-create"),
    path('fpupdate/<slug:name>',FPUpdateView.as_view(),name='fp-update'),
    path('fpdelete/<slug:name>',FPDeleteView.as_view(),name='fp-delete'),
    path('fpretrieve/<slug:name>',FPRetrieveView.as_view(),name='fp-retrieve'),

    #DailyneedProduct
    path('dp/',DPListView.as_view(), name="dp-list"),
    path('dpcreate',DPCreateView.as_view(), name="dp-create"),
    path('dpupdate/<slug:name>',DPUpdateView.as_view(),name='dp-update'),
    path('dpdelete/<slug:name>',DPDeleteView.as_view(),name='dp-delete'),
    path('dpretrieve/<slug:name>',DPRetrieveView.as_view(),name='dp-retrieve'),

    #DailyN_Product_Category
    path('dpc/',DPCListView.as_view(), name="dpc-list"),
    path('dpccreate',DPCCreateView.as_view(), name="dpc-create"),
    path('dpcupdate/<int:d_id>',DPCUpdateView.as_view(),name='dpc-update'),
    path('dpcdelete/<int:d_id>',DPCDeleteView.as_view(),name='dpc-delete'),
    path('dpcretrieve/<int:d_id>',DPCRetrieveView.as_view(),name='dpc-retrieve'),

    # AddToCart 
    path('addtocartcreate',AddToCartView.as_view(), name="addtocart"),
    path('addtocartdelete',AddToCartView.as_view(), name="addtocartdelete"),
    path('addtocartget',AddToCartView.as_view(), name="addtocartget"),

    # ProfilePhotos
    path('profilephoto',ProfilePhotoUpload.as_view(), name="profilephoto"),
]

