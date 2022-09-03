import sys

from inventory import Acquire
from inventory.Item import ItemSpec

from narrator import Checkpoint

class Ink(ItemSpec):

  def __init__(self):
    super().__init__(__file__)

def main():
  filename = sys.argv[0]
  Checkpoint.set_flag('ink',__file__)
  Acquire(filename)

if __name__ == "__main__":
  main()
