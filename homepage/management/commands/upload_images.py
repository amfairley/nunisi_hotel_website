import os
from django.conf import settings
import cloudinary.uploader
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Upload existing media files to Cloudinary"

    def handle(self, *args, **kwargs):
        media_directory = settings.MEDIA_ROOT
        # List all files in your media folder
        for root, dirs, files in os.walk(media_directory):
            for file in files:
                file_path = os.path.join(root, file)
                if file.endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
                    # Upload to Cloudinary
                    result = cloudinary.uploader.upload(file_path)
                    print(f"Uploaded {file} to Cloudinary. URL: {result['url']}")
