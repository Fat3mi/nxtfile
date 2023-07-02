from django.urls import path
from . import views
urlpatterns = [
    path('about_us/',views.aboutus,name='about_us'),
    path('contact_us/',views.ContactUsCreateView.as_view(),name='contact_us'),
]