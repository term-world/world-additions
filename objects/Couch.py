from inventory.Item import FixtureSpec

class Couch(FixtureSpec):

    def __init__(self):
        super().__init__()

def main():
    obj = Couch()
    obj.use()

if __name__ == "__main__":
    main()