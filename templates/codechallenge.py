
def swapnumbers():
    global int1
    global int2
    # set a temporary variable to hold int1's value
    temp = int1
    # set int1 equal to int2
    int1 = int2
    # set int2 equal to the temporary variable that is holding int1's value
    int2 = temp
    # int1, int2 = int2, int1


# The argument is a 2d array because it is a lists of lists
def matrixprint(matrix):
    # This is looping over the lists in matrix. The indexes go from 0 to len - 1
    for x in matrix:
        rowString = ""
        # This is a nested for loop that is looping over the numbers in each list
        for y in x:
            rowString += str(y)+ " "
        print(rowString)


if __name__ == "__main__":
    global int1
    global int2
    int1 = int(input("Enter a number: "))
    int2 = int(input("Enter a second number: "))

    print("Before: num1 = {0} and num2 = {1}".format(int1, int2))
    swapnumbers()

    print("After: num1 = {0} and num2 = {1}".format(int1, int2))
    matrixprint([[1,2,3],[4,5,6],[7,8,9]])