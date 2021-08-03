##!/usr/bin/env python3
# dev By Rouxhero
# Core class for bot
# Import 
from corePackage.dataSet import dataSet
from corePackage.awnser import *
from colorama import Fore,Style
# class


class Core :

	def __init__(self):
		self.dataSet = dataSet
		self.component = {}

	def get(self,arg):
		data = Awnser()
		if arg in self.dataSet:
			data.status = True
			data.data = self.dataSet[arg]["value"]
		else:
			data.status = False
			data.msg = 'Arguments doe\'st existe !'
		return data
		

	def config(self,output,sender):
		sender.sendall(Awnser(good,"Starting bot configuration").code().encode())
		for data in self.dataSet:
			if self.dataSet[data]["user"] == self.dataSet["defaultUser"]["value"] or self.dataSet["defaultUser"]["value"] == 'root':
				print('Editing {} option :\nenter new value or let empty for no change\nValue is now : {}'.format(data,self.dataSet[data]["value"]))
				ok = True
				while ok:
					newValue = input('PyBot-Config >>>')
					if newValue != "":
						if type(newValue) == self.dataSet[data]["type"]:
							self.dataSet[data]["value"] = newValue
							ok = False
						else :
							print('Error incorecte value, need : {}'.format(self.dataSet[data]["type"]))
	def upgrade(self,output):
		output.print("Warning root user give access to all option, it's can break the bot !",Fore.RED)
		self.dataSet['defaultUser']['value'] = "root"
		print(Style.RESET_ALL)

	def addComponent(self,component):
		self.component[len(self.component)+1] = [component.getName(),component]
		component.start()


