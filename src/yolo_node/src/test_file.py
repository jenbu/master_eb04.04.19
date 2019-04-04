

def decorator(a_function):

    def wrapper():
        print("hei")
        return a_function()

    return wrapper

def doSomething():
    print("heisann")


if __name__ == "__main__":
    avc = decorator(doSomething)

