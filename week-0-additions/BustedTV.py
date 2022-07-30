import narrator

from inventory.Item import FixtureSpec

class BustedTV(FixtureSpec):

    def __init__(self):
        super().__init__()

n = narrator.Narrator()

def main():
    n.path.change(9.0)
    n.narrate()

if __name__ == "__main__":
    main()