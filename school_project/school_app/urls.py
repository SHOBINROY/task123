from . import views
from django.urls import path

from .views import OrderView

app_name="school_app"

urlpatterns = [
      path('',views.index,name="index"),
      path('order1/', views.order1, name='order1'),

      path('course/',views.course,name="course"),
      path('art/',views.art,name="art"),
      path('cs/',views.cs,name="cs"),
      path('ss/',views.ss,name="ss"),
      path('md/',views.md,name="md"),


]
