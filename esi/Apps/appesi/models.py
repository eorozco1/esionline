from __future__ import unicode_literals
from django.db import models
# Create your models here.


class Tipopagomod(models.Model):
	tipo = models.CharField(max_length=300,default="")

	def __str__(self):
		return self.tipo

class Tipocursomod(models.Model):
	nombre = models.CharField(max_length=50,default="")

	def __str__(self):
		return self.nombre

class Tipocomputadoramod(models.Model):
	tipo = models.CharField(max_length=50,default="")

	def __str__(self):
		return self.tipo

class Marcamod(models.Model):
	marca = models.CharField(max_length=50,default="")

	def __str__(self):
		return self.marca

class Tipoaccesoriomod(models.Model):
	tipoaccesorio = models.CharField(max_length=50,default="")

	def __str__(self):
		return self.tipoaccesorio

class Cursomod(models.Model):
	fechainicio = models.DateField()
	fechafinal = models.DateField()
	horarioini = models.TimeField()
	horariofin = models.TimeField()
	dias = models.CharField(max_length=500,default="")
	requisitos = models.CharField(max_length=1000,default="")
	descripcion = models.CharField(max_length=1000,default="")
	objetivos = models.CharField(max_length=1000,default="")
	dirigido =  models.CharField(max_length=1000,default="")
	costo = models.CharField(max_length=15,default="")
	costototal = models.CharField(max_length=15,default="")
	tipocursof = models.ForeignKey(Tipocursomod,default="")
	tipopagof = models.ForeignKey(Tipopagomod,default="")

	def __str__(self):
		return self.descripcion

class Computadoramod(models.Model):
	imagen = models.FileField(default="")
	hdd = models.CharField(max_length=15,default="")
	ram = models.CharField(max_length=30,default="")
	pantalla = models.CharField(max_length=30,default="")
	precio = models.CharField(max_length=15,default="")
	otros =  models.CharField(max_length=1500,default="")
	tipocomputadoraf = models.ForeignKey(Tipocomputadoramod,default="")
	marcaf = models.ForeignKey(Marcamod,default="")

	def __str__(self):
		return self.otros

class Accesoriomod(models.Model):
	imagen = models.FileField(default="")
	precio = models.CharField(max_length=15,default="")
	otros = models.CharField(max_length=1500,default="")
	marcaf = models.ForeignKey(Marcamod,default="")
	tipoaccesoriof = models.ForeignKey(Tipoaccesoriomod,default="")

