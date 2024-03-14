from django.urls import path
from productapi import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken

router=DefaultRouter()
router.register("product",views.ProductView,basename="product")
router.register("user/product",views.UserProductView,basename="userproduct")
router.register('oder/(?P<product_id>\d+)',views.OderView, basename='comment')
router.register('user/oder',views.oderReadView,basename="user_oder")



from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('register/',views.UserSignUpView.as_view()),
    path("token/",ObtainAuthToken.as_view()),
    path('user/count/',views.ProductCountView.as_view(),name="product-count"),
]+router.urls
