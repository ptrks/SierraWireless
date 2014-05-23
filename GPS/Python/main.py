#!/usr/bin/env python

"""
This is an example Python program that will allow you to receive and manipulate 
TAIP based data from Sierra Wireless smart gateways. 

This example makes use of the SocketServer module for simplicity.

"""

import re
import time
import SocketServer


class TaipData:
  def __init__(self,taipString):
    self.reg = '^>(\w)(\w{2})(\d{5})(\+|-)(\d{2})(\d{5})(\+|-)(\d{3})(\d{5})(\d{3})(\d{3})(\d)(\d)(?:;ID=(\w+))?;\*(\w+)<$'
    self.TaipData = re.search(self.reg,taip_string)
    self.type = self.TaipData.group(0)
    self.data = self.TaipData.group(1)
    self.time_of_day = self.TaipData.group(2)
    self.longitude = self.TaipData.group(4) + self.TaipData.group(5) + "." + self.TaipData.group(3)
    self.latitude =  self.TaipData.group(7) + self.TaipData.group(8) + "." + self.TaipData.group(6)
    self.speed = self.TaipData.group(9)
    self.heading = self.TaipData.group(10)
    self.source = self.TaipData.group(11)
    self.age = self.TaipData.group(12)
    self. id = self.TaipData.group(13)
    self.checksum = self.TaipData.group(14)

class MyUDPHandler(SocketServer.BaseRequestHandler):
  def handle(self):
          time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
          data = self.request[0].strip()
          remote_host = self.client_address[0]
          print "remote host: " + remote_host + " data: " + data
          try:
           taip_data = TaipData(data)
           longitude = taip_data.longitude
           latitude = taip_data.latitude

           # do something with data here


          except ValueError:
            latitude = 0
            longitude = 0

if __name__ == "__main__":

    HOST, PORT = "", 22331
    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print "shutting down server"
        server.shutdown()


