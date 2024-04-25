# bubblesort is a classic algorithm and is very easy to understand
# it is a little brute-forced and its complexity O(n^2), which isn't great.

# let's say we need to sort this array
array = [11, 8, 0, 9, 1, 3, 4, 2, 5]

# think of the numbers as having density. Like bubbles they want to float to the top.
# smaller numbers have a higher density and larger numbers have a lower, like an over-inflated balloon.

# let's say we want to sort this array. We'll need a loop and we need to rerun this loop
# until we've sorted the array.
unsorted = True

# a while loop can take a boolean variable.
while unsorted:
    # we set unsorted to false so the loop ends if it isn't set to True again
    # it will be set to true every time a swap is made, which only happens when you are unsorted=
    unsorted = False
    # we need to iterate through the array, but we need to stop 1 short because we
    # will compare two numbers at a time.
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            # swap the numbers
            array[i], array[i + 1] = array[i + 1], array[i]
            # we made a swap so we are still in an unsorted list
            unsorted = True

print(array)