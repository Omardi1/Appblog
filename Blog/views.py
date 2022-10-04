from email import message
from importlib.abc import Loader
from multiprocessing import context
from os import name
from pipes import Template
from re import template
from turtle import title
from unittest import loader
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article

def home(request):
    details = "Bonjour les xaralistes !"
    context = {'details':details}
    return render(request, "page/index.html", context)

def about(request):
    return render(request, "page/about.html")

def article_list(request):
    Articles = Article.objects.all()
    return render(request, "Articles/article_list.html", {"Articles":Articles})

def article_details(request, id):
    article = get_object_or_404(Article, id=id)
    
    return render(request, "Articles/article_details.html", {"article":article})

#@login_required(login_url="/login/")
def new_article(request):
    if request.method == "POST":
        title = request.POST['title']
        name = request.POST['name']
        picture = request.POST['picture']
        article = Article.objects.create(
            title=title,
            name=name,
            picture=picture
        
        )
        article.save()
        return  redirect("/Article")
    return render(request, "Articles/new_article.html")
def edit_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        title = request.POST['title']
        name = request.POST['name']
        picture = request.POST['picture']
        article_to_update = Article.objects.filter(pk=article.id)
        article_to_update.update(
            title=title,
            name=name,
            picture=picture
        
        )
        return redirect("/Article")
    return render(request, "Articles/edit_article.html", {"article": article})
    