def _cached(function):
    def anotherFunc(arg1, arg2, arg3):
        Sum = arg1 + arg2 + arg3
        Mul = arg1 * arg2 * arg3
        key = tuple([arg1, arg2, arg3])

        if len(memory) == 0:
            memory.update({key: [Sum, Mul]})
            print("Sum:", Sum)
            function(arg1, arg2, arg3)

        elif key not in memory:
            memory.update({key: [Sum, Mul]})
            print("Sum:", Sum)
            function(arg1, arg2, arg3)

        else:
            print("Sum and Mul:", memory[key])
    return anotherFunc


@_cached
def print_sum_then_mul(arg1, arg2, arg3):
    print("Mul:", arg1 * arg2 * arg3)


i = 0
memory = {}
N = int(input())
while i < N:
    num1, num2, num3 = map(int, input().split())
    print_sum_then_mul(num1, num2, num3)
