from src import auditor


@auditor.audit_decorator
def simple_view(input: str):
    """A simple view to be part of a test."""
    print("simple_view:inner")
    return input
