from inventory.Item import FixtureSpec

class Lease(FixtureSpec):
  
  def __init__(self):
    super().__init__()

  def __str__(self) -> str:
    return """
# Very Official `term-world` lease

Oh, you're here.

We didn't expect you so soon.

Congratulations on moving to `term-world`, etc, blah blah blah. This document finalizes your residency so that you can have a wonderful,
labor-intensive time here, etc, blah blah blah.

Lorem ipsum and some more very official language. Lorem ipsum and some more very official language. Lorem ipsum and some more very official language.
Lorem ipsum and some more very official language. Lorem ipsum and some more very official language. Lorem ipsum and some more very official language.
Lorem ipsum and some more very official language. Lorem ipsum and some more very official language. Lorem ipsum and some more very official language.
Lorem ipsum and some more very official language. Lorem ipsum and some more very official language. Lorem ipsum and some more very official language.
Lorem ipsum and some more very official language. Lorem ipsum and some more very official language. Lorem ipsum and some more very official language.
Lorem ipsum and some more very official language. Lorem ipsum and some more very official language. Lorem ipsum and some more very official language.
Lorem ipsum and some more very official language. Lorem ipsum and some more very official language. Lorem ipsum and some more very official language.
Lorem ipsum and some more very official language. Lorem ipsum and some more very official language. Lorem ipsum and some more very official language.
Lorem ipsum and some more very official language. Lorem ipsum and some more very official language. Lorem ipsum and some more very official language.
Lorem ipsum and some more very official language. Lorem ipsum and some more very official language. Lorem ipsum and some more very official language.

   
Oh, right, you need to know what to do.

## Setting up residency

You need to tell `term-world` who you are in order to truly send and receive things. In your terminal, this is what you need to do (you
can copy and paste these commands, changing relevant details):

### 1. Setting up who you are

```
git config --global user.email "YOUR_ALLEGHENY_EMAL"
```

### 2. Labeling how you appear

```
git config --global user.name "YOUR_GITHUB_USER_NAME"
```

## Signature

- [ ] `TODO`

To sign the above:

1. Remove the `TODO` and replace it with your GitHub username
2. Place an `x` inside the brackets (`[]`) to check the box and official sign this document

"""

  def use(self) -> str:
    return self.__str__()

def main():
  lease = Lease()
  print(lease)

if __name__ == "__main__":
  main()