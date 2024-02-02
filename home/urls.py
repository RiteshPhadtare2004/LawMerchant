from django.urls import path, include
from home import views

urlpatterns = [
    
    path('',views.home, name="Home"),
    path('about',views.about, name="About Us"),
    path('contact',views.contact, name="Contact"),
    path('state',views.state, name="State"),
    path('central',views.central, name="Central"),
    path('verify',views.verify, name="Verify")
]