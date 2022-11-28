from django.shortcuts import render
from .models import Aluno
from django.views.generic import ListView, CreateView
from .forms import alunoForm
from usuario.forms import usuarioForm
from django.contrib import messages
from django.shortcuts import render, redirect

class listagemAlunoView(ListView):
    model = Aluno
    queryset = Aluno.objects.all().order_by('nome_aluno')

class alunoCreateView(CreateView):
    model = Aluno
    form_class = alunoForm
    success_url = '/alunos/'
    success_message = "Cadastrado com sucesso"

    def get_success_message(self, cleaned_data):
        return self.success_message

'''def register(request):
    if request.method=="POST":
        form = usuarioSysForm(request.POST)
        
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        
        if len(password1)<8:
            messages.error(request, 'A senha deve ter 8 caracteres')
        if password1 != password2:  
            messages.error(request,"As senhas são diferentes")  
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Login Registrado com Sucesso')
            return redirect('home') 
        messages.error(request, 'Falha no registro')
    form = usuarioSysForm()
    context = {'form': form}
    return render(request, template_name='usuario/register.html', context=context)'''

def verificarAluno(request):
    if request.method=="POST":
        form = alunoForm(request.POST)
        form2 = usuarioForm(request.POST)

        cpf_aluno = request.POST['cpf_aluno']
        cpf = request.POST['cpf']

        if cpf_aluno not in cpf:
            messages.error(request, 'Esse cpf não pertence a este aluno')

        if form.is_valid():
            alunos = form.save()
            messages.success(request, 'Aluno Cadastrado')
            return redirect('home')
        messages.error(request, 'Falha no cadastro')
    form = alunoForm()
    context = {'form': form}
    return render(request, template_name='alunos/aluno_form.html', context=context)


