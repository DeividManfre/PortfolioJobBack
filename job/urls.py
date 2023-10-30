from django.contrib import admin
from rest_framework import routers
from django.urls import include, path
from product.views import ProductListView

router = routers.DefaultRouter()
router.register('product', ProductListView, basename='Product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]