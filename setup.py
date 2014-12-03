# -*- coding: utf8 -* 

import sys, os, codecs, inspect
from cx_Freeze import setup, Executable

path = os.path.realpath(__file__)
path2 = path.encode('utf-8')
try:
	setup(  name = "Simulador",
        version = "0.1",
        description = "Simulador para Operativa II",
        executables = [Executable(script="main.py", path=path2)])
except UnicodeEncodeError or UnicodeDecodeError:
	print "File System Encoding:", sys.getfilesystemencoding()
	print path2

#from distutils.core import setup
#import py2exe
#from glob import glob
#data_files = [("Microsoft.VC90.CRT", glob(r'C:\Program Files\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT\*.*'))]
#setup(
	#data_files=data_files,
	#console=['main.py']
	#)