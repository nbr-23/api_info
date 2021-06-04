from django.urls import path
from . import views
urlpatterns = [
    path('employes/', views.allEmploye),
    path('departs/', views.allDepart),
    path('employe/<int:id>/', views.getEmploye),
    path('depart/<int:id>/', views.getDepart),
    path('add_employe/', views.addEmploye),
    path('add_depart/', views.addDepart),
    path('update_depart/<int:id>/', views.updateDepart),
    path('update_employe/<int:id>/', views.addEmploye),
    path('del_employe/<int:id>/', views.delEmploye),
    
]
