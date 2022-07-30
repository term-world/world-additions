import importlib
import inventory

from inventory.Item import FixtureSpec

class Printer(FixtureSpec):

    def __init__(self):
        super().__init__()
    
    def write(self, document:str):
        try:
            mod = importlib.import_module(document)
            doc = mod.__name__
            with open(f"{doc}.md", "w") as fh:
                item = getattr(mod, document)()
                fh.write(item.__str__())
        except:
            print("PC LOAD LETTER\nPC LOAD LETTER\nPC LOAD LETTER")

    def use(self, document):
        self.write(document)