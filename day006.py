import random

class OoppsException(Exception):
    pass


# numbers = list()
# for i in range(5):
#     numbers.append(random.randint(1,100))
numbers = [random.randint(1,100) for i in range(5)]
print(numbers)

try :
    pick = int(input(f"Input index (0~{len(numbers)-1}) : "))
    print(numbers[pick])
    print(5/2)
    raise OopsException("Oopps~~") # exception!
except IndexError as err:
    print(f"Wrong index number\n{err}")
except ValueError as err:
    print(f"Input Only Number~\n{err}")
except ZeroDivisionError as err:
    print(f"The denominator cannot be 0.\n{err}")
except OoppsException as err:
    print(f"Oops Oops\n{err}")
except Exception as err:
    print(f"Error occurs\n{err}")
else:
    print(f'Program terminate')

# 순서대로 처리되기 때문에 범위가 작은 에러부터 차례대로 코드 작성





