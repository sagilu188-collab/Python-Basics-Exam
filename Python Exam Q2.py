import numbers


def find_median(numbers: list) -> float:
    sorted_list = sorted(numbers)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 != 0:
        return float(sorted_list[mid])
    else:
        left_mid = sorted_list[mid - 1]
        right_mid = sorted_list[mid]
        return (left_mid + right_mid) / 2.0


user_list = []
print("Enter a number:")
print("Enter '0' to quit.")

while True:
    try:
        user_input = input()
        num = float(user_input)

        if num == 0:
            if len(user_list) > 0:
                result = find_median(user_list)
                print(f"\n the median is {result}")
            else:
                print("\n the median is empty")
                break
        user_list.append(num)
    except ValueError:
        print("invalid input")
