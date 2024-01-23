import os

class FileUtils:
    @staticmethod
    def delete_file(file_path):
        os.remove(file_path)