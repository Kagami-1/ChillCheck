import machine
import dht
from web_server import connect
from web_server import sendData


sensor = dht.DHT11(machine.Pin(28))


if __name__=="__main__":
    print(connect())
    connect()
    
while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        humidity = sensor.humidity()
        sendData(str(temp))
        print('Temperature: %3.2f C' %temp)
        print('Humidity: %3.2f %%' %humidity)
    except OSError as e:
        print('Failed to read sensor.')
