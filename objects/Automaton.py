from rich.console import Console
from rich.markdown import Markdown
from inventory.specs import ItemSpec

class Robot(ItemSpec):

    def __init__(self):
        super().__init__(__name__)
        self.volume = 1

    def __str__(self):
        return "It looks back. It's also awkward."

    def use(self):
        console = Console()
        console.print(Markdown("""> The robot throws itself at the challenge ahead while yelling 'Auto5 is aliiiiive!'
        
> This will turn out just fine."""))
