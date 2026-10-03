import importlib.util

spec = importlib.util.spec_from_file_location(
    "even_odd_module",
    "Code/01_even_odd.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

even_odd = module.even_odd


def test_even_number():
    assert even_odd(10) == "Even"


def test_odd_number():
    assert even_odd(7) == "Odd"


def test_zero():
    assert even_odd(0) == "Even"


def test_negative_even():
    assert even_odd(-4) == "Even"


def test_negative_odd():
    assert even_odd(-5) == "Odd"


print("All test cases passed.")