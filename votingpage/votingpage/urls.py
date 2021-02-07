"""votingpage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path

from poll import views as poll_views

urlpatterns = [
    # path('votes/', include('poll.urls')),
    path('voteGood/<poll_id>/', poll_views.voteGood, name='voteGood'),
    path('voteBad/<poll_id>/', poll_views.voteBad, name='voteBad'),
    # path('vote/<poll_id>/', poll_views.vote, name='vote'),
    path('admin/', admin.site.urls),
    path('', poll_views.home, name='home'),
    # path('create/', poll_views.create, name='create'),
    # path('vote/<poll_id>/', poll_views.vote, name='vote'),
    path('resultsGood/<poll_id>/', poll_views.resultsGood, name='resultsGood'),
    path('resultsBad/<poll_id>/', poll_views.resultsBad, name='resultsBad'),
    path('resetPolls/<poll_id>/', poll_views.resetPolls, name='resetPolls'),
]
