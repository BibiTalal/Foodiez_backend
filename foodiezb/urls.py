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
    path('list/category/', views.Categorylist.as_view(), name='category'),
    path('create/category/', views.Categorycreate.as_view(),
         name='create-category'),
    path('recipes/add/', views.RecipeCreateView.as_view(),
         name='create-recipes'),
    path('recipes/', views.Recipelist.as_view(), name='recipes'),
    path('recipes/update/<int:id>',
         views.RecipeUpdateView.as_view(), name='update-recipes'),
    path('recipes/delete/<int:id>/',
         views.DeleteRecipeView.as_view(), name='delete-recipes'),
    path('list/ingrediants/', views.IngrediantCreateView.as_view(), name='ingrediants'),
    path('ingrediants/update/<int:id>/',
         views.IngrediantUpdateView.as_view(), name='update-ingrediants'),
    path('ingrediants/delete/<int:id>/',
         views.DeleteIngrediantView.as_view(), name='delete-ingrediants'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
