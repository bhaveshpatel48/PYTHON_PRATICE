from module1.conf import settings
print("Util settings started")
APP_VERSION = '1.0.0'

print("Call settings.GET_SSL() : util_settings.py " , settings.GET_SSL())

print("Accessing the TZ_FUTURE ", settings.TZ_FUTURE)

LANGUAGE = 'Python'
SYSTEM = 'UNIX'

print("Util settings ended")
