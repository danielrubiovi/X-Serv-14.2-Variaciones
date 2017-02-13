#!/usr/bin/python3

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket

imagen_bat = 'http://1001camisetas.com/wp-content/uploads/2015/01/batamanta-heman.jpg'

 #Mensaje a devolver en el navegador
def answer ():
    htmlAnswer = "<html><body><body bgcolor='red'>"
    htmlAnswer += "<p><h2>"'     ¡Última tendencia en batamantas!'"</h2></p>"
    htmlAnswer += "<p>" + "<IMG SRC=" + imagen_bat + ">" + "</p>"
    htmlAnswer += "</body></html>"
    return htmlAnswer

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

url_redirec = 'https://gsyc.urjc.es/'

while True:
    print('Waiting for connections')
    (recvSocket, address) = mySocket.accept()
    print('HTTP request received:')
    print(recvSocket.recv(1024))
    htmlAnswer = answer()
    recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                    str(htmlAnswer) +
                    "\r\n", 'utf-8'))
    recvSocket.close()
