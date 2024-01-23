import os
from datetime import datetime

class PhotoFinder:
    def __init__(self, directory, date_str):
        self.directory = directory
        self.date = datetime.strptime(date_str, "%Y-%m-%d").date()

    def find_photos(self):
        photos = []
        for root, _, files in os.walk(self.directory):
            for file in files:
                file_path = os.path.join(root, file)
                creation_date = datetime.fromtimestamp(os.path.getctime(file_path)).date()
                if creation_date == self.date:
                    photos.append(file_path)
        return photos