from django.contrib import admin
from .models import Rol, Categoria, Usuario, Publicacion

# Registrar los modelos en el panel de administración
admin.site.register(Rol)
admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(Publicacion)

