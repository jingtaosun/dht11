from datetime import datetime, timezone, timedelta
import time
import dht11
import RPi.GPIO as GPIO
import requests

#GPIO 14 as DHT11 data pin
Temp_sensor=14
#data create
#path_w = './dht11_20191219.csv'

#get sensor values
def get_temp():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    instance = dht11.DHT11(pin=Temp_sensor)

    while True:
        #read data
        result = instance.read()
        return result.temperature,result.humidity

if __name__ == '__main__':
    url = "https://maker.ifttt.com/trigger/dht11/with/key/InQQGS7DO_SLTzuDs4iF7"
    headers = {
        'Content-Type': 'application/json'
    }
    #temperature, humidity = 0, 1
    #temperature, humidity = get_temp()
    while True:
            #time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            #JST = timezone(timedelta(hours=+9), 'JST')
            #loc = datetime.fromtimestamp(now, JST)
        time_now = datetime.now().strftime('%M:%S')
        temperature,humidity = get_temp()
        if temperature == 0:
            continue
        print(time_now)
        print("Temperature = ",temperature,"C"," Humidity = ",humidity,"%")
        #sleep 2s for update data valuesi
        #payload2='{"value0":str(time_now),"value1":str(temperature),"value2":str(humidity)}'
        #payload='{"value1":"12","value2":"23","value3":"34"}'
        payload = {"value1":str(time_now),"value2":str(temperature),"value3":str(humidity)}
        response = requests.post(url, data = payload)
        #        (str(time_now)+str(',')+str(temperature)+','+str(humidity)+'\n')
        time.sleep(1)
        print(response.text.encode('utf8'))

