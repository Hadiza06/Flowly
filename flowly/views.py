from django.shortcuts import render
from datetime import datetime

# Create your views here.
#request est la requête http que la fonction views doit gérer
def index(request):
    context = {
        "messages":[
            {
                "content": "text",
                "username": "CommentCoder",
                "created_at": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            },
    {
                "content": "text",
                "username": "CommentCoder",
                "created_at": datetime.now()
            },
    {
                "content": "text",
                "username": "CommentCoder",
                "created_at": datetime.now()
            }

        ]

    }

    return render(request, 'index.html',context=context)
#template_name est le fichier html qu'on va servir à l'utilisateur quand on passe dans cette fonction views