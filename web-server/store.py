import requests 

def get_categories():
  # hacemos la peticion http 
  r = requests.get('https://api.escuelajs.co/api/v1/categories')
  # pasamos los datos a un json 
  categorias = r.json()
  # iteramos sobre los elementos 
  for items in categorias:
    print(items['name'])
   