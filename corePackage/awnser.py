##!/usr/bin/env python3
# dev By Rouxhero
# Core class for bot
# value



line = 0
good = 1
warning = 2
error = 3

#class

class Awnser :

	def __init__(self,statu=line,data="None",msg="Empty"):
		self.statu = statu
		self.data = data
		self.msg = msg

	def code(self):
		return str(self.statu)+";"+self.data+";"+self.msg

	@staticmethod
	def uncode(data):
		data = data.decode()
		data = data.split(';')
		if len(data) != 3:
			emptyAwnser = Awnser(error,'incorecte data !')
		else :
			emptyAwnser = Awnser(data[0],data[1],data[2])
		return emptyAwnser