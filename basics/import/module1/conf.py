
import importlib


class Settings:
    def __init__(self,module_name) -> None:
        print("Importing module")
        mod = importlib.import_module(module_name)
        print("dir of mod : ", dir(mod))
        for setting in dir(mod):
            setattr(self,setting,getattr(mod,setting))

class LazySettings:
    def __init__(self) -> None:
        self._wrapped = None
        self.modulename = 'module2.settings'
        
    def _setup(self):
        print("setup called: _wrapped ", self._wrapped)
        self._wrapped = Settings(self.modulename)
        
    def __getattr__(self, __name):
        try:
            print("self._wrapped : ", self._wrapped)
            if self._wrapped is None:
                print("called setup")
                self._setup()
            print("getting attributes value")
            return getattr(self._wrapped, __name)
        except Exception as e:
            print(e)
    
settings = LazySettings()