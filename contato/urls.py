from django.urls import path

from . import views 
urlpatterns = [
    path('', views.contato, name='contato'),
    path('gravar/', views.gravar, name='gravar'),
    path('mostrar/', views.exibe,name='mostrar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('atualizar/<int:id>', views.atualizar, name='atualizar'),
    path('apagar/<int:id>', views.apagar, name='apagar'),
    path('localizar/', views.localizar, name='localizar'),   
    path('image_upload/',views.image_view,name='image_upload'), 
]

