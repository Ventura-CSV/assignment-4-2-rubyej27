def main():
    result = []
    a1 = int(input('Enter your first number: '))
    a2 = int(input('Enter your second number: '))
    N = int(input('Enter the number of sequences: '))
    result.append(a1)
    result.append(a2)
    """
    ########################################
    Code Your Program here
    ########################################
    """
    result = [a1, a2]
    for i in range(2, N):
        a3 = result[-1] + result[-2]
        result.append(a3)
    print(result)
    
    

    ########################################
    # Do not delete the return statement
    ########################################
    return result



if __name__ == '__main__':
    main()
