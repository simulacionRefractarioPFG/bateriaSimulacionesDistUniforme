import os
import glob
import math
import numpy as np

'''
	Bateria de simulaciones con distribucion en masa uniforme.
	Ejecuta simulaciones en funcion de la proporcion de MgO, de la fuerza maxima aplicada y 
	del radio minimo en la distribucion uniforme.
'''

# Poder manipular la carpeta sin que me vuelvan a pedir permiso
os.system('sudo mkdir dumps')
os.system('sudo mkdir scripts')
os.system('sudo mkdir post')	
os.system('sudo chmod -R 777 ./*')

MgO = ['60.0', '75.0', '90.0']
for proporcion in MgO:

	directorioProporcion = './scripts/input_MgO-' + proporcion
	fuerzas = [1000, 100000, 10000000] # Newtons -> 1kN, 100kN, 10T

	for fuerza in fuerzas:
		os.system("sed -e 's/FUERZA/%d/g' in.plantilla2.0 > in.plantilla2" % (fuerza))
		os.system("sed -e 's/PROPMGO/%.0f/g' -e 's/FUERZA/%d/g' ejecuta0.py > ejecuta.py" % (float(proporcion), fuerza))
		os.system('python plantilla2scripts.py')
		directorioMgO = os.listdir(directorioProporcion)
		directorioMgO.sort()

		for caso in directorioMgO:
			if(caso.endswith('1450')):
				os.chdir(directorioProporcion + '/' + caso)
				os.system('python ejecuta.py')
				# archivos dump para posible renderizado posterior
				os.system('mv dump1 ../../../dumps/dump1MgO_%s-%s-F_%sN' % (proporcion, caso, str(fuerza)))
				os.system('mv dump2 ../../../dumps/dump2MgO_%s-%s-F_%sN' % (proporcion, caso, str(fuerza)))
				# Vuelve a directorio simulaciones
				os.chdir('../../../')


print 'Tareas completadas! :D'
# Apaga el equipo si se ejecuta en un servidor
#os.system('sudo shutdown -h now')
