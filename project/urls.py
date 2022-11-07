from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include


from main import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('usuarios/', include('usuario.urls')),
    path('professores/', include('professor.urls')),
    path('disciplinas/', include('disciplina.urls')),
    path('alunos/', include('aluno.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, 
                        document_root=settings.MEDIA_ROOT)
    
