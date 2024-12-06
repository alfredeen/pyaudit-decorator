from auditor import simple_decorator


def test_simple_decorator():
    """A simple test of the auditor decorator."""
    _user_function_to_test("hello")
    # TODO: assert something meaningful


@simple_decorator
def _user_function_to_test(input: str):
    """A simple function to be part of a test."""
    print(input)
    return input


def test_verify_test_setup():
    """A simple test to verify the test setup."""
    assert 1 == 1
