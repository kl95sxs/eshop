from django.urls import path, include
from vitrina import views
app_name = 'vitrina'

urlpatterns = [
    path('', views.vitrina, name='vitrina'),
    path('<int:product_id>/', views.detail, name='detail'),

]
