from datetime import datetime, timezone, timedelta
import time
import dht11
import RPi.GPIO as GPIO

#GPIO 14 as DHT11 data pin
Temp_sensor=14
#data create
path_w = './dht11_20191219.csv'

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

    #temperature, humidity = 0, 1
    #temperature, humidity = get_temp()
    with open(path_w, mode='w') as f:
        for i in range(50):
            #time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            #JST = timezone(timedelta(hours=+9), 'JST')
            #loc = datetime.fromtimestamp(now, JST)
            time_now = datetime.now().strftime('%M:%S')
            temperature,humidity = get_temp()
            if temperature == 0:
                continue
            print(time_now)
            print("Temperature = ",temperature,"C"," Humidity = ",humidity,"%")
        #sleep 2s for update data values
            f.write(str(time_now)+str(',')+str(temperature)+','+str(humidity)+'\n')
            time.sleep(1)
