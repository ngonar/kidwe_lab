def high_and_low(numbers):
    # ...
    data = numbers.split(" ")
    print("Initial Data ",data)
    num = []
    for x in data:
        num.append(int(x))

    num.sort()

    print("Sorted : ",num)

    result = str(num[len(num)-1]) + " " + str(num[0])

    return result

high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"