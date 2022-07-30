import sys

from inventory import Acquire
from inventory.Item import ItemSpec

class Ink(ItemSpec):

  def __init__(self):
    super().__init__()

def main():
  filename = sys.argv[0]
  Acquire(filename)

if __name__ == "__main__":
  main()