from contactos.models import Contacto, Distrito
from django.contrib import admin

class ContactoAdmin(admin.ModelAdmin):
	
	list_display = ('apellidos_concat', 'nombre', 'correo')
	
	def apellidos_concat(self, instance):
		return instance.apellido_paterno+' '+instance.apellido_materno

	apellidos_concat.short_description = 'Apellidos'	

class DistritoAdmin(admin.ModelAdmin):

	list_display = ('nombre', )	

admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Distrito, DistritoAdmin)
