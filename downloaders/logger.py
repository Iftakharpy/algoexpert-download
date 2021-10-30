def log_message_print_success_or_fail(message, log=True):
    def decorator(func:function):
        def wrapper(*args, **kwargs):
            if log:
                print(message)
            try:
                result = func(*args, **kwargs)
                if log:
                    print("Success")
                return result
            except Exception as e:
                if log:
                    print(f"Failed: {func.__name__}\({','.join([str(arg) for arg in args])}, {', '.join([f'{kwarg[0]} = {kwarg[1]}' for kwarg in kwargs.items()]) },)")
                print(e)
        return wrapper
    return decorator