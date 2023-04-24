# imageClassification/management/commands/load_images.py
from django.core.management.base import BaseCommand
from django.core.files import File
from imageClassification.models import Image
import os

class Command(BaseCommand):
    help = "Charge les images à partir du dossier 'raw' dans le modèle 'Image'"

    def add_arguments(self, parser):
        parser.add_argument('raw_folder_path', type=str, help="Chemin du dossier contenant les images à trier")

    def handle(self, *args, **options):
        raw_folder_path = options['raw_folder_path']
        image_filenames = os.listdir(raw_folder_path)

        for image_filename in image_filenames:
            image_path = os.path.join(raw_folder_path, image_filename)

            # Vérifie si le fichier est une image en se basant sur l'extension
            if os.path.isfile(image_path) and image_filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                # Vérifie si l'image a déjà été importée
                if not Image.objects.filter(image__contains=image_filename).exists():
                    with open(image_path, 'rb') as image_file:
                        # Crée une instance du modèle Image pour chaque fichier image
                        image_instance = Image()
                        image_instance.image.save(image_filename, File(image_file), save=False)
                        image_instance.image.name = os.path.join('raw', image_filename)
                        image_instance.save()

        self.stdout.write(self.style.SUCCESS(f"Images chargées avec succès à partir du dossier '{raw_folder_path}'."))
