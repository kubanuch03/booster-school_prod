from django.urls import path

from .views import EventListApiView, EventDetailApiView


urlpatterns = [
    path('list/events/',EventListApiView.as_view(),name= 'list-event'),
    path('detail/events/',EventDetailApiView.as_view(),name= 'detail-event-id')
]