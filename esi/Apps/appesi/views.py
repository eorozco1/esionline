from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView, ListView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
# Create your views here.
# modelos y formularios
from .models import Cursomod
from .forms import  CursoForm
from .models import Tipocursomod
from .forms import  TipoCursoForm
from .models import Tipopagomod
from .forms import  TipoPagoForm
from .models import Computadoramod
from .forms import  ComputadoraForm
from django.contrib.auth.models import User

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class IndexView(TemplateView):
	template_name='index.html'

class IngresarCursoView(CreateView):
	template_name = 'ingresarcurso.html'
	form_class = CursoForm
	success_url = reverse_lazy('appesi:index')

class IngresarTipoCursoView(CreateView):
	template_name = 'ingresartipocurso.html'
	form_class = TipoCursoForm
	success_url = reverse_lazy('appesi:index')

class IngresarTipoPagoView(CreateView):
	template_name = 'ingresartipopago.html'
	form_class = TipoPagoForm
	success_url = reverse_lazy('appesi:index')

class LoginView(FormView):
	template_name='login.html'
	form_class = AuthenticationForm
	success_url = reverse_lazy('appesi:IngCurso')

	def form_valid (self, form):
		login(self.request, form.get_user())
		return super (LoginView, self) .form_valid (form)

def logoutview(request):
	logout(request)
	return redirect ('appesi:index')

class CrearUsuarioView(CreateView):
	model=User
	template_name = "CrearUsuario.html"
	form_class = UserCreationForm
	success_url = reverse_lazy('appesi:Login')

class ContactoView(TemplateView):
	template_name='contacto.html'

class QuienView(TemplateView):
	template_name='quien.html'

class IngresarComputadoraView(CreateView):
	template_name = 'ingresarcomputadora.html'
	form_class = ComputadoraForm
	success_url = reverse_lazy('appesi:index')

class ListaCursoView(ListView):
	template_name = 'listarcursos.html'
	model = Cursomod

	def get_queryset(self):
		return Cursomod.objects.all()
