"""This functions calculate some statistics from real data obtained from real devices"""

import json
import sys
from math import pow, sqrt, pi
from matplotlib import pyplot
from numpy import linspace, arange, reshape, dot, asarray, exp


def average(data, name):
    """This function calculates the average value of the variable 'name' collected from the data"""
    sum = 0
    i = 0
    for every in data:
        if every[name]:
            sum += every[name]
            i += 1
    return sum / i


def standarddeviation(data, name, ave):
    """This function calculates the standard deviation of the variable 'name' collected from the data"""
    sum = 0
    i = 0
    for every in data:
        if every[name]:
            sum += pow(every[name] - ave, 2)
            i += 1
    return sqrt(sum / (i - 1))


def meansquarederror(data, name, realvalue):
    """This function calculates the mean square error value of the variable 'name' collected from the data"""
    sum = 0
    i = 0
    for every in data:
        if every[name]:
            sum += pow(every[name] - realvalue, 2)
            i += 1
    return sum / i


def readjson(path):
    with open(path, 'r') as f:
        data = json.load(f)
    return data


def plot(data, name):
    """This function plots the signal 'name' and its deviation"""
    # 12:46:59.996620 12:47:00.008585
    xplotvalues = []
    rangeplotvalues = []
    rangeplotvaluesfirst = data[0]["timestamp"].split(":")
    rangeplotvaluesfirst[0] = float(rangeplotvaluesfirst[0]) * 3600
    rangeplotvaluesfirst[1] = float(rangeplotvaluesfirst[1]) * 60
    rangeplotvaluesfirst.append(rangeplotvaluesfirst[0] + rangeplotvaluesfirst[1] + float(rangeplotvaluesfirst[2]))
    min = sys.maxsize
    max = -sys.maxsize

    for every in data:
        if every[name] and every["timestamp"]:
            xplotvalues.append(float(every[name]))
            splitplotvalue = every["timestamp"].split(":")
            splitplotvalue[0] = float(splitplotvalue[0]) * 3600
            splitplotvalue[1] = float(splitplotvalue[1]) * 60
            rangeplotvalues.append(splitplotvalue[0] +
                                   splitplotvalue[1] +
                                   float(splitplotvalue[2]) -
                                   rangeplotvaluesfirst[3])
            if every[name] < min:
                min = every[name]
            if every[name] > max:
                max = every[name]

    pyplot.plot(rangeplotvalues, xplotvalues)
    pyplot.ylabel(name)
    pyplot.xlabel("time")
    pyplot.show()

    bins = linspace(min, max, num=500)
    pyplot.hist(xplotvalues, bins=bins)
    pyplot.ylabel(name)
    pyplot.xlabel("deviation")
    pyplot.show()


def dft_slow(data, name):
    """Compute the discrete Fourier Transform of the 'name' signal"""
    """
    datavalues = []
    for every in data:
        if every[name]:
            datavalues.append(float(every[name]))
    print("")
    print("DFT data retieved for "+name)

    x = asarray(datavalues[0:15000], dtype=float)
    N = x.shape[0]
    n = arange(N)
    k = n.reshape((N, 1))
    M = exp(-2j * pi * k * n / N)
    dft = dot(M, x)
    f = range(0, (N - 1)*100 / N)
    print("DFT calculed for "+name)
    return f, dft
    """
    datavalues = []
    for every in data:
        if every[name]:
            datavalues.append(every[name])
    print("")
    print("DFT data retieved for "+name)

    fs = len(datavalues)  # Sampling rate
    dt = 1/fs
    N = len(datavalues)  # Sampling of Fourier transform
    df = 1 / (N * dt)  # Frequency step
    nyq = 1 / (dt * 2)

    """
    time = list(range(0, N-1))  # Time values
    for i, t in enumerate(time):
        time[i] = t * dt
    print("DFT time array calculated for "+name)
    """
    freq = []  # Frequency values
    lastfrec = 0
    while lastfrec < nyq - df:
        newfreq = -nyq + lastfrec
        print(newfreq)
        lastfrec = abs(newfreq)
        freq.append(newfreq)
    print("DFT freq array calculated for "+name)
    print("DFT points:", N)


    dft = []
    for k in range(0, N-1):
        sum = 0
        for n in range(0, N-1):
            sum = sum + datavalues[n+1] * exp(-(1j * 2 * pi * k * n) / N)
            # sum = sum + datavalues[n+1] * exp(-1*j * 2 * pi + freq[k] * time[n])
        dft.append(sum)
        print(k)

    return freq, dft



def plotdft(n, dft):
    """This function plots the data"""
    pyplot.plot(n, dft)
    pyplot.ylabel("DFT")
    pyplot.xlabel("pulsation")
    pyplot.show()


def analycequantization(data, name, correction):
    """This function calculates the quantization step of quantization of the amplitudes of a signal"""
    min = sys.maxsize
    lastevery = 0
    amplitudesteps = []
    for every in data:
        if every[name]:
            amplitudstep = abs(every[name] - lastevery)
            lastevery = abs(every[name])
            amplitudesteps.append(amplitudstep)
            if amplitudstep < min and amplitudstep != 0:
                min = amplitudstep

    print(amplitudesteps[0:1000])
    quantizationdata = []
    for amplitud in amplitudesteps:
        n = amplitud / min
        quantizationdata.append(n)
    quantization = set(quantizationdata)

    print("Consecutive amplitudes minimum step for "+name+" value:", str(min))
    print("Relations between them for "+name+" value:", str(quantization))
    print("Corrected minimum step value for "+name+" value: "+str(correction))
    min = 1.5e-05
    quantizationdata = []
    for amplitud in amplitudesteps:
        n = amplitud / min
        quantizationdata.append(n)
    quantization = set(quantizationdata)
    print("Corrected relations between them for "+name+" value: ", quantization)


def main():

    name = "accelerometer_raw_data"
    path = "/Users/miso/Desktop/alberto/Archivo/Código/_Repositorios/miso_beacon/miso_beacon_analysis/" + name

    data = readjson(path)
    avex = average(data, "x")
    avey = average(data, "y")
    avez = average(data, "z")

    print("Average for x value: " + str(avex))
    print("Average for y value: " + str(avey))
    print("Average for z value: " + str(avez))

    standesx = standarddeviation(data, "x", avex)
    standesy = standarddeviation(data, "y", avey)
    standesz = standarddeviation(data, "z", avez)

    print("Standard deviation for x value: " + str(standesx))
    print("Standard deviation for y value: " + str(standesy))
    print("Standard deviation for z value: " + str(standesz))

    msex = meansquarederror(data, "x", 0)
    msey = meansquarederror(data, "y", 0)
    msez = meansquarederror(data, "z", -9.7994)

    print("Mean square error for x value: " + str(msex))
    print("Mean square error for y value: " + str(msey))
    print("Mean square error for z value: " + str(msez))

    print("")
    analycequantization(data, "x", 1.5e-5)
    print("")
    analycequantization(data, "y", 1.5e-5)
    print("")
    analycequantization(data, "z", 1.5e-5)

    # plot(data, "x")
    # plot(data, "y")
    # plot(data, "z")

    n, dft = dft_slow(data, "x")
    plotdft(n, dft)
    # n, dft = DFT(data, "x")
    # plotDFT(n, dft)
    # n, dft = DFT(data, "x")
    # plotDFT(n, dft)


if __name__ == "__main__":
    main()
