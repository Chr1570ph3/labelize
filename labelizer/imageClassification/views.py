from django.shortcuts import render, redirect
from imageClassification.models import Classe, Image
import os
import shutil
from random import randint
import glob
from django.core.files import File

def get_random_unprocessed_image():
    unprocessed_images = Image.objects.filter(is_processed=False)  # Filtrer les images non traitées
    if not unprocessed_images.exists():
        return None

    random_index = randint(0, unprocessed_images.count() - 1)
    return unprocessed_images[random_index]

def load_classes_from_directory(directory):
    image_paths = glob.glob(os.path.join(directory, '*.jpg'))

    for image_path in image_paths:
        class_name = os.path.splitext(os.path.basename(image_path))[0]
        print(class_name)
        # Vérifie si la classe existe déjà
        class_obj, created = Classe.objects.get_or_create(nom=class_name)
        
        if created:
            # Si la classe n'existe pas, ajoutez l'image et enregistrez-la
            with open(image_path, 'rb') as f:
                class_obj.image_representative.save(f'{class_name}.jpg', File(f), save=True)
        else:
            # Si la classe existe déjà, vérifiez si l'image a changé et mettez à jour si nécessaire
            with open(image_path, 'rb') as f:
                new_image_data = f.read()
                with open(class_obj.image_representative.path, 'rb') as current_image_f:
                    current_image_data = current_image_f.read()
                if new_image_data != current_image_data:
                    class_obj.image_representative.save(f'{class_name}.jpg', File(f), save=True)


def home(request):
    if request.method == 'POST':
        classe_id = request.POST.get('classe')
        image_id = request.POST.get('image_id')
        image = Image.objects.get(id=image_id)
        image.classe = Classe.objects.get(id=classe_id)
        image.is_processed = True  # Marquez l'image comme traitée
        image.save()

        # Déplacer l'image vers le dossier de la classe dans "image_triees"
        os.makedirs(os.path.join('media', 'image_triees', image.classe.nom), exist_ok=True)
        shutil.move(image.image.path, os.path.join('media', 'image_triees', image.classe.nom, os.path.basename(image.image.path)))

        return redirect('home')

    classes = Classe.objects.all()
    image = Image.objects.filter(classe__isnull=True).first()

    context = {
        'classes': classes,
        'image': image,
    }

    return render(request, 'imageClassification/home.html', context)

# load_classes_from_directory('labelizer/labelizer/media/classes_representatives/')
load_classes_from_directory('C:/Users/chris/Projets/Labelizer/labelizer/labelizer/media/classes_representatives')
