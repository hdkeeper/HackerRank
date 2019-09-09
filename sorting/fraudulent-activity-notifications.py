MAX_EXP = 200

# Complete the activityNotifications function below.
def activityNotifications(exp, d):
    result = 0
    count = [0] * (MAX_EXP + 1)

    for i in range(0, d):
        count[exp[i]] += 1

    for i in range(d, len(exp)):
        median = getMedian(count, d)
        if median <= exp[i]:
            result += 1
        
        count[exp[i-d]] -= 1
        count[exp[i]] += 1
        
    return result

def getMedian(count, d):
    sum = 0
    for i in range(0, len(count)):
        sum += count[i]
        if 2*sum == d:
            return 2*i + 1
        elif 2*sum > d:
            return 2*i

    return 1


if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    expenditure = list(map(int, input().rstrip().split()))
    result = activityNotifications(expenditure, d)
    print(str(result) + '\n')
