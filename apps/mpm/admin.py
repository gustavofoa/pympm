from django.contrib import admin

from .models import Categoria
from .models import Musica


admin.site.register(Categoria)
admin.site.register(Musica)
