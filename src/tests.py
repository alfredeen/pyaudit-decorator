import sys
from auditor import simple_decorator


def test_simple_decorator(capsys):
    """A simple test of the auditor decorator."""
    _user_function_to_test("test_simple_decorator hello _user_function_to_test")
    # TODO: assert something meaningful
    captured = capsys.readouterr()
    assert captured is not None
    expected = "simple_decorator:Before function call\ntest_simple_decorator hello _user_function_to_test\n"
    assert captured.out == expected


@simple_decorator
def _user_function_to_test(input: str):
    """A simple function to be part of a test."""
    print(input)
    return input


def test_myoutput(capsys):  # or use "capfd" for fd-level
    print("hello")
    sys.stderr.write("world\n")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"


def test_verify_test_setup():
    """A simple test to verify the test setup."""
    assert True
