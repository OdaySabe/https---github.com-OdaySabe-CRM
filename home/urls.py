from django.urls import path
from . import views
app_name = "home_app"
urlpatterns = [
    path("",views.home,name='home'),
    path('create-agent/',views.create_agent,name="create_agent"),
    path('delete-agent/', views.delete_agent, name='delete_agent'),
    path('update-agent/', views.update_agent, name='update_agent'),
]
