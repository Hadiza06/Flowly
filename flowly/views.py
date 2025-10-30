#Le fichier views gère toutes les reqêtes html
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from flowly.models import Message

# Create your views here.
#request est la requête http que la fonction views doit gérer

def index(request):
    if request.method == "POST":
        content = request.POST.get('content')
        user=request.user

        Message.objects.create(message=content,user=user)

    context = {}
#ORM Object-Relational mapper
    context['messages'] = Message.objects.order_by('-created_at')
#recupérer tous les objets de la table message
    return render(request, 'index.html',context=context)
#template_name est le fichier html qu'on va servir à l'utilisateur quand on passe dans cette fonction views

