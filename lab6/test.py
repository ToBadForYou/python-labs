from lab6 import *


def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


def test_fib():
    print("Enter input for fibonaccis number")
    calc = ["calc", ["set", "a", 0], ["set", "b", 1], ["read", "n"],
            ["set", "counter", 2],
            ["if", ["n", "<", 0], ["print", "n"],
            ["if", ["n", "=", 0], ["print", "a"],
             ["if", ["n", "=", 1], ["print", "b"],
              ["while", ["counter", "<", "n"],
              ["set", "counter", ["counter", "+", 1]],
              ["set", "c", ["a", "+", "b"]],
              ["set", "a", "b"], ["set", "b", "c"]]]]],
            ["if", ["n", ">", 1], ["print", "b"]]
            ]
    result = eval_program(calc)
    python_result = fibonacci(result["n"])

    assert result["b"] == python_result


test_fib()
