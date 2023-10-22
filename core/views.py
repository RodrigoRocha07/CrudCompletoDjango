from django.shortcuts import render, redirect
from django.core import serializers
from .models import Pessoa

def home(request):
    pessoas = Pessoa.objects.all()
    cursos = Pessoa.objects.values_list('curso', flat=True).distinct()
    periodos = Pessoa.objects.values_list('periodo', flat=True).distinct()
    return render(request, "index.html", {"pessoas":pessoas,"cursos":cursos, "periodos":periodos})

def tabela(request):
    pessoas = Pessoa.objects.all()
    cursos = Pessoa.objects.values_list('curso', flat=True).distinct()
    periodos = Pessoa.objects.values_list('periodo', flat=True).distinct()
    return render(request, "tabela.html", {"pessoas":pessoas,"cursos":cursos, "periodos":periodos})


def salvar (request):
    nome = request.POST.get("nome")
    idade = request.POST.get("idade")
    matricula = request.POST.get("matricula")
    curso = request.POST.get("curso")
    periodo = request.POST.get("periodo")
    Pessoa.objects.create(nome=nome, idade=idade, matricula=matricula, curso=curso,periodo=periodo)
    pessoas = Pessoa.objects.all()
    return redirect(home)

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render (request, "update.html", {"pessoa":pessoa})

def update(request, id):
    nome = request.POST.get("nome")
    idade = request.POST.get("idade")
    matricula = request.POST.get("matricula")
    curso = request.POST.get("curso")
    periodo = request.POST.get("periodo")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = nome
    pessoa.idade = idade
    pessoa.matricula = matricula
    pessoa.curso = curso
    pessoa.periodo = periodo
    pessoa.save()
    return redirect(tabela)

def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(tabela)


def filtrar_curso(request):
    filtrados = []
    pessoas = Pessoa.objects.all()
    cursos = Pessoa.objects.values_list('curso', flat=True).distinct()
    curso = request.POST.get("curso")
    for pessoa in pessoas:
        if pessoa.curso == curso:
            filtrados.append(pessoa)
    return render(request, 'tabela.html',{"pessoas":pessoas, "filtrados":filtrados, "cursos":cursos})

def filtrar_periodo(request):
    filtrados = []
    pessoas = Pessoa.objects.all()
    periodos = Pessoa.objects.values_list('periodo', flat=True).distinct()
    periodo = request.POST.get("periodo")
    for pessoa in pessoas:
        if pessoa.periodo == periodo:
            filtrados.append(pessoa)
    return render(request, 'tabela.html',{"pessoas":pessoas, "filtrados":filtrados,"periodos":periodos})
