import numpy as np

def meanMoment(channel):
    sumValue = 0
    countValue = 0
    for i in range(len(channel)):
        for j in range(len(channel[i])):
            #if(channel[i][j] < 99):
            if(channel[i][j] < 200):
                sumValue += channel[i][j]
                countValue += 1
    if(countValue == 0):
        return 0
    else:
        return sumValue/countValue

def varianceMoment(channel, meanChannel):
    sumValue = 0
    countValue = 0
    for i in range(len(channel)):
        for j in range(len(channel[i])):
            #if(channel[i][j] < 99):
            if(channel[i][j] < 200):
                sumValue += np.power(channel[i][j] - meanChannel,2)
                countValue += 1
    if(countValue == 0):
        return 0
    else:
        return np.sqrt(sumValue/countValue)

def skewnessMoment(channel, meanChannel):
    sumValue = np.int64(0)
    countValue = 0
    for i in range(len(channel)):
        for j in range(len(channel[i])):
            #if(channel[i][j] < 99):
            if(channel[i][j] < 200):
                sumValue += np.power(channel[i][j] - meanChannel,3)
                countValue += 1
    if(countValue == 0):
        return 0
    else:
        return np.cbrt(sumValue/countValue)
    
def getColorMoment(channel):
    meanChannel = meanMoment(channel)
    varChannel = varianceMoment(channel, meanChannel)
    skewChannel = skewnessMoment(channel, meanChannel)

    #return meanChannel, varChannel, skewChannel
    return meanChannel, varChannel, skewChannel