def _cached(function):
    def anotherFunc(arg1, arg2, arg3):
        Sum, Mul = arg1 + arg2 + arg3, arg1 * arg2 * arg3
        key = tuple([arg1, arg2, arg3])

        if key not in Dict:
            Dict.update({key: [Sum, Mul]})
            print("Sum:", Sum)
            function(arg1, arg2, arg3)

        else:
            print("Sum and Mul:", Dict[key])
    return anotherFunc


@_cached
def print_sum_then_mul(arg1, arg2, arg3):
    print("Mul:", arg1 * arg2 * arg3)


Dict = {}
for i in range(int(input())):
    num1, num2, num3 = map(int, input().split())
    print_sum_then_mul(num1, num2, num3)
