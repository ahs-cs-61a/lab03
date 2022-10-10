# lab03 WWPD?

import inspect

# preliminaries

def repeat():
    print("try again:")
    return input()


def intro():
    print("What Would Python Display?")
    print(
        "type the expected output, 'function' if you think the answer is a function object, 'infinite loop' if it loops forever, 'nothing' if nothing is displayed, or 'error' if it errors; use single quotes '' when needed\n"
    )


def outro():
    print("\nall questions for this question set complete")


# reference functions

def virfib_sq(n): # with print
    print(n)
    if n <= 1:
        return n
    return (virfib_sq(n - 1) + virfib_sq(n - 2)) ** 2

def virfib_sq2(n): # without print, used to check answers  
    if n <= 1:
        return n
    return (virfib_sq2(n - 1) + virfib_sq2(n - 2)) ** 2


# wwpd questions

def wwpd_virfib_sq(): # wwpd_virfib
    intro()

    print(inspect.getsource(virfib_sq))

    print(">>> r0 = virfib_sq(0)")
    x = input()
    while x != "0":
        x = repeat()

    
    print(">>> r1 = virfib_sq(1)")
    x = input()
    while x != "1":
        x = repeat()


    print(">>> r2 = virfib_sq(2)")
    x = input()
    while x != "2":
        x = repeat()
    x = input()
    while x != "1":
        x = repeat()
    x = input()
    while x != "0":
        x = repeat()


    print(">>> r3 = virfib_sq(3)")
    x = input()
    while x != "3":
        x = repeat()
    x = input()
    while x != "2":
        x = repeat()
    x = input()
    while x != "1":
        x = repeat()
    x = input()
    while x != "0":
        x = repeat()
    x = input()
    while x != "1":
        x = repeat()


    print(">>> r3")
    x = input()
    while x != str(virfib_sq2(3)):
        x = repeat()


    print(">>> (r1 + r2) ** 2")
    x = input()
    while x != str((virfib_sq2(1) + virfib_sq2(2)) ** 2):
        x = repeat()
    

    print(">>> r4 = virfib_sq(4)")
    x = input()
    while x != "4":
        x = repeat()
    x = input()
    while x != "3":
        x = repeat()
    x = input()
    while x != "2":
        x = repeat()
    x = input()
    while x != "1":
        x = repeat()
    x = input()
    while x != "0":
        x = repeat()
    x = input()
    while x != "1":
        x = repeat()
    x = input()
    while x != "2":
        x = repeat()
    x = input()
    while x != "1":
        x = repeat()
    x = input()
    while x != "0": 
        x = repeat()


    print(">>> r4")
    x = input()
    while x != str(virfib_sq2(4)):
        x = repeat()
    
    outro()
