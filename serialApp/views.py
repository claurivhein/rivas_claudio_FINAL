from django.shortcuts import render, redirect
from .models import Inscritos, Institucion, DatosAutor
from .forms import FormInscritos, FormInstitucion
from .serialiazers import InscritosSerializer, InstitucionSerializer, DatosAutorSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import Http404

# Vistas pára el crud de Inscritros

def index(request):
    return render(request, 'index.html')

def listarinscritos(request):
    pro = Inscritos.objects.all()
    data = {'inscritos': pro}
    return render(request, 'crudinscritos.html', data)

def agregarinscripcion(request):
    form = FormInscritos()
    if request.method == 'POST':
        form = FormInscritos(request.POST)
        if form.is_valid():
            form.save()
        return redirect('crudinscritos')
    data = {'form' : form}
    return render(request, 'agregarinscripcion.html', data)

def eliminarinscripcion(request, id):
    pro = Inscritos.objects.get(id = id)
    pro.delete()
    return redirect('crudinscritos')

def actualizarinscripcion(request, id):
    pro = Inscritos.objects.get(id = id)
    form = FormInscritos(instance=pro)
    if request.method == 'POST':
        form = FormInscritos(request.POST, instance=pro)
        if form.is_valid():
            form.save()
        return redirect('crudinscritos')
    data = {'form': form}
    return render(request, 'agregarinscripcion.html', data)

# Vistas para crud Instituciones

def listarinstituciones(request):
    pro = Institucion.objects.all()
    data = {'instituciones': pro}
    return render(request, 'crudinstitucion.html', data)

def agregarinstitucion(request):
    form = FormInstitucion()
    if request.method == 'POST':
        form = FormInstitucion(request.POST)
        if form.is_valid():
            form.save()
        return redirect('crudinstitucion')
    data = {'form' : form}
    return render(request, 'agregarinstitucion.html', data)

def eliminarinstitucion(request, id):
    pro = Institucion.objects.get(id = id)
    pro.delete()
    return redirect('crudinstitucion')

def actualizarinstitucion(request, id):
    pro = Institucion.objects.get(id = id)
    form = FormInstitucion(instance=pro)
    if request.method == 'POST':
        form = FormInstitucion(request.POST, instance=pro)
        if form.is_valid():
            form.save()
        return redirect('crudinstitucion')
    data = {'form': form}
    return render(request, 'agregarinstitucion.html', data)

# Class Based Views para Inscritos

class ListarInscripciones(APIView):

    def get(self, request):
        estu = Inscritos.objects.all()
        serial = InscritosSerializer(estu, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = InscritosSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class InscritosDetalle(APIView):
    
    def get_object(self, pk):
        try:
            return Inscritos.objects.get(pk=pk)
        except Inscritos.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        estu = self.get_object(pk)
        serial = InscritosSerializer(estu)
        return Response(serial.data)

    def put(self, request, pk):
        estu = self.get_object(pk)
        serial = InscritosSerializer(estu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        estu = self.get_object(pk)
        estu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Function Based Views para Instituciones

@api_view(['GET', 'POST'])
def institucion_list(request):
    if request.method == 'GET':
        estu = Institucion.objects.all()
        serial = InstitucionSerializer(estu, many=True)
        return Response(serial.data)
    
    if request.method == 'POST':
        serial = InstitucionSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def institucion_detalle(request, pk):
    try:
        estu = Institucion.objects.get(id = pk)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionSerializer(estu)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = InstitucionSerializer(estu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        estu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Class Based Views para Datos del autor

class ListarAutor(APIView):

    def get(self, request):
        estu = DatosAutor.objects.all()
        serial = DatosAutorSerializer(estu, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = DatosAutorSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class AutorDetalle(APIView):
    
    def get_object(self, pk):
        try:
            return DatosAutor.objects.get(pk=pk)
        except DatosAutor.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        estu = self.get_object(pk)
        serial = DatosAutorSerializer(estu)
        return Response(serial.data)

    def put(self, request, pk):
        estu = self.get_object(pk)
        serial = DatosAutorSerializer(estu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        estu = self.get_object(pk)
        estu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)