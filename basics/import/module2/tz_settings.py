from typing import Any
from module1.conf import settings

print("tz settings started")

TZ = 'Asia/Kolkata'

# print("Accessing var from settings.py : ", settings.BASE_DIR)

class getSSL:
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("DB_CERTS_PATH : ", DB_CERTS_PATH)
GET_SSL = getSSL()

TZ_FUTURE = 'UTC'

print("before acessing settings object var\n")

DB_CERTS_PATH = 'certificates/db/'+settings.BASE_DIR    #? Once the module is loaded and executed completely then only the variables, functions,class will be added to module namespace
# settings._wrapped = None    #? Keeping this will solve the problem
print("\ntz settings ended")

#^ Chatgpt conversation link : https://chat.openai.com/c/d7606dc4-fd22-4df4-bbf5-4834d8a62602
#^                           : https://chat.openai.com/c/8bd04f3f-2eaa-49bb-be6c-85af87af230f
#^                           : https://chat.openai.com/c/a16a7584-b736-4c39-a82c-93e04b3a0f30                            