from datetime import datetime, timezone, timedelta
import time
import dht11
import RPi.GPIO as GPIO
import json
from sinetstream import MessageWriter
import argparse
import sys

#GPIO 14 as DHT11 data pin
Temp_sensor=14

#get sensor values
def get_temp():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    instance = dht11.DHT11(pin=Temp_sensor)

    while True:
        result = instance.read()
        return result.temperature,result.humidity

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="SINETStream Producer")
    parser.add_argument(
        "-s", "--service", metavar="SERVICE_NAME", required=True)
    args = parser.parse_args()

    try:
        print("Press ctrl-c to exit the program.", file=sys.stderr)
        print(f": service={args.service}", file=sys.stderr)
        #producer(args.service)
        with MessageWriter(args.service) as writer:
            while True:
                time_now = datetime.now()
                temperature,humidity = get_temp()
                if temperature == 0:
                    continue
                data = {
                        'time':datetime.now().isoformat(),
                        'temperature': sensor.temperature,
                        'humidity': sensor.humidity,
                        }
                writer.publish(json.dump(data))
                time.sleep(2)
    except KeyboardInterrupt:
        pass
