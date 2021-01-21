from os import listdir
from os.path import isfile, join

class Java():

    def __init__(self):
        # Metodo vacio
        pass

    def get_filenames(self):
        filenames = [self.change_name(file) for file in listdir('Docs/learning') if isfile(join('Docs/learning', file))]
        return filenames

    def get_file(self, filename):
        try:  
            file = open(f"Docs/learning/{filename.text}.md", "r", encoding="utf8")
            textfile = file.read()
            file.close()
            return textfile

        except FileNotFoundError as error:
            texterror = "El archivo especificado no existe\n FileNotFoundError: {0}"
            print(texterror.format(error))
            return f"Aun no existe el tema especificado {filename.text}"
    
    def change_name(self, filename):
        filename_withoutext = filename.split(".")
        return filename_withoutext[0]