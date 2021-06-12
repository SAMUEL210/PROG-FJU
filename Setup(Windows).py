import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = 'C:\\Python\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = 'C:\\Python\\tcl\\tk8.6'

base = 'Win32GUI' #None

executables = [cx_Freeze.Executable('PROG FJU.py', base=base,\
                                    icon ='Images/FJU_Lyon.ico')]

cx_Freeze.setup(
    name = 'FJU LYON',
    options = {'build_exe': {'packages':\
                             ['idna', 'tkinter', 'turtle', 'pygame', \
                              'tkinter.messagebox','datetime',\
                              'math','random', 'time' ]}},
    version = '4.4.0',
    description = "Programme de la FJU LYON pour les activités du Samedi",
    executables = executables
)
