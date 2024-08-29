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
from .views.flavor_effect_view import EffectApiView
from .views.flavor_player_view import PlayerApiView
from .views.flavor_race_view import RaceApiView
from .views.flavor_skill_view import SkillApiView
from .views.flavor_stat_view import StatApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flavor/player', PlayerApiView.as_view()),
    path('flavor/attribute', AttributeApiView.as_view()),
    path('flavor/effect', EffectApiView.as_view()),
    path('flavor/race', RaceApiView.as_view()),
    path('flavor/skill', SkillApiView.as_view()),
    path('flavor/stat', StatApiView.as_view()),
]
