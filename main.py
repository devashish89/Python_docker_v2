import functools
import sys


def sum(*nums):
    try:
        val = functools.reduce(lambda a,b:float(a)+float(b), *nums)
    except Exception as e:
        val = 0
    finally:
        return val


if __name__=='__main__':
    print(sum(sys.argv[1:]))