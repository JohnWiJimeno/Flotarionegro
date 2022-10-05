from django.contrib import admin
from .models.user import User
from .models.conductor import Conductor
from .models.ruta import Ruta
from .models.vehiculo import Vehiculo
from .models.despacho import Despacho

admin.site.register(User)
admin.site.register(Conductor)
admin.site.register(Ruta)
admin.site.register(Vehiculo)
admin.site.register(Despacho)

# Register your models here.
