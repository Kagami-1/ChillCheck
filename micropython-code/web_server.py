import network
from time import sleep
import usocket as socket
import ujson

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

import machine

ssid = 'router2.4'
password = '12345678'

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def sendData(message):
    try:    
        addr = socket.getaddrinfo('192.168.0.164', 1880)[0][-1]
        s.sendto(message, addr)
        print('Message sent.')
    except:
        print('Message not sent. Error: {str(e)}')





try:
    ip = connect()
except KeyboardInterrupt:
    machine.reset()


