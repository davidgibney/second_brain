#!/usr/bin/env python3

def fizzlink(n=100):
    """Iterate from 1 to n numbers and conditionally print some arbitrary strings"""
    for num in range(1, n + 1):
        if num % 4 == 0 and num % 6 == 0:
            print("LinkedIn")
        elif num % 4 == 0:
            print("Linked")
        elif num % 6 == 0:
            print("In")
        else:
            print(num)

def fizzlink_2(n=100):
    """A variation of the solution"""
    for num in range(1, n + 1):
        linked = 'Linked' if num % 4 == 0 else ''
        _in = 'In' if num % 6 == 0 else ''
        print(f'{linked}{_in}' or num)

def gen_fizzlink(n=100):
    for i in range(1, n + 1):
        linked = 'Linked' if i % 4 == 0 else ''
        _in = 'In' if i % 6 == 0 else ''
        yield f'{linked}{_in}' or i


if __name__ == "__main__":
    print('Using first solution:')
    fizzlink()

    print('\nUsing second solution:')
    fizzlink_2()

    print('\nUsing third solution (generator):')
    for i in gen_fizzlink():
        print(i)
