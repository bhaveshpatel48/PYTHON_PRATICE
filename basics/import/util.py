
'''
    #% -> Here the variable from the settings obj is accessed in order to trigger the settins to be loaded to memory
'''

from module1.conf import settings

print("Accessing the settings here : " + __file__)

print(settings.SURNAME)
print("Accessing the TZ_FUTURE in util.py ", settings.TZ_FUTURE)