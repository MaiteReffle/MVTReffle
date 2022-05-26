from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from AppFamiliares.models import Familiares
import datetime


def familiar(self):
    familiar = Familiares(nombre="Alejandra",apellido="Ovando",edad=56,fechaDeNacimiento="1966-03-25")
    familiar.save()
    familiar2 = Familiares(nombre="Octavio",apellido="Ovando",edad=55,fechaDeNacimiento="1967-02-05")
    familiar2.save()
    familiar3 = Familiares(nombre="Bruno",apellido="Ovando",edad=30,fechaDeNacimiento="1992-04-22")
    familiar3.save()
    diccionario = {"nombre":familiar.nombre,"apellido":familiar.apellido,"edad":familiar.edad,"fechaDeNacimiento":familiar.fechaDeNacimiento,"nombre2":familiar2.nombre,"apellido2":familiar2.apellido,"edad2":familiar2.edad,"fechaDeNacimiento2":familiar2.fechaDeNacimiento,"nombre3":familiar3.nombre,"apellido3":familiar3.apellido,"edad3":familiar3.edad,"fechaDeNacimiento3":familiar3.fechaDeNacimiento}
    plantilla = loader.get_template('template.html')
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

