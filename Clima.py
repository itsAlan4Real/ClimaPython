#Instalar los modulos:
# "bs4" que es una libreria para extraer datos de documentos HTML y XML.
# "win10toast" para crear las notificaciones de escritorio.
# "requests" permite mandar peticiones HTTP/1.1 de manera sencilla.

#importar librerias:
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

#Objeto para la clase ToastNotifier.
n=ToastNotifier()

#definir una funcion
def getdata(url):
    r=requests.get(url)
    return r.text
#Codigo
#Usar la funcion para obtener los datos de la pagina del clima.
#Para la pagina del clima, use buscar simplemente "clima" en google y en la opcion predeterminada que brinda google
#Entrar y copiar el link que mande de tu ciudad.

htmldata=getdata("https://weather.com/es-MX/tiempo/hoy/l/25.50,-103.39?par=google&temp=c")
soup=BeautifulSoup(htmldata,'html.parser')

#obtener registros de temperatura y probabilidad de lluvia, usando codigo fuente de la pagina.
#Usar ctrl+f para buscar las palabras "components-src-organism-etc...." hacerlo para "TempValule y precipValue"
#Cada ciudad es diferente la serie de numeros y letras al final, asi que hacer ese paso con tu ciudad.
temperatura_actual=soup.find_all("span",class_="_-_-components-src-organism.CurrentConditions-CurrentConditions--tempValue--3KcTQ")
probabilidad_lluvia=soup.find_all("span",clas_="_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--RBVJT")
temp=(str(temperatura_actual))
lluvia=(str(probabilidad_lluvia))

#mostrar notificacion
result=" Temperatura actual " + temp[128:-9] + "en Torreón Coahuila" + "\n"+ lluvia[131:-14]
n.show_toast("Actualizacion del Clima en vivo", result, duration=10)