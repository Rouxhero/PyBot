import os
import socket
import time
import sys
import re
from corePackage.awnser import Awnser
from Console.console import *
from Console.consoleObject import *
from time import sleep as pause

clean()
#OS checkup
if os.name == "posix":
	separator = '/'
else :
	separator = "\\"


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_hostname = socket.gethostname()
local_fqdn = socket.getfqdn()
 
ip_address = socket.gethostbyname(local_hostname)
port = 55468
 
server_address = (ip_address, port)

#Create var for final main
imports = "import os\nimport socket\n"
cmd = "\n\n\ncommand = {\n"

# Function to unpack file.cfg to data
def unpackConfig(text):
	cmds = ""
	newData = []
	files = []
	line = text.read()
	datas = re.findall(r"\[[a-zA-Z0-9]+\]\{[a-zA-Z0-9\s\t\n\.;':]*\}",line)
	for config in datas:
		title = re.findall(r'\[[a-zA-Z0-9]+\]',config)[0][1:-1]
		data = re.findall(r"\{[a-zA-Z0-9\s\t\n\.;':]*\}",config)[0][1:-1].replace('\t','').replace('\n','').split(';')
		if title == 'command':
			for line in data:
				if line != '':
					cmds += "\t"+line + ",\n"
		elif title == 'file':
			for file in data:
				if file != '':
					files.append(file)
					newData.append(file.split('.')[0])
	return {'cmd':cmds,'import':newData,'files':files}


# Create Console output

output = Console()


# cheking all file from package

output.print('Fetching package')
for path , dirs, files in os.walk('.'):
	if 'PackageConfig.cfg' in files:
		package = path.split(separator)[-1]
		output.println('found package : '+package+'\nImporting data : ')
		config = open(path+separator+'PackageConfig.cfg','r')
		data = unpackConfig(config)
		for file in data['files']:
			if not file in files:
				output.print('\nERROR :{}.{} not found'.format(package,file),RED)
				exit()
		cmd += data['cmd']
		for file in data['import']:
			imports+= 'from {}.{} import *\n'.format(package,file)
		output.print('ok',GREEN)
output.println('Importing package ok\nCreating main file : ')


try :
	open('main.py','w+').write(imports+cmd+'}\n'+open('.data/main.data','r').read())
except Exception as e:
	output.print('Erro :'+str(e),RED)


output.print('Done',GREEN)
output.println('Lauching main : ')
os.system('start python main.py')
output.print('Done',GREEN)
output.println('Starting server-side connection: ')
sock.bind(server_address)
sock.listen(1)
timeout = 0
output.print('Done',GREEN)
os.system('title PyBot output')
output.println("Waiting for a connection from main script : ")
connection, client_address = sock.accept()
output.print('Done',GREEN)
msg = Awnser()
while msg.data != 'quit':
	data = connection.recv(640)
	msg = Awnser.uncode(data)
	if msg.data == 'clear':
		output.clear()
	else :
		output.println("Received data : ")
		print(data)
		print(msg.code())
		output.print(msg.data,code[msg.statu])
	output.showText()
	pause(0.5)
 
connection.close()
output.print("Connection closed.")
exit()
