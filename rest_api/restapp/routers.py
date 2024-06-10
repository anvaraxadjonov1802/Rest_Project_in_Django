from rest_framework.routers import DefaultRouter
from .views import ProductViwset

router = DefaultRouter()


router.register("products", ProductViwset, basename='product')