import machine
import dht
import ujson
from time import sleep
from web_server import connect, sendData

sensor = dht.DHT11(machine.Pin(28))
temperatures = []
humidities = []

# Connect to WLAN
connect()

while True:
    try:
        sensor.measure()
        sleep(0.5)
        temp = sensor.temperature()
        humidity = sensor.humidity()

        # Store up to the last 100 sensor readings
        if len(temperatures) >= 100:
            temperatures.pop(0)  # remove oldest temperature
        if len(humidities) >= 100:
            humidities.pop(0)  # remove oldest humidity

        temperatures.append(temp)
        humidities.append(humidity)
        
        avgTemp = sum(temperatures) / len(temperatures)
        avgHumidity = sum(humidities) / len(humidities)

        # Check if the temperature has changed by 5 degrees or more
        if abs(avgTemp - temp) >= 5:
            door_status = "Door Open!"
        else:
            door_status = "Door Fine"

        # Send data and door status as a JSON string
        sendData(temp, humidity, avgTemp, avgHumidity, door_status)

    except OSError as e:
        print('Failed to read sensor.')


