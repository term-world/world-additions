import os
import random
import narrator

from inventory.Item import FixtureSpec

class Toaster(FixtureSpec):

    def __init__(self):
        super().__init__()

    def use(self):
        seed = math.floor(
            random.random() * 10
        )
        if seed > 5:
            print("🎊🎊 TOAST + 1 🎊🎊")
            if os.path.exists("a_toast"):
                os.rename("a_haunted_toast", "stack_of_haunted_toast")
            files = len(glob.glob("*_toast"))
            if not files:
                Path("a_toast").touch()
        else:
            print("NO TOAST 😞")

def main():
    n = narrator.Narrator()
    n.path.change(10.0)
    n.narrate()

if __name__ == "__main__":
    main()