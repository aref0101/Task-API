from django.urls import path
from rest_framework.routers import DefaultRouter
from .import views
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)


router= DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
urlpatterns= router.urls

urlpatterns+= [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('register/', views.RegisterView.as_view()),
]