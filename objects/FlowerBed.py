import os
import math
import narrator

from PIL import Image
from PIL import ImageDraw

from Flower import Flower
from inventory.Item import FixtureSpec
from narrator.Checkpoint import exists
from narrator.Checkpoint import set_flag
from narrator.Checkpoint import check_flag

class FlowerBed(FixtureSpec):

  def __init__(self):
    self.garden = "garden.png"
    if not exists([self.garden]):
      self.till()
    self.dirt = Image.open(self.garden)

  def till(self) -> None:
    img = Image.new(
      'RGB',
      (1000, 1000),
      (191, 168, 98)
    )
    draw = ImageDraw.Draw(img)
    draw.rectangle(
      ((50, 50),
      (950, 950)),
      fill=(116,102,59)
    )
    img.save(self.garden)

  def plant_flower(self, color: str, count: int) -> Image:
    flower = Image.open(
      Flower(color).use()
    )
    bed = Image.new(
      'RGBA',
      (300, 300),
      (0,0,0,0)
    )
    x, y = 0, 0
    for number in range(count):
      if number % 3 != 0:
        x += flower.size[0]
      elif x != 0:
        x = 0
        y += flower.size[1]
      bed.paste(flower, (x, y), mask=flower)
    os.remove("flower.png")
    return bed
    
  def place_plot(self, bed: Image, plot:int) -> None:
    plot -= 1
    x = 50 + (300 * (plot % 3))
    y = 50 + (300 * (plot // 3))

    self.dirt.paste(bed, (x, y), mask=bed)
    self.dirt.save(self.garden)

def main():
  n = narrator.Narrator()

  if check_flag("viewed"):
   
    q = narrator.YesNoQuestion({
      "question": "Skip the story",
      "outcome":[4.0, 3.0]
    })

    n.path.change(q.ask())

    if not n.path.number == 4:
      n.narrate()
      set_flag("viewed")
  
  bed = FlowerBed()

  q = narrator.YesNoQuestion({
    "question": "View the instructions again",
    "outcomes": [3.1, 4.0]
  })

  n.path.change(q.ask())

  if not n.path.scene == 0:
    n.narrate()

  color = input("Color of flower: ")
  plot = int(input("Section to plant [1-9]: "))
  count = int(input("Number to plant [1-9]: "))
  
  planted = bed.plant_flower(color, count)
  bed.place_plot(planted, plot)

  n.path.change(4.0)

  n.narrate()

if __name__ == "__main__":
  main()
