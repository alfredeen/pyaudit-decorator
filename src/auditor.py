def simple_decorator(func):
    """A very simple decorator for testing."""

    def wrapper(*args, **kwargs):
        print("simple_decorator:Before function call")
        func(*args)
        # print("After the function call")

    return wrapper
