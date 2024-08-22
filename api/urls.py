from django.urls import path

from . import views
from .crud_apis import animal, usuario, adopcion

animalespatterns = [
    path("animal-list", animal.List, name="animal-list"), 
    path("animal-detail/<str:pk>",animal.Detail,name="animal-detail"),
    path("animal-create",animal.Create,name="animal-create"),
    path("animal-update/<str:pk>",animal.Update,name="animal-update"),
    path("animal-delete/<str:pk>",animal.Delete,name="animal-delete")
]

usuariopatterns = [
    path("usuario-validar-contra", usuario.ValidarContra, name="usuario-validar-contra"), 
    path("adoptantes-list", usuario.ListAdoptantes, name="usuario-list"), 
    path("voluntarios-list", usuario.ListVoluntarios, name="usuario-list"), 
    path("usuario-detail/<str:pk>",usuario.Detail,name="usuario-detail"),
    path("usuario-create",usuario.Create,name="usuario-create"),
    path("usuario-update/<str:pk>",usuario.Update,name="usuario-update"),
    path("usuario-delete/<str:pk>",usuario.Delete,name="usuario-delete")
]

adopcionpatterns = [
    path("adopcion-list", adopcion.List, name="adopcion-list"), 
    path("adopcion-detail/<str:pk>",adopcion.Detail,name="adopcion-detail"),
    path("adopcion-create",adopcion.Create,name="adopcion-create"),
    path("adopcion-update/<str:pk>",adopcion.Update,name="adopcion-update"),
    path("adopcion-delete/<str:pk>",adopcion.Delete,name="adopcion-delete"),
    path("adopcion-creacion-edicion-animal",adopcion.CreateAdopcionEditAnimal,name="adopcion-creacion-edicion-animal")

]

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
]+animalespatterns+usuariopatterns+adopcionpatterns