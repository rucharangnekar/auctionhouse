from django.contrib import admin
from .models import Item, Antique, Painting, Myuser, Cart

admin.site.register(Item)
admin.site.register(Antique)
admin.site.register(Painting)
admin.site.register(Myuser)
admin.site.register(Cart)
