def remove_smallest(numbers):
    output = []
    if not numbers:
        return numbers
    else:
        output = []
        lowest = min(numbers)
        counter = 0
        for number in numbers:
            if(lowest == number):
                counter += 1
            else:
                output.append(number)
            if counter > 1:
                output.append(number)
        return output
