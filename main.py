import requests
import urllib3
import json
import conf

urllib3.disable_warnings()
url = "https://192.168.100.60"


r = requests.get(url+"/rest/ip/address/*2", auth=(conf.user,conf.clave), verify=False)
print(json.dumps(r.json(), indent=4))


r2 = requests.get(url+"/rest/interface/ether1", auth=(conf.user,conf.clave), verify=False)
if r2.json()["mac-address"] == "00:0C:29:B6:9C:47":
    print("El equipo no fue cambiado")
else:
    print("Alguien cambio el equipo")

#############################################################################################

#Evaluacion3
response = requests.get(url)
if (response.status_code == 200):
    print("solicitud exitosa!")

elif (response.status_code == 404):
    print("Soliocitud Fallida!")

#############################################################################################

#eliminar el registro con una ID específica

r3 = requests.delete(url+"/rest/ip/address/*2", auth=(conf.user,conf.clave), verify=False)
print(json.dumps(r3.json(), indent=4))