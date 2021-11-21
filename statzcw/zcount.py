


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
    '''Variance of a list'''




def zstddev(list) -> float:
    '''Standard Deviation of a list,
    square root of the variance of a list'''




def zstderr(list) -> float:
    '''Standard error of a list,
    Standard deviation divided by square root of the count'''


def zcorr(listx, listy) -> float:
    '''Correlation, finding the covariance between the two lists,
    then the correlation is the covariance divided by the stddev of each list multiplied together'''



answer = (zmedian([4,12,2,5,3]))
print(answer)
print(type(answer))