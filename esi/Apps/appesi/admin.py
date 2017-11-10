from __future__ import unicode_literals
from django.contrib import admin
from .models import Cursomod
from .models import Tipocursomod
from .models import Tipopagomod
from .models import Computadoramod
from .models import Tipocomputadoramod
from .models import Marcamod
from .models import Tipoaccesoriomod
from .models import Accesoriomod

admin.site.register(Cursomod)
admin.site.register(Tipocursomod)
admin.site.register(Tipopagomod)
admin.site.register(Computadoramod)
admin.site.register(Tipocomputadoramod)
admin.site.register(Marcamod)
admin.site.register(Tipoaccesoriomod)
admin.site.register(Accesoriomod)


