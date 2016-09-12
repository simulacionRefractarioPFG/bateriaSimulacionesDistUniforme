import os
import glob
import math
import numpy as np


os.system('mpirun -np 4 liggghts < in1.MgO_proporcion_Rmin_radioMinimo_Rmax_radioMaximo')
os.system('mpirun -np 4 liggghts < in2.MgO_proporcion_Rmin_radioMinimo_Rmax_radioMaximo')
os.system('mpirun -np 4 liggghts < in3.MgO_proporcion_Rmin_radioMinimo_Rmax_radioMaximo')
newest = max(glob.iglob('post/dump*.pruebas'), key=os.path.getctime)
os.system('mv %s dump1' % (newest))
os.system('python PostProc.py >> ../../../MgO_' + str(PROPMGO) +'-' + str(FUERZA) + '.txt')
os.system('mpirun -np 4 liggghts < in4.MgO_proporcion_Rmin_radioMinimo_Rmax_radioMaximo')
newest = max(glob.iglob('post/dump*.pruebas'), key=os.path.getctime)
os.system('mv %s dump2' % (newest))
os.system('python PostProc.py >> ../../../MgO_' + str(PROPMGO) + '-' + str(FUERZA) + '.txt')

