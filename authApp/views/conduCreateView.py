from optparse import Values
from django.views import View
from authApp.models import conductor,Conductor
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


class ConductorView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,pk=0):
        if (pk>0):
            conductores=list(Conductor.objects.filter(pk=pk).values())
            if len(conductores)>0:
                conducu=conductores[0]
                datos={'messages':"success", 'conductor':conductores}
            else:
                datos={'messages':"No se encontro registro"}
            return JsonResponse(datos)
        else:
            conductores=list(Conductor.objects.values())
            if len(conductores)>0:
                datos={'messages':"success",'conductor':conductores}
            else:
                datos={'messages':"No e encontro registro"}
            return JsonResponse(datos)


    def post(self, request):
        jd=json.loads(request.body)
        Conductor.objects.create(idconductor=jd['idconductor'],nombre=jd['nombre'],apellidos=jd['apellidos'],telefono=jd['telefono'],email=jd['email'],direccion=jd['direccion'])
        datos={'messages':"success"}
        return JsonResponse(datos)   


    def put(self, request,pk):
        jd=json.loads(request.body)
        conductores=list(Conductor.objects.filter(pk=pk).values())
        if len(conductores)>0:
            conducu=Conductor.objects.get(pk=pk)
            conducu.idconductor=jd['idconductor']
            conducu.nombre=jd['nombre']
            conducu.apellidos=jd['apellidos']
            conducu.telefono=jd['telefono']
            conducu.email=jd['email']
            conducu.direccion=jd['direccion']
            conducu.save()
            datos={'messages':"success"}
        else:
            datos={'messages':"No se encontro registro"}
        return JsonResponse(datos)

    def delete(self, request,pk):
        conductores=list(Conductor.objects.filter(pk=pk).values())
        if len(conductores)>0:
            Conductor.objects.filter(pk=pk).delete()
            datos={'messages':"success"}
        else:
            datos={'messages':"No se encontro registro"}
        return JsonResponse(datos)        
