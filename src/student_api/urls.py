from django.urls import path
from .views import home, manual_api, student_list_api, student_list_api2, student_add_api, student_api

urlpatterns = [
    path('', home),
    # path('student/', manual_api),
    path('list/', student_list_api),
    path('list2/', student_list_api2),
    path('add/', student_add_api),
    path('student/', student_api),

]
