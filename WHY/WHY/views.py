from django.http import HttpResponse

def bienvenida(request):
  return HttpResponse ("Bienvenid@ a la página web")