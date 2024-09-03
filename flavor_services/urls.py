"""
URL configuration for flavor_services project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from .views.flavor_attribute_view import AttributeApiView
from .views.flavor_currency_view import CurrencyApiView
from .views.flavor_denizen_view import DenizenApiView
from .views.flavor_inventory_view import InventoryApiView
from .views.flavor_item_view import ItemApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flavor/denizen', DenizenApiView.as_view()),
    path('flavor/attribute', AttributeApiView.as_view()),
    path('flavor/inventory', InventoryApiView.as_view()),
    path('flavor/item', ItemApiView.as_view()),
    path('flavor/currency', CurrencyApiView.as_view()),
]
