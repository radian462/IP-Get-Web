from bottle import route, run, request
import requests
import re

@route('/')
def index():
    ip_address = request.environ.get('REMOTE_ADDR')
    #url = f"https://freeipapi.com/api/json/{ip_address}"
    url = f"https://api.ipapi.is/?q={ip_address}"

    response = requests.get(url)
    data = response.json()

    def safe_get(dictionary, keys, default='-'):
        for key in keys:
            dictionary = dictionary.get(key, default)
            if dictionary == default:
                break
        return dictionary

    ip_info = (
        f"Your IP address: {safe_get(data, ['ip'])}\n"
        f"Your country: {safe_get(data, ['location', 'country'])}\n"
        f"Your state: {safe_get(data, ['location', 'state'])}\n"
        f"Your city: {safe_get(data, ['location', 'city'])}\n"
        f"Your latitude: {safe_get(data, ['location', 'latitude'])}\n"
        f"Your longitude: {safe_get(data, ['location', 'longitude'])}\n"
        f"Your zip code: {safe_get(data, ['location', 'zip'])}\n"
        f"Your time zone: {safe_get(data, ['location', 'timezone'])}\n"
        f"using vpn: {safe_get(data, ['is_vpn'])}\n"
        f"using proxy: {safe_get(data, ['is_proxy'])}\n"
        f"using tor: {safe_get(data, ['is_tor'])}\n"
        f"using mobile: {safe_get(data, ['is_mobile'])}"
    )
  
    print(ip_info)
    return re.sub("\n","<br>",ip_info)

run(port=8080)