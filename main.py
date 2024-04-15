from bottle import route, run, request
import requests
import re

@route('/')
def index():
    ip_address = request.environ.get('REMOTE_ADDR')
    url = f"https://freeipapi.com/api/json/{ip_address}"

    response = requests.get(url)
    data = response.json()

    ip_info = (
      f"Your IP address: {data['ipAddress']}\n"
      f"Your country: {data['countryName']}\n"
      f"Your region: {data['regionName']}\n"
      f"Your city: {data['cityName']}\n"
      f"Your latitude: {data['latitude']}\n"
      f"Your longitude: {data['longitude']}\n"
      f"Your zip code: {data['zipCode']}\n"
      f"Your time zone: {data['timeZone']}\n"
      f"Your continent: {data['continent']}\n"
      f"Are you using a proxy: {data['isProxy']}"
    )
    print(ip_info)
    return re.sub("\n","<br>",ip_info)
  
run(port=8080)
