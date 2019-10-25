
from os import system, name
import time

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def menu(log=[]):
    should_run = True
    while should_run:
        def pick_function(i):
            dict = { 1 : hello,
                     2 : world,
                     3 : hello_world,
                     11 : exit
                }
            if i in dict:
                return dict.get(i)

        clear()

        print("MENU \n 1. Run hello function \n 2. Run world function \n 3. Run hello world function \n 11. Exit")
        print("\n".join(log))

        choice = input("choice: ")
        try:
            choice = int(choice)
        except ValueError:
            break;
        function = pick_function(int(choice))
        if function is not None:
            log.append(function())
        else:
            print("Invalid option \r")
            time.sleep(1)

    if should_run:
        menu(log)
    else:
        exit()



def hello():
    return "Hello"

def world():
    return "World"

def hello_world():
    return "Hello, World"


if __name__ == "__main__":
    print("Hello, world!")
    menu()
