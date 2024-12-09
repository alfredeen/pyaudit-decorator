def audit_decorator(func, context=None):
    """
    An audit decorator.

    TODO: Add facilities to:
    - capture and append information of interest:
    Pattern: [ts] [userid] [action-verb] [object-type [objectid] [view/endpoint]
    Example AUDIT: ts user102 created user-app 1234 view/apps/create
    Example AUDIT: ts user101 updated user-profile None view/edit-profile
    """

    def wrapper(*args, **kwargs):
        func(*args)

        # Parse the context. Expected data for now: context["classname"]
        if context:
            classname = context["classname"]

        logmsg = f"test {classname}"

        # TODO: add logging
        print(logmsg)

    return wrapper
