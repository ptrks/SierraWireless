"""
  This is a template for recieving GPS data in TAIP format with UDP sockets.
  I have used this code on Sierra Wireless GX400,GX440 and LS300 devices


  2013 Patrick Servello

"""


import SocketServer
import time
import taip

class MyUDPHandler(SocketServer.BaseRequestHandler):
  def handle(self):
          time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
          data = self.request[0].strip()
          remoteIP = self.client_address[0]
          try:
           taipData = taip.Taipy(data)
           longitude = taipData.longitude
           latitude = taipData.latitude

           # do something with data here


          except ValueError:
            latitude = 0
            longitude = 0

if __name__ == "__main__":

    HOST, PORT = "", 22335
    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print "shutting down server"
        server.shutdown()