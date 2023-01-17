# lab03 WWPD?


# IMPORTS 

import inspect
import tests.wwpd_storage as s

st = s.wwpd_storage


# COLORED PRINTS - custom text type to terminal: https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal, ANSI colors: http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html

class bcolors:
    HIGH_MAGENTA = '\u001b[45m'
    HIGH_GREEN = '\u001b[42m'
    HIGH_YELLOW = '\u001b[43;1m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\u001b[0m'


# INCORRECT ANSWER LOOP, INSTRUCTIONS, COMPLETE, OPTIONS

def repeat():
    print("Try again:")
    return input()

def intro(name):
    print("\nWhat Would Python Display?: " + name)
    print("Type the expected output, 'function' if you think the answer is a function object, 'infinite loop' if it loops forever, 'nothing' if nothing is displayed, or 'error' if it errors; use single quotes '' when needed.\n")

def complete():
    print(bcolors.HIGH_GREEN + bcolors.BOLD + "\nSUCCESS: All questions for this question set complete." + bcolors.ENDC)

def options():
    print(bcolors.HIGH_MAGENTA + bcolors.BOLD + "\nMESSAGE: All questions for this question set complete. Restart question set?" + bcolors.ENDC)
    guess = input("Y/N?\n")
    guess = guess.lower()
    while guess != "y" and guess != "n":
        print(bcolors.HIGH_YELLOW + bcolors.BOLD + "\nUnknown input, please try again." + bcolors.ENDC)
        guess = input()
    if guess == "y":
        return "restart"
    return False


# WWPD? ALGORITHM 

def wwpd(name, question_set, stored_list):

    intro(name)

    matched = str([i[:-1] for i in question_set])[1:-1] in str([i[:-1] for i in stored_list])
    restart = matched and options() == "restart"
    done = False

    for q in question_set:
        q[4] = True
        if q not in stored_list or restart:
            done = True 
            if q[1]:
                print(q[1])
            if q[2]:
                print(q[2])
            guess = input()
            while guess != q[3]:
                guess = repeat()
            if not matched:
                op = open("tests/wwpd_storage.py", "w")
                for j in range(len(stored_list)):
                    if q[0] < stored_list[j][0]:
                        stored_list.insert(j, q)
                        break
                if q not in stored_list: 
                    stored_list.append(q)
                op.write("wwpd_storage = " + str(stored_list))
                op.close()
    if done:
        complete()


# REFERENCE FUNCTIONS, CLASSES, METHODS, SEQUENCES, ETC.

# https://inst.eecs.berkeley.edu/~cs61a/su22/lab/lab03/

def virfib_sq(n): # with print
    print(n)
    if n <= 1:
        return n
    return (virfib_sq(n - 1) + virfib_sq(n - 2)) ** 2

def virfib_sq2(n): # without print, used to check answers  
    if n <= 1:
        return n
    return (virfib_sq2(n - 1) + virfib_sq2(n - 2)) ** 2


# QUESTION SET - ELEMENT FORMAT: [<QUESTION NUMBER>, <INITIAL PRINTS> (usually empty), <QUESTION>, <ANSWER>]
# INSPECT MODULE - convert function/class body into String: https://docs.python.org/3/library/inspect.html 
# wwpd questions

virfib_sq_qs = [
    [1, "\n" + inspect.getsource(virfib_sq), ">>> r0 = virfib_sq(0)", "0"],
    [2, "", ">>> r1 = virfib_sq(1)", "1"],
    [3, "", ">>> r2 = virfib_sq(2)", "2"],
    [4, "", "", "1"],
    [5, "", "", 0],
    [6, "", ">>> r3 = virfib_sq(3)", "3"], 
    [7, "", "", 2],
    [8, "", "", 1],
    [9, "", "", 0],
    [10, "", "", 1],
    [11, "", ">>> r3", str(virfib_sq2(3))],
    [12, ">>> (r1 + r2) ** 2", str((virfib_sq2(1) + virfib_sq2(2)) ** 2)],
    [13, "", ">>> r4 = virfib_sq(4)", "4"],
    [14, "", "", "3"]
    [15, "", "", "2"],
    [16, "", "", "1"],
    [17, "", "", "0"],
    [18, "", "", "1"],
    [19, "", "", "2"],
    [20, "", "", "1"],
    [21, "", "", "0"], 
    [22, "", ">>> r4", str(virfib_sq2(4))]
]

all_qs = [virfib_sq_qs]

for set in all_qs:
    for q in set:
        q.append(False)

# WWPD? QUESTIONS

def wwpd_virfib_sq(): 
    wwpd("Virahanka Fibonacci", virfib_sq_qs)
