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

def virfib_sq(n):
    print(n)
    if n <= 1:
        return n
    return (virfib_sq(n - 1) + virfib_sq(n - 2)) ** 2


# wwpd_functions

def virfib_wwwpd(): # wwpd_virfib
    intro()

    print(inspect.getsource(virfib))

    print(">>> r0 = virfib_sq(0)")
    x = input()
    if x != str(virfib_sq(0)):
        x = repeat()

    print(">>> r1 = virfib_sq(1)")
    x = input()
    if x != str(virfib_sq(1)):
        x = repeat()

    print(">>> r2 = virfib_sq(2)")
    x = input()
    if x != str(virfib_sq(2)):
        x = repeat()
