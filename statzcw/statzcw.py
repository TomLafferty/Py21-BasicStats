


# can put in one .py file, shoot for about 76 lines long for total - Kris

# cov ... the z cor... z correlation, probably neeed to right a variance routine, which does a mean followed by an odd sumation... make sure that youre doing the sample mean, not the population mean

#take the sum of n divided by n, gives the population mean, the sample mean is the sum divided by n - 1...

#difference between population summary and sample version

def zcount(list) -> float:
    '''Count of a list'''
    return len(list)

def zmean(list) -> float:
    '''Mean of a list'''
    return sum(list) / zcount(list)

def zmode(array) -> list:
    '''Mode of a list'''
    most = max(list(map(array.count, array)))
    return list(set(filter(lambda x: array.count(x) == most, array)))

def zmedian(list) -> float:
    '''Median of a list'''
    length = len(list)
    middle = length // 2
    if length % 2:
        return float(sorted(list)[middle])
    else:
        return sum(sorted(list)[middle -1:middle +1]) / 2

def zvariance(list) -> float:
    '''Variance of a list,
    average of the squared differences from the mean'''
    n = zcount(list) - 1
    mean = zmean(list)
    deviations = []
    for xi in list:
        deviations.append((mean - xi) ** 2)
    variance = sum(deviations) / n
    return variance

def zstddev(list) -> float:
    '''Standard Deviation of a list,
    square root of the variance of a list'''
    return zvariance(list) ** 0.5

def zstderr(list) -> float:
    '''Standard error of a list,
    Standard deviation divided by square root of the count'''
    return zstddev(list) / (zcount(list) ** 0.5)

def zcov(list1, list2):
    '''Covariance of two lists to be used for correlation'''
    summed = 0
    for i in range(0, zcount(list1)):
        summed += ((list1[i] - zmean(list1)) * (list2[i] - zmean(list2)))
    return summed/(zcount(list1)-1)


def zcorr(listx, listy) -> float:
    '''Correlation, finding the covariance between the two lists,
    then the correlation is the covariance divided by the stddev of each list multiplied together'''
    return zcov(listx, listy) / (zstddev(listx) * zstddev(listy))


data0 = [1.0, 2.0, 3.0, 4.0, 5.0]
data2 = [1.0, 2.0, 2.0, 4.0, 5.0]
answer = (zcorr(data0, data2))
print(answer)
print(type(answer))