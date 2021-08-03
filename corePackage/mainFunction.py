from corePackage.awnser import *

def upgrade(needs):
	needs['core'].upgrade(needs['console'])

def manageComponent(needs):
	component = needs['core'].component
	needs['socket'].sendall(Awnser(line,"Start manage panel").code().encode())
	leave = False
	while not leave :
		text = "List of all component\n0- Leave manage\n"
		for c in component:
			text += "{} -> {}\n".format(c,component[c][0])
		print(text)
		print('Enter number of the component to manage ')
		ok = False
		slected = ""
		while not ok:
			selection = input(needs['core'].dataSet['name']['value']+">>> ")
			if selection != "0":
				try :
					selection = int(selection)
					assert(selection in component)
					slected = component[selection][1]
					ok = True
				except Exception :
					print('Bad number !')
			else :
				ok = True
				slected = "Quit"
		if slected != "Quit" and slected != "":
			txt,data = slected.getManage()
			print('Option of the component :\n{}\nEnter command :'.format(txt))
			ok = False
			while not ok:
				inp = input(">>>")
				if inp in data :
					slected.doManage(inp)
					ok = True
			needs['console'].showText()
		elif slected == "Quit":
			leave = True

	needs['socket'].sendall(Awnser(line,"Leaving manage panel").code().encode())
	needs['console'].showText()

