import pytest
from _pytest import monkeypatch

from UVSim import (
    read,
    write,
    load,
    store,
    branch,
    branchneg,
    branchzero,
    add,
    subtract,
    multiply,
    divide,
)

def make_memory():
    return ["+0000" for inum in range(100)]

def fake_input(monkeypatch, value):
    def input_replacement(prompt):
        return value

    monkeypatch.setattr("builtins.input", input_replacement)

# I/O operation tests ------------------------------------------------------

def test_read_stores_positive_number(monkeypatch):
    memory = make_memory()

    fake_input(monkeypatch, "1515")
    read(memory, 10)

    assert memory[10] == "+1515"


def test_read_stores_negative_number(monkeypatch):
    memory = make_memory()

    fake_input(monkeypatch, "-1515")
    read(memory, 10)

    assert memory[10] == "-1515"


def test_write_displays_positive_number(capsys):
    memory = make_memory()
    memory[10] = "+1515"

    write(memory, 10)

    captured = capsys.readouterr()

    assert captured.out == "Content in address 10: +1515\n"


def test_write_displays_negative_number(capsys):
    memory = make_memory()
    memory[10] = "-1515"

    write(memory, 10)

    captured = capsys.readouterr()

    assert captured.out == "Content in address 10: -1515\n"


def test_load_retrieves_positive_value_from_memory():
    memory = make_memory()
    memory[10] = "+0015"

    result = load(memory, 10)

    assert result == 15


def test_load_retrieves_negative_value_from_memory():
    memory = make_memory()
    memory[10] = "-0015"

    result = load(memory, 10)

    assert result == -15


def test_store_saves_positive_value_from_accumulator_to_memory():
    memory = make_memory()
    accumulator = 15

    store(memory, 10, accumulator)

    assert memory[10] == "+0015"


def test_store_saves_negative_value_from_accumulator_to_memory():
    memory = make_memory()
    accumulator = -15

    store(memory, 10, accumulator)

    assert memory[10] == "-0015"

#Branching tests ---------------------------------------------------------

def test_branch_always_returns_target_address():
    target_address = 45

    result = branch(target_address)

    assert result == 45

def test_branchneg_does_not_branch_when_accumulator_is_positive():
    target_address = 45
    accumulator = 100

    result = branchneg(target_address, accumulator)

    assert result is None


def test_branchneg_branches_when_accumulator_is_negative():
    target_address = 45
    accumulator = -50

    result = branchneg(target_address, accumulator)

    assert result == 45


def test_branchzero_branches_when_accumulator_is_zero():
    target_address = 45
    accumulator = 0

    result = branchzero(target_address, accumulator)

    assert result == 45


def test_branchzero_does_not_branch_when_accumulator_is_nonzero():
    target_address = 45
    accumulator = 7

    result = branchzero(target_address, accumulator)

    assert result is None

#Arithmetic operations tests -----------------------------------------------

def test_add_adds_memory_value_to_accumulator():
    memory = make_memory()
    memory[10] = "+0005"
    accumulator = 3

    result = add(accumulator, memory, 10)

    assert result == 8


def test_add_adds_negative_number_to_accumulator():
    memory = make_memory()
    memory[10] = "-0005"
    accumulator = 3

    result = add(accumulator, memory, 10)

    assert result == -2


def test_subtract_subtracts_memory_value_from_accumulator():
    memory = make_memory()
    memory[10] = "+0003"
    accumulator = 10

    result = subtract(accumulator, memory, 10)

    assert result == 7


def test_subtract_subtracts_negative_number_from_accumulator():
    memory = make_memory()
    memory[10] = "-0003"
    accumulator = -10

    result = subtract(accumulator, memory, 10)

    assert result == -7


def test_multiply_multiplies_memory_value_by_accumulator():
    memory = make_memory()
    memory[10] = "+0004"
    accumulator = 5

    result = multiply(accumulator, memory, 10)

    assert result == 20


def test_multiply_with_negative_numbers():
    memory = make_memory()
    memory[10] = "-0004"
    accumulator = -5

    result = multiply(accumulator, memory, 10)

    assert result == 20

def test_divide_divides_accumulator_by_memory_value():
    memory = make_memory()
    memory[10] = "+0005"
    accumulator = 20

    result = divide(accumulator, memory, 10)

    assert result == 4

def test_divide_by_zero_exits_program():
    memory = make_memory()
    memory[10] = "+0000"
    accumulator = 10

    with pytest.raises(SystemExit):
        divide(accumulator, memory, 10)