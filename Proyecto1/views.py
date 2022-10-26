from datetime import date, datetime
from django.http import HttpResponse

def saludo(request):
    return  HttpResponse("Hola Django - Coder")


def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy facil :) ") 


def DiaDeHoy(request):
    dia = datetime.datetime.now()

    documentoDeTexto = f"Hoy es dia: <br> {dia}"

    return HttpResponse(documentoDeTexto)

def miNombreEs(request, nombre):
    documentoDeTexto = f"Mi nombre es: <br><br> {nombre}"

    return HttpResponse(documentoDeTexto)
