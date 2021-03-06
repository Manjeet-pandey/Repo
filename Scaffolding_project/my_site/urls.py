from django.urls import include,path
from . import views
from django.views.generic import RedirectView

urlpatterns=[
    path('product/',include('product.urls')),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('account/',include('account.urls')),
    path('',RedirectView.as_view(url='dashboard/')),
    ]
