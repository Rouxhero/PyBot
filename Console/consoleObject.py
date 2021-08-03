# class file for all litle class util for output


class ProgessBar :

	def __init__(self,maxP,title,char="#"):
		self.maxP = maxP
		self.title = title
		self.progressP = 0
		self.char = char
		self.statu = False
		self.end = True



	def progess(self,nb=1):
		endP = self.progressP+nb
		if endP <= self.maxP :
			self.progressP = endP
		else:
			self.progressP = self.maxP
			self.statu = True

	def show(self):
		text = self.title + ' : '
		if self.statu:
			text += '[     Complete      ]'
		else :
			# maxChar = 50
			progress = int((self.progressP*50)/self.maxP)
			text += '['+'#'*progress+" "*(50-progress)+"]"
		return text


class Line :

	def __init__(self,text,color,noEnd=False):
		self.text = text
		self.color = color
		self.end = noEnd

	def show(self):
		return self.color+self.text


