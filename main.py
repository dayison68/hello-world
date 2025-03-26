import sys

def say_hello(name="world"):
    print(f"Hello, {name}!")

if __name__ == "__main__":
        if len(sys.argv) > 1:
            say_hello(sys.argv[1])
        else:
            say_hello()
