import narrator

n = narrator.Narrator()

def main():
    n.path.change(10.0)
    n.narrate()

if __name__ == "__main__":
    main()