from django import forms
#importando modelos
from .models import Cursomod
from .models import Tipocursomod
from .models import Tipopagomod
from .models import Computadoramod
from .models import Tipocomputadoramod
from .models import Marcamod
from .models import Tipoaccesoriomod
from .models import Accesoriomod

class CursoForm(forms.ModelForm):
	class Meta:
		model = Cursomod
		fields = '__all__'

class TipoCursoForm(forms.ModelForm):
	class Meta:
		model = Tipocursomod
		fields = '__all__'

class TipoPagoForm(forms.ModelForm):
	class Meta:
		model = Tipopagomod
		fields = '__all__'

class ComputadoraForm(forms.ModelForm):
	class Meta:
		model = Computadoramod
		fields = '__all__'

class TipoComputadoraForm(forms.ModelForm):
	class Meta:
		model = Tipocomputadoramod
		fields = '__all__'

class MarcaForm(forms.ModelForm):
	class Meta:
		model = Marcamod
		fields = '__all__'

class TipoAccesorioForm(forms.ModelForm):
	class Meta:
		model = Tipoaccesoriomod
		fields = '__all__'



		








