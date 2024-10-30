import requests

# URL con parámetros de consulta para obtener eventos de terremotos en formato JSON
url = 'https://earthquake.usgs.gov/fdsnws/event/1/query'

# Parámetros para la solicitud
params = {
    'format': 'geojson',  # Especifica que la respuesta esté en formato JSON
    'starttime': '2023-01-01',  # Fecha de inicio
    'endtime': '2023-12-31',    # Fecha de fin
    'minmagnitude': 5           # Magnitud mínima del terremoto
}

# Hacer la solicitud GET con parámetros
response = requests.get(url, params=params)

# Verificar el estado de la respuesta
if response.status_code == 200:
    data = response.json()  # Convertir respuesta en JSON
    # Iterar sobre los eventos y mostrar títulos
    for event in data['features']:
        print(event['properties']['title'])
else:
    print("Error:", response.status_code)