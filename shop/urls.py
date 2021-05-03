"""ProductProjectUsingSQL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from .views import BrandCreate,BrandEdit,BrandDelete,\
    MobileCreate,MobileList,OrderCreate,\
    Orderlist,\
    OrderCancel,OrderDetails,AddToCart,Cartview,CartDelete,\
    UserRegistration,UserLogin,UserLogout


urlpatterns = [
    path('',lambda request:render(request,'shop/base.html')),
    path('brandcreate',BrandCreate.as_view(),name='brandcreate'),
    path('brandedit/<int:id>',BrandEdit.as_view(),name='brandedit'),
    path('branddelete/<int:id>',BrandDelete.as_view(),name='branddelete'),
    path('mobilecreate',MobileCreate.as_view(),name='mobilecreate'),
    path('mobilelist',MobileList.as_view(),name='mobilelist'),
    path('ordercreate/<int:id>',OrderCreate.as_view(),name='ordercreate'),
    path('userregistration',UserRegistration.as_view(),name='register'),
    path('userlogin',UserLogin.as_view(),name='userlogin'),
    path('userlogout',UserLogout.as_view(),name='userlogout'),
    path('orderlist',Orderlist.as_view(),name='orderlist'),
    path('ordercancel/<int:pk>',OrderCancel.as_view(),name='ordercancel'),
    path('orderdetails/<int:pk>',OrderDetails.as_view(),name='orderdetails'),
    path('addtocart/<int:id>',AddToCart.as_view(),name='addtocart'),
    path('cartview',Cartview.as_view(),name='cartview'),
    path('cartdelete/<int:pk>',CartDelete.as_view(),name='cartdelete'),
    path('errorpage',lambda request:render(request,'shop/errorpage.html'),name='errorpage')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
