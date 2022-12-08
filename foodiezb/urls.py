"""foodiezb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backend import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("signin/", views.SigninView.as_view(), name="signin"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path('list/cuisine/', views.Cuisinelist.as_view(), name='cuisine'),
    path('create/cuisine/', views.Cuisinecreate.as_view(),
         name='create-cuisine'),
    path('dishes/create/', views.DishCreateView.as_view(),
         name='create-dishes'),
    path('dish/', views.Dishlist.as_view(), name='dish'),
    path('dishes/update/<int:dish_id>/',
         views.DishUpdateView.as_view(), name='update-dish'),
    path('dish/delete/<int:dish_id>/',
         views.DeleteDishView.as_view(), name='delete-dish'),
    path('ingrediants/creeate/',
         views.IngrediantCreateView.as_view(), name='create-ingrediants'),
    path('list/ingrediants/', views.IngrediantList.as_view(), name='ingrediants'),
    path('ingrediants/update/<int:ingrediant_id>/',
         views.IngrediantUpdateView.as_view(), name='update-ingrediants'),
    path('ingrediants/delete/<int:ingrediant_id>/',
         views.DeleteIngrediantView.as_view(), name='delete-ingrediants'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
