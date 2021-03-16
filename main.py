def f(a, b, *args):
    arguments = (a, b) + args
    print(arguments)
    print(args)


f(1, 2)
