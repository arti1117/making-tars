import traceback

def f():
    tuple()[0]

try:
    f()
except IndexError:
    print('---Exception Occurred ---')
    traceback.print_exc(limit=1)

