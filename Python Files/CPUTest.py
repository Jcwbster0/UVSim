import pytest

from CPU import CPU


def make_memory():
    return ["+0000" for inum in range(100)]


class FakeController:
    def __init__(self):
        self.output = []

    def handleWrite(self, output):
        self.output.append(output)


# I/O operation tests ------------------------------------------------------

def test_read_stores_positive_number():
    cpu = CPU()
    cpu.memory = make_memory()

    cpu.read(None, "1515", 10)

    assert cpu.memory[10] == "+1515"


def test_read_stores_negative_number():
    cpu = CPU()
    cpu.memory = make_memory()

    cpu.read(None, "-1515", 10)

    assert cpu.memory[10] == "-1515"


def test_write_outputs_positive_number():
    cpu = CPU()
    controller = FakeController()
    cpu.memory = make_memory()
    cpu.memory[10] = "+1515"

    cpu.write(controller, 10)

    assert controller.output == ["+1515"]


def test_write_outputs_negative_number():
    cpu = CPU()
    controller = FakeController()
    cpu.memory = make_memory()
    cpu.memory[10] = "-1515"

    cpu.write(controller, 10)

    assert controller.output == ["-1515"]


def test_load_retrieves_positive_value_from_memory():
    cpu = CPU()
    cpu.memory = make_memory()
    cpu.memory[10] = "+0015"

    cpu.load(10)

    assert cpu.accumulator == 15


def test_load_retrieves_negative_value_from_memory():
    cpu = CPU()
    cpu.memory = make_memory()
    cpu.memory[10] = "-0015"

    cpu.load(10)

    assert cpu.accumulator == -15


def test_store_saves_positive_value_from_accumulator_to_memory():
    cpu = CPU()
    cpu.memory = make_memory()
    cpu.accumulator = 15

    cpu.store(10)

    assert cpu.memory[10] == "+0015"


def test_store_saves_negative_value_from_accumulator_to_memory():
    cpu = CPU()
    cpu.memory = make_memory()
    cpu.accumulator = -15

    cpu.store(10)

    assert cpu.memory[10] == "-0015"

#Branching tests ---------------------------------------------------------

def test_branch_always_returns_true():
    cpu = CPU()

    result = cpu.branch()

    assert result is True


def test_branchNeg_does_not_branch_when_accumulator_is_positive():
    cpu = CPU()
    cpu.accumulator = 100

    result = cpu.branchNeg()

    assert result is None


def test_branchNeg_branches_when_accumulator_is_negative():
    cpu = CPU()
    cpu.accumulator = -50

    result = cpu.branchNeg()

    assert result is True


def test_branchZero_branches_when_accumulator_is_zero():
    cpu = CPU()
    cpu.accumulator = 0

    result = cpu.branchZero()

    assert result is True


def test_branchZero_does_not_branch_when_accumulator_is_nonzero():
    cpu = CPU()
    cpu.accumulator = 7

    result = cpu.branchZero()

    assert result is None

#Arithmetic operations tests -----------------------------------------------

def test_add_adds_memory_value_to_accumulator():
    cpu = CPU()
    cpu.memory = make_memory()
    cpu.memory[10] = "+0005"
    cpu.accumulator = 3

    cpu.add(10)

    assert cpu.accumulator == 8


def test_add_adds_negative_number_to_accumulator():
    cpu = CPU()
    cpu.memory = make_memory()
    cpu.memory[10] = "-0005"
    cpu.accumulator = 3

    cpu.add(10)

    assert cpu.accumulator == -2


def test_subtract_subtracts_memory_value_from_accumulator():
    cpu = CPU()
    cpu.memory = make_memory()
    cpu.memory[10] = "+0003"
    cpu.accumulator = 10

    cpu.subtract(10)

    assert cpu.accumulator == 7


def test_subtract_subtracts_negative_number_from_accumulator():
    cpu = CPU()
    cpu.memory = make_memory()
    cpu.memory[10] = "-0003"
    cpu.accumulator = -10

    cpu.subtract(10)

    assert cpu.accumulator == -7


def test_multiply_multiplies_memory_value_by_accumulator():
    cpu = CPU()
    cpu.memory = make_memory()
    cpu.memory[10] = "+0004"
    cpu.accumulator = 5

    cpu.multiply(10)

    assert cpu.accumulator == 20


def test_multiply_with_negative_numbers():
    cpu = CPU()
    cpu.memory = make_memory()
    cpu.memory[10] = "-0004"
    cpu.accumulator = -5

    cpu.multiply(10)

    assert cpu.accumulator == 20

def test_divide_divides_accumulator_by_memory_value():
    cpu = CPU()
    cpu.memory = make_memory()
    cpu.memory[10] = "+0005"
    cpu.accumulator = 20

    cpu.divide(10)

    assert cpu.accumulator == 4

def test_divide_by_zero_raises_zero_division_error():
    cpu = CPU()
    cpu.memory = make_memory()
    cpu.memory[10] = "+0000"
    cpu.accumulator = 10

    with pytest.raises(ZeroDivisionError):
        cpu.divide(10)
