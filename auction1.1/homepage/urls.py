from django.conf.urls import url
from . import views

app_name = 'homepage'

urlpatterns = [
    # /homepage/
    url(r'^$', views.index, name='index'),
    url(r'^item/', views.item, name='item'),
    url(r'^antique/', views.antique, name='antique'),
    url(r'^painting/', views.painting, name='painting'),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.detailview, name='detail'),
    url(r'^registration/$', views.getreg, name='register'),
    url(r'^setreg/$', views.regi, name='regi'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^home/(?P<pk>[0-9]+)/detail/$', views.bid, name='bid'),
    url(r'^team/$', views.team, name='team'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^home/(?P<pk>[0-9]+)/detail/cart/$', views.cart1, name='cart1'),
    url(r'^successful_checkout/$', views.successful_checkout, name='successful_checkout'),
    url(r'^del/$', views.DeleteUserItem, name='delete1'),
    url(r'^final/$', views.final, name='final'),
]