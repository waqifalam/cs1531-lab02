def find_reverse(numbers):
    print(numbers.reverse())

def find_max(numbers):
    print(max(numbers))

def find_min(numbers):
    print(min(numbers))

def find_sum(numbers):
    print(sum(numbers))

def find_average(numbers):
    print(sum(numbers)/len(numbers))

def find_descending(numbers):
    print(sorted(numbers, key=lambda x:-x))

def second_smallest(numbers):
    smallest = 99999999
    for num in numbers:
        if num < smallest:
            smallest = num
    second = 9999999
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
    #TODO: find the kth smallest number in the list
    pass
