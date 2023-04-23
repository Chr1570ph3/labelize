# imageClassification/load_images.py
import os
from django.core.files import File
from .models import Image

def load_images_from_raw_folder(raw_folder_path):
    image_filenames = os.listdir(raw_folder_path)

    for image_filename in image_filenames:
        image_path = os.path.join(raw_folder_path, image_filename)

        # Vérifie si le fichier est une image en se basant sur l'extension
        if os.path.isfile(image_path) and image_filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            with open(image_path, 'rb') as image_file:
                # Crée une instance du modèle Image pour chaque fichier image
                image_instance = Image()
                image_instance.image.save(image_filename, File(image_file), save=True)
