from django.urls import path, include, reverse

from . import views

urlpatterns = [

    # path("january", views.january),
    #  path("february", views.february)
    path("",  views.index, name="index"), 
    path("<int:month>",views.monthly_challanges_by_number),
    path("<str:month>",views.monthy_challanges_by_string, name="month-challange")

]
