from django.shortcuts import render, redirect
from django.http import HttpResponse

# Vista de login
def login_view(request):
    if request.method == "POST":
        # No se validan las credenciales, solo redirigimos al inicio
        return redirect('inicio')  # Redirigir a la página de inicio después de login
        
    return render(request, 'mi_app/login.html')  # Mostrar el formulario de login

# Vista de inicio
def inicio(request):
    return render(request, 'mi_app/index.html')  # Mostrar la página de inicio

# Vista adicional (acerca de)
def acercade(request):
    context = {
        'titulo': 'Acerca de',
        'mensaje': 'Esta es la página acerca de nosotros.',
    }
    return render(request, 'mi_app/acercade.html', context)

def contacto(request):
    return render(request, 'mi_app/contacto_desactivado.html')


def procesar_formulario(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre", "")
        correo = request.POST.get("correo", "")
        return HttpResponse(f"Formulario recibido. Nombre: {nombre}, Correo: {correo}")
    else:
        return HttpResponse("Método no permitido", status=405)