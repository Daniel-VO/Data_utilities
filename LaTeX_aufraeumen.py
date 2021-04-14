"""
Created 14. April 2020 by Daniel Van Opdenbosch, Technical University of Munich

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. It is distributed without any warranty or implied warranty of merchantability or fitness for a particular purpose. See the GNU general public license for more details: <http://www.gnu.org/licenses/>
"""

import glob, os

Unterordner=input('Unterordner beinhalten (j/n)? ')
if Unterordner=='j':
	Ordner=os.listdir('.')
elif Unterordner=='n':
	Ordner=[os.getcwd()]
else:
	print('Eingabe nicht verstanden.')
	exit()

Endung=input('Eingabe Endung der aufzuraeumenden Dateien: ')

print('Aufzuraeumende Dateien sind jene, die nicht in lokalen .tex-Dateien referenziert werden. Sie werden nach dem Muster <Dateiname> -> del_<Dateiname> umbenannt.')

for o in Ordner:
	Prueftext=str()
	Texfiles=glob.glob(o+'/*.tex')
	for i in Texfiles:
		Prueftext+=open(i,'r').read()
	if Prueftext!=str():
		if '.' in Endung:
			Endung=Endung.split('.')[1]
		files=glob.glob(o+'/*.'+Endung)
		for j in files:
			filename=os.path.splitext(os.path.split(j)[1])[0]
			if filename not in Prueftext:
				print('mv "'+j+'" "'+os.path.split(j)[0]+'/del_'+os.path.split(j)[1]+'"')
				os.system('mv "'+j+'" "'+os.path.split(j)[0]+'/del_'+os.path.split(j)[1]+'"')


