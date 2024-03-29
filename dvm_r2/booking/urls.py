from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_form, name='booking_form'),
    path('submit/',views.booking_submit,name="booking_submit"),
    path('booking_submit_no_js/',views.booking_submit_no_js,name="booking_submit_no_js"),
    path('mytickets/',views.my_tickets,name="my_tickets"),
    path('mytickets/edit_passenger/<int:booking_id>/',views.edit_passenger,name="edit_passenger")
]
 