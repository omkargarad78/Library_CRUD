from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AdminViewSet, book_list

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'admin', AdminViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('student/books/', book_list, name='book_list'),
] 