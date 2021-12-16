def decorated(something="am i necessary"):
    def my_decorator(my_fun):
        print(something, "2")   # doesnt work in finally function only when u creat function

        def wrapper(*args, **kwargs):
            print(something, "1")
            print("hi")
            my_fun(*args, **kwargs)
            print("by")
        return wrapper
    print("3")  # doesnt work in finally function only when u creat function
    return my_decorator


@decorated("nothing")
def my_func(*args, **kwargs):
    print("my function")
    print(args)
    print(kwargs)


if __name__ == '__main__':
    my_func("test", "good", name="burger", price=12)
    # my_func = decorated(my_func)
    # my_func()

