

def encrypto(numbers):
    max_sum=[]
    for i in range(len(numbers)):
        numbers[i]=numbers[i]+1
        max_sum.append(sum(i))
        numbers[i]=numbers[i]-1

    return max(max_sum)

if __name__=="__main__":
    numbers = list(map(int, input().strip().split(' ')))
    result = encrypto(numbers)
    # print (" ".join(map(str, result)))
    print(result)
