# main class of console object
import os
from time import sleep as pause
from Console.consoleObject import *
try :
	import colorama
except ImportError :
	os.system('pip3 install colorama')
from colorama import init, Fore,Style

RED = Fore.RED
GREEN = Fore.GREEN
WHITE = Fore.WHITE
YELLOW = Fore.YELLOW


code = {'0':WHITE,'1':GREEN,'2':YELLOW,'3':RED}



def clean():
	if os.name == "posix":
		os.system('clear')
	else:
		os.system('cls')



class Console :

	def __init__(self):
		init()
		self.history = []

	def clear(self):
		self.history = []

	def print(self,text,color=WHITE):
		print(color+text)
		self.addLine(text,color)

	def println(self,text,color=WHITE):
		print(color+text,end='')
		self.addLine(text,color,True)

	def addLine(self,text,color=WHITE,noEnd=False):
		self.history.append(Line(text,color,noEnd))

	def addProgessBar(self,progessBar):
		self.history.append(progessBar)

	def showText(self):
		clean()
		for line in self.history:
			if not line.end :
				print(line.show()+Style.RESET_ALL)
			else :
				print(line.show()+Style.RESET_ALL,end='')
		print(WHITE)



if __name__ == '__main__':
	test = Console()
	test.addLine('Litle message for test')
	test.addLine('Succes',GREEN)
	test.addLine('ERROR',RED)
	theProgessBar = ProgessBar(3,'Test')
	test.addProgessBar(theProgessBar)
	test.showText()
	while not theProgessBar.statu:
		theProgessBar.progess()
		test.showText()
		test.addLine('Litle message for test')
		pause(0.5)
