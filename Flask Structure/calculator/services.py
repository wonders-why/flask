from .models import Numbers, Division


def add(nums):
    numbers = Numbers(nums)
    result = numbers.nums[0]
    for num in numbers.nums[1:]:
        result += num
    return result

def subtract(nums):
    numbers = Numbers(nums)
    result = numbers.nums[0]
    for num in numbers.nums[1:]:
        result -= num
    return result

def multiply(nums):
    numbers = Numbers(nums)
    result = numbers.nums[0]
    for num in numbers.nums[1:]:
        result *= num
    return result

def divide(a, b):
    div = Division(a, b)
    if div.b == 0:
        return None, "Enter a valid value"
    return div.a / div.b, None
