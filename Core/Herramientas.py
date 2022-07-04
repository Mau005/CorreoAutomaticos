import os
import pandas as pd

class Herramientas:

    @staticmethod
    def CargarExcel(path,hoja):
        if os.path.exists(path):
            archivo = pd.read_excel(path, sheet_name = hoja)
            print(len(archivo.head(50)))
        else:
            print("No existe la ruta")

    @staticmethod
    def InfoCorreo(nombre, evaluacion, ramo, puntos, nota):
        correo = """
Estimado {0}
En la evaluación {1} de nuestro ramo {2} ha obtenido un total de {3} y su       
nota corresponde a un {4}.  A continuación se detalla el resultado por cada pregunta de
la evaluación:
        """
