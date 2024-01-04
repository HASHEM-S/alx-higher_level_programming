import sys

def print_arguments(*args):
    num_args = len(args)

    print("Number of argument{}: {}".format("s" if num_args != 1 else "", num_args), end="")
    if num_args == 0:
        print(".", end="")
    else:
        print(":", end="\n")
        for i, arg in enumerate(args, start=1):
            print("{}: {}".format(i, arg))

if __name__ == "__main__":
    print_arguments("arg1", "arg2", "arg3")

