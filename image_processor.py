import os
import shutil
from image_converter import ImageConverter
from file_utils import FileUtils
import time

class ImageProcessor:
    SUPPORTED_FORMATS = {'.png', '.jpeg', '.jpg', '.webp', '.gif'}
    CONVERT_FORMAT = '.heic'

    def __init__(self, target_folder, date_str):
        self.target_folder = os.path.join(target_folder, date_str)
        os.makedirs(self.target_folder, exist_ok=True)

    def process_images(self, photos, openai_client):
        for photo in photos:
            _, ext = os.path.splitext(photo)
            if ext.lower() in self.SUPPORTED_FORMATS:
                target_path = os.path.join(self.target_folder, os.path.basename(photo))
                shutil.copy(photo, target_path)
                file_is_available = True
            elif ext.lower() == self.CONVERT_FORMAT:
                target_path = os.path.join(self.target_folder, os.path.basename(photo).replace(ext, '.jpeg'))
                file_is_available = ImageConverter.convert_to_jpeg(photo, target_path)
            else:
                file_is_available = False

            if file_is_available and not openai_client.is_food_image(target_path):
                FileUtils.delete_file(target_path)
            elif file_is_available:
                # Set the same creation time on target_path as the original photo file
                original_stat = os.stat(photo)
                os.utime(target_path, (original_stat.st_atime, original_stat.st_mtime))
