from contactos.models import Contacto
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from contactos.forms import ContactoForm
from django.core.mail import EmailMessage
#from django.template import RequestContext

def gracias(request):
	return render(request, 'gracias.html')

def lista_contactos(request):
	contactos	=	Contacto.objects.order_by('apellido_paterno')
	return render_to_response('lista_contactos.html', {'lista': contactos})

def contacto(request, id_contacto):
	contact	= get_object_or_404(Contacto, pk=id_contacto,)
	
	if request.method=='GET':
		formulario = ContactoForm(instance=contact)
		#return render_to_response('detalle_contacto.html', {'contacto': contact, 'formulario': formulario})
		return render(request, 'detalle_contacto.html', {'contacto': contact, 'formulario': formulario})
	elif request.method=='POST':
		form = ContactoForm(request.POST, instance=contact)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/contacto/'+str(id_contacto))
		else:
			return render(request, 'detalle_contacto.html', {'contacto': contact, 'formulario': form})

def detalle_contacto2(request, id_contacto):
	#contact 	=	Contacto.objects.get(nombre__contains=id_contacto)
        contact         =       get_list_or_404(Contacto, nombre__contains=id_contacto)

	return render_to_response('detalle_contacto.html', {'contacto':contact})

def contactar(request):
	if request.method=='POST':
		formulario = ContactoForm(request.POST)
		if formulario.is_valid():
			titulo 		= 'Mensaje desde el contacto de la Agenda Virtual'
			contenido	= formulario.cleaned_data['mensaje'] + '\n'
			contenido	+= 'Comunicarse a: ' + formulario.cleaned_data['correo']
			correo		= EmailMessage(titulo, contenido, to=['andres@seguridadinformatica.org'])
			correo.send()
			return HttpResponseRedirect('/gracias')
	else:
		formulario = ContactoForm()
	return render(request, 'contactoform.html', {'formulario': formulario})
	# return render_to_response('contactoform.html', {'formulario': formulario}, context_instance = RequestContext(request))
