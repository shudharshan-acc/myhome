
from django.urls import path
from . import views
urlpatterns = [
    path('manage/', views.manager,name="manager"),
    # Videos
    path('readvideo/', views.readvideo),
    path('addvideo/', views.add_video),
    path('editvideo/<int:video_id>/', views.edit_video, name='edit_video'),
    path('deletevideo/<int:video_id>/<str:username>', views.delete_video, name='delete_video'),

    # inventory
    path('readinventory/', views.readinventory),
    path('additem/', views.add_item),
    path('deleteitem/<int:item_id>/<str:username>', views.delete_item, name='delete_item'),
    path('incrementitem/<int:item_id>/<str:username>', views.increment_item, name='incrementitem'),
    path('decrementitem/<int:item_id>/<str:username>', views.decrement_item, name='decrementitem'),
]
