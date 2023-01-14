# lab03 tests


# IMPORTS 

import labs.lab03 as lab
import tests.wwpd_storage as s
import re
import inspect
from io import StringIO 
import sys
import git

st = s.wwpd_storage 


# CAPTURING PRINTS (STDOUT) - https://stackoverflow.com/questions/16571150/how-to-capture-stdout-output-from-a-python-function-call

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout


# COLORED PRINTS - custom text type to terminal: https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal, ANSI colors: http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html

class bcolors:
    HIGH_MAGENTA = '\u001b[45m'
    HIGH_GREEN = '\u001b[42m'
    HIGH_YELLOW = '\u001b[43m'
    HIGH_RED = '\u001b[41m'
    HIGH_BLUE = '\u001b[44m'
    MAGENTA = ' \u001b[35m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    RED = '\u001b[31m'
    BLUE = '\u001b[34m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\u001b[0m'


# TESTS


def test_multiply():
    assert lab.multiply(5, 3) == 15
    assert lab.multiply(2, 0) == 0


def test_is_prime():
    assert lab.is_prime(2) == True
    assert lab.is_prime(1) == False
    assert lab.is_prime(16) == False
    assert lab.is_prime(521) == True


def test_hailstone():
    print("\n\nhailstone(10) prints:")
    with Capturing() as hailstone_10_output:
        lab.hailstone(10)
    hailstone_10 = ['10', '5', '16', '8', '4', '2', '1']
    if hailstone_10 != hailstone_10_output:
        print(bcolors.HIGH_YELLOW + bcolors.BOLD + "ERROR: Incorrect prints from hailstone(10)" + bcolors.ENDC)
        assert hailstone_10 == hailstone_10_output
    assert lab.hailstone(10) == 7

    print("\n\nhailstone(1) prints:")
    with Capturing() as hailstone_1_output:
        lab.hailstone(1)
    hailstone_1 = ['1']
    if hailstone_1 != hailstone_1_output:
        print(bcolors.HIGH_YELLOW + bcolors.BOLD + "ERROR: Incorrect prints from hailstone(1)" + bcolors.ENDC)
        assert hailstone_1 == hailstone_1_output
    assert lab.hailstone(1) == 1


def test_merge():
    assert lab.merge(31, 42) == 4321
    assert lab.merge(21, 0) == 21
    assert lab.merge(21, 31) == 3211


def test_summation():
    assert lab.summation(5, lambda x: x * x * x) == 225
    assert lab.summation(9, lambda x: x + 1) == 54
    assert lab.summation(5, lambda x: 2**x) == 62


def test_paths():
    assert lab.paths(2, 2) == 2
    assert lab.paths(5, 7) == 210
    assert lab.paths(117, 1) == 1
    assert lab.paths(1, 157) == 1


def test_pascal():
    assert lab.pascal(0, 0) == 1
    assert lab.pascal(0, 5) == 0
    assert lab.pascal(3, 2) == 3
    assert lab.pascal(4, 2) == 6


def test_double_eights():
    assert lab.double_eights(1288) == True
    assert lab.double_eights(880) == True
    assert lab.double_eights(538835) == True
    assert lab.double_eights(284682) == False
    assert lab.double_eights(588138) == True
    assert lab.double_eights(78) == False


def test_num_eights():
    assert lab.num_eights(3) == 0
    assert lab.num_eights(8) == 1
    assert lab.num_eights(88888888) == 8
    assert lab.num_eights(2638) == 1
    assert lab.num_eights(86380) == 2
    assert lab.num_eights(12345) == 0


def test_pingpong():
    assert lab.pingpong(8) == 8
    assert lab.pingpong(10) == 6
    assert lab.pingpong(15) == 1
    assert lab.pingpong(21) == -1
    assert lab.pingpong(22) == -2
    assert lab.pingpong(30) == -2
    assert lab.pingpong(68) == 0
    assert lab.pingpong(69) == -1
    assert lab.pingpong(80) == 0
    assert lab.pingpong(81) == 1
    assert lab.pingpong(82) == 0
    assert lab.pingpong(100) == -6


def test_count_coins():
    assert lab.count_coins(15) == 6
    assert lab.count_coins(10) == 4
    assert lab.count_coins(20) == 9
    assert lab.count_coins(100) == 242
    assert lab.count_coins(200) == 1463


# CHECK WWPD? IS ALL COMPLETE

def test_wwpd():
    assert len(st) == 22


# AUTO-COMMIT WHEN ALL TESTS ARE RAN

user = []

def test_commit():
    try:
        # IF CHANGES ARE MADE, COMMIT TO GITHUB
        user.append(input("\n\nWhat is your GitHub username (exact match, case sensitive)?\n"))
        repo = git.Repo("/workspaces/lab03-" + user[0])
        repo.git.add('--all')
        repo.git.commit('-m', 'update lab')
        origin = repo.remote(name='origin')
        origin.push()
        print(bcolors.HIGH_GREEN + bcolors.BOLD + "\nSUCCESS: Lab complete and changes successfully committed." + bcolors.ENDC)
    except: 
        # IF CHANGES ARE NOT MADE, NO COMMITS TO GITHUB
        print(bcolors.HIGH_MAGENTA + bcolors.BOLD + "\nMESSAGE: Already up to date. No updates committed." + bcolors.ENDC)


# ADDITIONAL TEST: BAN ITERATION & ASSIGNMENT STATEMENTS

def test_ban_iteration():
    path = "/workspaces/lab03-" + user[0] + "/labs/lab03.py"
    text_file = open(path, "r")
    data = text_file.read()
    text_file.close()
    search = re.search(r"(while|for).*:{1}", data)
    if search is not None:
        print(bcolors.HIGH_YELLOW + bcolors.BOLD + "ERROR: Iteration detected; please implement using recursion only." + bcolors.ENDC)
    assert search is None


def test_ban_assignments():
    function = inspect.getsource(lab.pingpong)
    search = re.search(r"[^=]={1}[^=]", function)
    if search is not None:
        print(bcolors.HIGH_YELLOW + bcolors.BOLD + "ERROR: Assignment statement(s) detected in pingpong; implement without using." + bcolors.ENDC)
    assert search is None 