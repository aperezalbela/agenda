#encoding:utf-8
from django.db import models

class Distrito(models.Model):
	id_distrito		=	models.AutoField(primary_key=True)
        nombre                  =       models.CharField(max_length=80)

        def __unicode__(self):
                return self.nombre

	class Meta:
		ordering = ["nombre"]

class Contacto(models.Model):
	id_contacto		=	models.AutoField(primary_key=True)
	nombre			=	models.CharField(max_length=50)
	apellido_paterno        =       models.CharField(max_length=50)
	apellido_materno	=	models.CharField(max_length=50)
	telefono		=	models.IntegerField()
	correo			=	models.CharField(max_length=100)
	direccion		=	models.TextField()	
	distrito		=	models.ForeignKey(Distrito,default=1, db_column="id_distrito")	

	def __unicode__(self):
		return self.nombre

	def nombre_completo(self):
		return " ".join([self.apellido_paterno, self.apellido_materno, self.nombre])
