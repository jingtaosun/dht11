import requests

url = "https://maker.ifttt.com/trigger/dht11/with/key/InQQGS7DO_SLTzuDs4iF7"

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = '{"value1":"12","value2":"23","value3":"34"}')

print(response.text.encode('utf8'))
