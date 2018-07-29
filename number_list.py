def find_reverse(numbers):
    return numbers[::-1]

def find_max(numbers):
    return max(numbers)

def find_min(numbers):
    return min(numbers)


def find_sum(numbers):
    return sum(numbers)

def find_average(numbers):
    return sum(numbers) / len(numbers)

def find_descending(numbers):
    return sorted(numbers, reverse=True)



def second_smallest(numbers):
    # Initialise to maximum value possible
    sm1 = float('inf')  # smallest
    sm2 = float('inf')  # second smallest

    for n in numbers:

        if n < sm1:
            sm1, sm2 = n, sm1

        elif n == sm1:
            continue

        elif n < sm2:
            sm2 = n

    return sm2





'''
 bonus task:
 a function that takes in a list of numbers, and an index 'k' 
 and prints the kth smallest number in the list
'''
def kth_smallest(numbers, k):
    assert 1 <= k and k <= len(numbers)

    # remove duplicates
    numbers = list(set(numbers))

    # sort the list in ascending order
    numbers = sorted(numbers)

    # return the kth smallest
    return numbers[k - 1]
