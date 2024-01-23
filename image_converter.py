import os
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

class ImageConverter:
    @staticmethod
    def convert_to_jpeg(image_path, output_path):
        file_extension = os.path.splitext(image_path)[1].lower()
        print(f'Trying to convert {image_path} to JPEG...')
        try:
            if file_extension == '.heic':
                with Image.open(image_path) as img:
                    rgb_im = img.convert('RGB')
            else:
                with Image.open(image_path) as img:
                    rgb_im = img.convert('RGB')
            rgb_im.save(output_path, 'JPEG')
            print(f'Successfully converted {image_path} to JPEG.')
            return True
        except (PIL.UnidentifiedImageError, pillow_heif.UnidentifiedImageError):
            print(f'Failed to convert {image_path} to JPEG, skipping.')
            return False