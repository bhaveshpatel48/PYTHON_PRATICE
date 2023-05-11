from module1.conf import settings

print("Accessing the settings here : " + __file__)

print(settings.SURNAME)
print("Accessing the TZ_FUTURE in util.py ", settings.TZ_FUTURE)