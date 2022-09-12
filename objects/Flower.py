import sys

from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor

from inventory.Item import ItemSpec

class Flower(ItemSpec):

  def __init__(self, color: str = "red"):
    super().__init__()
    self.size = 100
    self.im = Image.new(
      'RGBA',
      (self.size, self.size),
      (0,0,0,0)
    )
    try:
        self.color = ImageColor.getrgb(color)
    except ValueError:
        print("Hm. That's one rare color of flower. We can't get that!")
        sys.exit(1)
        
  def __str__(self) -> str:
    return f"It's a {self.color} flower"

  def use(self) -> str:
    draw = ImageDraw.Draw(self.im)
    draw.rectangle(
      ((self.size//3,0),
      (self.size*2/3,self.size)),
      fill = self.color
    )
    draw.rectangle(
      ((0,self.size//3),
      (self.size,self.size*2/3)),
      fill = self.color
    )
    self.im.save("flower.png")
    return "flower.png"
