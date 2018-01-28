import argparse
import requests
import os

def get_week():
    """
    Función para obtener mediante la linea de comandos la semana a descargar
    """
    parser = argparse.ArgumentParser(
            description = "Descarga las tareas semanales del curso 'Python Para Actuarios' de la Universidad Marista."
            )

    parser.add_argument("-s", "--semana", action="store", required=True, type=int,
                        help="Selecciona la tarea de la semana la cuál quieres descargar. Si el archivo ya existe dentro de tu carpeta, el programa te preguntará si lo deseas volver a descargar, ten en cuenta que al hacer esto se borrará todo el progreso de otra tareas. De igual manera, si la semana aún no existe dentro de la carpeta de tareas, el programa te informará.")

    return parser.parse_args().semana

def homework_exists(filename):
    """
    Función para preguntar al usuario si el archivo ya existente dentro de su carpeta desea se vuelva a descargar.

    Parametros
    ----------
    filename: nombre del archivo a revisar

    Regresa 
    -------
    Bool: True si se eliminará el archivo viejo y False de otra manera
    """
    selection = input("El archivo {filename} ya existe, ¿seguro lo quieres volver a descargar? (y/n) ".format(filename=filename))
    if selection.lower() == "y":
        return True
    elif selection.lower() == "n":
        return False
    else:
        print("Selecciona 'y' o 'n'")
        return homework_exists()

def download_homework(week):
    """
    Función para descargar la tarea de una semana dada. SI el archivo existe y aún no se encuentra dentro de la carpeta del usuario se descagará automaticamente, de otro modo, preguntará al usuario si desea volver a descargar el archivo.

    Parametros
    ----------
    week: int
        La tarea de la semana a descargar
    """
    filename = "week{w:02}.ipynb".format(w=week)
    base_url = "https://raw.githubusercontent.com/gerdm/python_uma/master/exercises/{filename}".format(filename=filename)
    if os.path.exists(filename):
        if not homework_exists(filename):
            print("No se descargó el archivo {filename}".format(filename=filename))
            return None

    webdata = requests.get(base_url)
    if webdata.status_code == 404:
        print("No existe archivo {filename}".format(filename = filename))
        return None

    with open(filename, "w") as hm:
        hm.write(webdata.text)

def main():
    week = get_week()
    download_homework(week)

if __name__ == "__main__":
    main()
