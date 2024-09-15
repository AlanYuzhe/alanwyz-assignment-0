def sum_num(x, y):
    '''A dummy task to sum x and y to console'''

    return x + y

if __name__ == "__main__":
    # test case
    x = 3
    y = 8
    print("The sum of {} and {} is {}".format(x, y, sum_num(x, y)))