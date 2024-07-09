from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """декоратор log будет логировать вызов функции и ее результат в файл или в консоль"""
            try:
                result = func(*args, **kwargs)

                my_message = "my_function ok\n"
                if filename:
                    with open(filename, "a") as f:
                        f.write(my_message)

                else:
                    print(my_message)

                return result

            except Exception as e:
                error_message = f"my_function error: {e}. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a") as f:
                        f.write(error_message)
                else:
                    print(error_message)
                return error_message

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


if __name__ == "__main__":
    print(my_function(1, "0"))
    print(my_function(1, 3))
    print(my_function())
    print(my_function(1, 19))
