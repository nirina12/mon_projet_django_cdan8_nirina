from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import PersonneForm, VoitureForm
from .models import Personne

def home(request):
    context = {
        "typeActionPost":"Ajouter",
        "title":"home",
        "form" :PersonneForm(),
        "personnes" : Personne.objects.all()

    }
    return render(request,"personnes.html",context)

def actionPost(request):
    if request.method == "POST":
        type_action_post = request.POST.get('typeActionPost')
        idUser = request.POST.get('idUser')
        data = PersonneForm(request.POST)
        
        if data.is_valid():
            nom_form = data.cleaned_data["nom"]
            prenom_form = data.cleaned_data["prenom"]
            age_form = data.cleaned_data["age"]
            genre_form = data.cleaned_data["genre"]
            if idUser == "":
                print("Ajouter")
                Personne.objects.create(nom=nom_form,prenom=prenom_form,age=age_form, genre=genre_form)
            else:
                personne = Personne.objects.get(id=int(idUser))
                personne.nom = nom_form
                personne.prenom = prenom_form
                personne.age = age_form
                personne.genre = genre_form

                personne.save()
                print(f"Modifier {idUser}, {nom_form},{personne.nom}")

                
    return redirect("homePage")

def voitures(request):
    context = {
        "title": "voitures",
        "form":VoitureForm()
    }
    return render(request,"voitures.html",context)




def personnes_ajout(request):
    p = Personne.objects.create(nom="Mae",prenom="Christophe",age=55,genre="Homme")
    p.save()
    return HttpResponse(p)

def personnes(request):
    if request.method == "POST":
        data = PersonneForm(request.POST)
        if data.is_valid():
            nom_form = data.cleaned_data["nom"]
            prenom_form = data.cleaned_data["prenom"]
            age_form = data.cleaned_data["age"]
            genre_form = data.cleaned_data["genre"]
            Personne.objects.create(nom=nom_form,prenom=prenom_form,age=age_form, genre=genre_form)
            
            return redirect("page_utilisateur")
        return HttpResponse("Ajout échoué")
    context = {
        "title":"personnes",
        "form" :PersonneForm(),
        "personnes" : Personne.objects.all()
    }
    return render(request,"personnes.html",context)
                             
def supprimer_personne(request, id_personne):
    personne = Personne.objects.get(id=id_personne)
    personne.delete()
    return redirect("homePage")

def modifier_personne(request, id_personne):
    current_personne = Personne.objects.get(id=id_personne)
    
    context = {
        "idUser":id_personne,
        "typeActionPost":"Modifier",
        "title":"home",
        "form" :PersonneForm(initial={"nom":current_personne.nom,"prenom":current_personne.prenom,"age":current_personne.age,"genre":current_personne.genre}),
        "personnes" : Personne.objects.all()

    }
    return render(request,"personnes.html",context)