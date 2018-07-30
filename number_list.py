def find_reverse(numbers):
    return(numbers[::-1])

def find_max(numbers):
    return(max(numbers))

def find_min(numbers):
    return(min(numbers))

def find_sum(numbers):
    return(sum(numbers))

def find_average(numbers):
    return(sum(numbers)/len(numbers))

def find_descending(numbers):
    return(sorted(numbers, key=lambda x:-x))

def second_smallest(numbers):
    smallest = min(numbers)
    second = max(numbers)
    for num in numbers:
        if num > smallest and num < second:
            second = num
    return second


'''
 bonus task:
 a function that takes in a list of numbers, and an index 'k' 
 and prints the kth smallest number in the list
'''
def kth_smallest(numbers, k):
    pass
