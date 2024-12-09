from src import auditor

# context = {"classname": "class1"}
context = "class1"


@auditor.audit_decorator(context)
def simple_view(input: str):
    """A simple view to be part of a test."""
    print("simple_view:inner")
    return input
