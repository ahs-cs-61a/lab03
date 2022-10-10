# lab03 tests

import labs.lab03 as lab
import re
import inspect


user = input("\n\nWhat is your GitHub username (exact match, case sensitive)?\n")
path = "/workspaces/lab03-" + user + "/labs/lab03.py"
text_file = open(path, "r")
data = text_file.read()
text_file.close()


def test_ban_iteration():
    search = re.search(r"(while|for).*:{1}", data)
    assert search is None


def test_ban_assignments():
    function = inspect.getsource(lab.pingpong)
    search = re.search(r"[^=]={1}[^=]", function)
    assert search is None # assignment statement(s) detected in pingpong, please implement without


def test_multiply():
    assert lab.multiply(5, 3) == 15
    assert lab.multiply(2, 0) == 0


def test_is_prime():
    assert lab.is_prime(2) == True
    assert lab.is_prime(1) == False
    assert lab.is_prime(16) == False
    assert lab.is_prime(521) == True


def test_hailstone():
    print("\n\nhailstone prints:")
    assert lab.hailstone(10) == 7
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