from . import views
from django.urls import path

from .views import HomeView, OrderView

app_name="school_app"

urlpatterns = [
      path('',views.index,name="index"),
      path('order1/', views.order1, name='order1'),
      path('<int:pk>/', OrderView.as_view(), name='order'),
      path('department/', HomeView.as_view(), name='department'),
      path('course/',views.course,name="course"),
      path('art/',views.art,name="art"),
      path('cs/',views.cs,name="cs"),
      path('ss/',views.ss,name="ss"),
      path('md/',views.md,name="md"),


]
