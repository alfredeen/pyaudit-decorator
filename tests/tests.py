def simple_decorator(func):
    """A very simple decorator for testing."""

    def wrapper(*args, **kwargs):
        print("simple_decorator:Before function call")
        func(*args)
        assert args[0] == "test_simple_decorator hello _user_function_to_test"
        if args[0]:
            print(args[0])
        print("simple_decorator:After function call")

    return wrapper


def test_simple_decorator(capsys):
    """A test of a simple decorator."""

    _user_function_to_test("test_simple_decorator hello _user_function_to_test")

    captured = capsys.readouterr()

    assert captured is not None

    # The decorator adds the prefix and suffix part of the std out text
    # This text is printed by the decorator:
    expected = "simple_decorator:Before function call\n"
    # This text is printed by the user function:
    expected += "_user_function_to_test:inner\n"
    # This text is printed by the decorator using input to the user function:
    expected += "test_simple_decorator hello _user_function_to_test\n"
    # This text is printed by the decorator:
    expected += "simple_decorator:After function call\n"

    assert captured.out == expected


@simple_decorator
def _user_function_to_test(input: str):
    """A simple function to be part of a test."""
    print("_user_function_to_test:inner")
    return input


def test_verify_test_setup():
    """A simple test to verify the test setup."""
    assert True
