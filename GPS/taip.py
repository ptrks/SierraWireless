""" Python regular expression based TAIP data parser """ 
import re
class Taipy:
  def __init__(self,taipString):
    self.reg = '^>(\w)(\w{2})(\d{5})(\+|-)(\d{2})(\d{5})(\+|-)(\d{3})(\d{5})(\d{3})(\d{3})(\d)(\d)(?:;ID=(\w+))?;\*(\w+)<$'
    self.taipData = re.search(self.reg,taipString)
    self.type = self.taipData.group(0)
    self.data = self.taipData.group(1)
    self.timeOfDay = self.taipData.group(2)
    self.longitude = self.taipData.group(4) + self.taipData.group(5) + "." + self.taipData.group(3)
    self.latitude =  self.taipData.group(7) + self.taipData.group(8) + "." + self.taipData.group(6)
    self.speed = self.taipData.group(9)
    self.heading = self.taipData.group(10)
    self.source = self.taipData.group(11)
    self.age = self.taipData.group(12)
    self. id = self.taipData.group(13)
    self.checksum = self.taipData.group(14)