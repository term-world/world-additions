import gitit 

from inventory.Item import FixtureSpec

class Couch(FixtureSpec):

    def __init__(self):
        super().__init__()

    def use(self):
      try:
        gitit.get(file_name = "Ink.py")
      except:
        print("It looks like you already found think Ink!")

def main():
    obj = Couch()
    obj.use()

if __name__ == "__main__":
    main()
