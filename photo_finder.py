import os
from datetime import datetime, timezone

class PhotoFinder:
    def __init__(self, directory, date_str):
        self.directory = directory
        self.date = datetime.strptime(date_str, "%Y-%m-%d").date()

    def find_photos(self):
        photos = []
        for root, _, files in os.walk(self.directory):
            for file in files:
                file_path = os.path.join(root, file)
                creation_timestamp = os.path.getctime(file_path)
                creation_local_date = datetime.fromtimestamp(creation_timestamp, timezone.utc).astimezone()
                creation_date = creation_local_date.date()
                if creation_date == self.date:
                    print(f'{file_path} created on {creation_timestamp}')
                    print(f'{file_path} created on {creation_local_date}')
                    print(f'{file_path} created on {creation_date}')
                    print(f'{file_path} created on {creation_date} == {self.date}')
                if creation_date == self.date:
                    photos.append(file_path)
        return photos