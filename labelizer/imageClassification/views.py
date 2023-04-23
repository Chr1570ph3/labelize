from django.shortcuts import render, redirect
from imageClassification.models import Classe, Image
from imageClassification.forms import ImageForm
import os
import shutil

def home(request):
    if request.method == 'POST':
        classe_id = request.POST.get('classe')
        image_id = request.POST.get('image_id')
        image = Image.objects.get(id=image_id)
        image.classe = Classe.objects.get(id=classe_id)
        image.save()

        # Déplacer l'image vers le dossier de la classe dans "image_triees"
        os.makedirs(os.path.join('media', 'image_triees', image.classe.nom), exist_ok=True)
        shutil.move(image.image.path, os.path.join('media', 'image_triees', image.classe.nom, os.path.basename(image.image.path)))

        return redirect('home')

    form = ImageForm()
    classes = Classe.objects.all()
    image = Image.objects.filter(classe__isnull=True).first()
    
    context = {
        'form': form,
        'classes': classes,
        'image': image,
    }

    return render(request, 'imageClassification/home.html', context)
