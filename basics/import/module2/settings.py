
'''
    #% -> Settings file just like in django
    
    #? -> Module Import in Python
        #% -> Module gets imported once in a programme for the first time it encounters import, rest if anywhere else it is imported, it will take the modile from cache
        #% -> If module is not loaded completely, and we try to access the namespace from the module object, it can be noted that we will get only few variables, class or functions from the moduel object. 
        #% -> Load -> Compile -> Execute bytecode : Process of loadinf module to memory with importlib
        
    #? -> Import vs Importlib 
        
    #? -> Flow of this programme
        1) from util.py first time the settings variable accessed, and this triggers the settings to load in memory
        2) From module1.conf.py, _setup() is called
        3) From module1.conf.py.Settings, __init__() is called
        4) importlib.import_module() is called to load the module settings in memory
        5) Iteretate the module returned objects to set the napespace 
'''

import os

NAME = "bhavesh vaviya"
BASE_DIR = os.path.dirname(__file__)

# Import the another module/file
from .tz_settings import *

SURNAME = 'vaviya'

# Import the another module/file
from .util_settings import *

FROM = 'Kutch, Gujarat'