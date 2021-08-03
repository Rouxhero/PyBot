from tkinter.filedialog import *
from corePackage.awnser import *
import threading
import os


class FileWatcher(threading.Thread):
	def __init__(self,sender):
		threading.Thread.__init__(self)
		self._cached_stamp = {}
		self.path = askdirectory()
		self.data = []
		self.console = sender
		self.manage = {"stop":self.stop}
		for path, dirs, files in os.walk(self.path):
			for file in files:
				end = file.split('.')
				if len(end) > 1 :
					end = end[1]
					self.data.append(path+"/"+file)
					self._cached_stamp[path+"/"+file] = {"stamp":os.stat(path+"/"+file).st_mtime, "type":end}
		self.send(good,'start watching folder :\n{}'.format(self.path))
		self.send(good,'-> {} file(s) loaded'.format(len(self.data)))
		self.turn = True
	
	def send(self,etat,msg):
		self.console.sendall(Awnser(etat,msg).code().encode())
	   

	def getName(self):
		return 'File Watcher on {} '.format(self.path)

	def getManage(self):
		txt = ""
		allC = []
		for key in self.manage:
			txt += key+"\n"
			allC.append(key)
		return txt,allC

	def doManage(self,order):
		self.manage[order]()
	def run(self):
		while self.turn :
			for file in self.data :
				stamp = os.stat(file).st_mtime
				if stamp != self._cached_stamp[file]["stamp"]:
					self.send(warning,'FileChange : {} Updated !'.format(file))
					data = self.checkSyntaxe(self._cached_stamp[file]["type"],file)	
					text = "Checking syntaxe : "
					if data["status"] :
						self.send(good,text+'OK')
					else :
						self.send(error,text + data["data"])
					self._cached_stamp[file]["stamp"] = stamp


	def checkSyntaxe(self,types,file):
		rep = {"status":False,"data":""}
		if types == "py":
			rep['status'] = True
		elif types == "java":
			rep['status'] = True
			textFile = open(file,'r')
			line = '-1;\n'
			lineC = 0
			while line != '' :
				if len(line)>2 :
					if (line[-2] != ";" and
						line[-2] != "{" and 
						line.lstrip(' ').lstrip('\t').rstrip('\n') != "*/" and 
						line.lstrip(' ').lstrip('\t').rstrip('\n') != "/**" and 
						line.lstrip(' ').lstrip('\t').rstrip('\n')[0] != '*' and
						line.lstrip(' ').lstrip('\t').rstrip('\n') != "}"):
						rep['status'] = False
						rep['data']   = "missing ';' line({}) : {}".format(lineC,line)
						break 
				else :
					if line != '\n' and line != '*\n' and line != '}\n' and line != '':
						rep['status'] = False
						rep['data']   = "missing ';' line({}) : {}".format(lineC,line)
						break 
				line = textFile.readline()
				lineC+=1
		else:
			rep['status'] = True
		return rep
	def stop(self):
		self.send(warning,'stop watching folder :\n{}'.format(self.path))
		self.turn = False 