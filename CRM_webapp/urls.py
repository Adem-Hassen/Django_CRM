from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("user_login/",views.user_login,name='user_login'),
    path("signup/",views.signup,name="signup"),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('dashboard/',views.dashboard,name="dashboard"),
    path("record/<int:pk>",views.user_record,name="record"),
    path("back_to_records/",views.back_to_records,name="back_to_records"),
    path("delete_record/<int:pk>",views.delete_record,name="delete_record"),
    path("add_record/",views.add_record,name="add_record"),
    path("update_record/<int:pk>",views.update_record,name="update_record"),
    ]
