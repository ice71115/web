from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('photos/', views.LocationPhotosListView.as_view(), name='Photos'),
    path('photo/<int:pk>/', views.LocationPhotosDetailView.as_view(), name='Photo-detail'),
]
urlpatterns += [  
    path('photo/create/', views.PhotoCreate.as_view(), name='photo_create'),
    path('photo/<int:pk>/update/', views.PhotoUpdate.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete/', views.PhotoDelete.as_view(), name='photo_delete'),
]