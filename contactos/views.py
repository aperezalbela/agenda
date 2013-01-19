from contactos.models import Contacto
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.http import Http404

def lista_contactos(request):
	contactos	=	Contacto.objects.order_by('id_contacto')
	return render_to_response('lista_contactos.html', {'lista': contactos})

def detalle_contacto(request, id_contacto):
	contact		=	get_list_or_404(Contacto, pk=id_contacto)
	return render_to_response('detalle_contacto.html', {'contacto':contact})

def detalle_contacto2(request, nombre_contacto):
	#contact 	=	Contacto.objects.get(nombre__contains=nombre_contacto)
        contact         =       get_list_or_404(Contacto, nombre__contains=nombre_contacto)

	return render_to_response('detalle_contacto.html', {'contacto':contact})
