"""This functions calculate some statistics from real data obtained from real devices"""

import json
import sys
import os
from math import pow, sqrt, pi
from matplotlib import pyplot
from numpy import linspace, arange, reshape, dot, asarray, exp


# ##### GET DATA #####
def readjson(path):
    with open(path, 'r') as f:
        data = json.load(f)
    return data


def getdatafromraw(rawdata, date, name):
    """This function retrieves each 'name' data item from a 'rawdata' file and a specific 'date'"""
    data = []
    for item in rawdata:
        if item["date"] == date:
            if item[name]:
                data.append(item[name])
    return data


def gettimefromraw(rawdata, date):
    """This function retrieves each 'name' data item's time from a 'rawdata' file and a specific 'date'"""
    time = []
    # Get the fisrt time stamp as initial time
    # Retrieve the time stamp and convert it into seconds
    splittimefirst = rawdata[0]["timestamp"].split(":")
    splittimefirst[0] = float(splittimefirst[0]) * 3600
    splittimefirst[1] = float(splittimefirst[1]) * 60
    splittimefirst.append(splittimefirst[0] +
                          splittimefirst[1] +
                          float(splittimefirst[2]))

    for item in rawdata:
        if item["date"] == date:
            if item["timestamp"]:
                # Retrieve the time stamp and convert it into seconds
                splittime = item["timestamp"].split(":")
                splittime[0] = float(splittime[0]) * 3600
                splittime[1] = float(splittime[1]) * 60
                time.append(splittime[0] +
                            splittime[1] +
                            float(splittime[2]) -
                            splittimefirst[3])
    return time


# ##### STATISTICS #####
def average(data):
    """This function calculates the average value of the data collection"""
    return sum(data) / len(data)


def standarddeviation(data):
    """This function calculates the standard deviation of the data collection"""
    ave = average(data)
    suma = 0
    for item in data:
        suma += pow(item - ave, 2)
    return sqrt(suma / (len(data) - 1))


def meansquarederror(data, expectedvalue):
    """This function calculates the mean square error value of the data collection"""
    sum = 0
    for item in data:
        sum += pow(item - expectedvalue, 2)
    return sum / len(data)


# ##### Signalling #####
def analycequantization(data):
    """This function calculates the quantization step of the amplitudes of a signal"""

    # Get the lowest amplitude step among them
    minamplitudestep = sys.maxsize
    lastitem = 0
    amplitudesteps = []
    for item in data:
        # Calculate amplitude step by euclidean norm
        amplitudestep = abs(item - lastitem)
        lastitem = item
        amplitudesteps.append(amplitudestep)
        # Save the minimum of them
        if amplitudestep < minamplitudestep and amplitudestep != 0:
            minamplitudestep = amplitudestep

    # Quantization exists if every amplitude is multiple of tha minimum; only for uniform quantizations
    quantizationdata = []
    for step in amplitudesteps:
        n = step / minamplitudestep
        quantizationdata.append(n)
    quantization = set(quantizationdata)
    return minamplitudestep, amplitudesteps, quantization


def dft_slow(signal, fs, N=None):
    """Compute the discrete Fourier Transform of a signal sampled with 'fs' rate in Hz"""
    # Sampling points for transform
    if not N:
        N = len(signal)
    # Calculate
    dft = []
    for m in range(N):
        sample = 0.0
        for n in range(N):
            sample += signal[n] * exp(- 1j * 2 * pi * m * n / N)
        dft.append(sample / N)
    # Frequency values for each sample of the N ones
    fs = fs  # Sampling rate in Hz
    fn = fs / 2  # Nyquist frequency
    ts = 1 / fs  # Sampling period
    df = 1 / (N * ts)  # Frequency step of DFT samples

    freq = []  # Frequency values
    for i in range(N):
        freq.append(-fn + i * df)
    return dft, freq


def idft_slow(signal, fs, N=None):
    """Compute the inverse discrete Fourier Transform of the signal sampled with 'fs' rate in Hz"""
    # Sampling points for transform
    if not N:
        N = len(signal)
    # Calculate
    idft = []
    for n in range(N):
        fn = 0.0
        for m in range(N):
            fn += signal[m] * exp(1j * 2 * pi * m * n / N)
        idft.append(fn)
    # Time values for each sample of the signal
    time = list(range(0, N))
    ts = 1 / fs  # Sampling period
    for i, t in enumerate(time):
        time[i] = t * ts

    return idft, time


# ##### Plotting #####
def plotsignal(time, data, name):
    """This function plots a signal from a collection of data and its time frame"""
    pyplot.plot(time, data)
    pyplot.ylabel(name)
    pyplot.xlabel("time")
    pyplot.show()


def plothistogram(data, numberofbins, name):
    """This function plots a histogram from a collection of data ana given number of bins"""
    minimum = min(data)
    maximum = max(data)
    bins = linspace(minimum, maximum, num=numberofbins)
    pyplot.hist(data, bins=bins)
    pyplot.ylabel(name)
    pyplot.xlabel("Deviation")
    pyplot.show()


def plotdft(n, dft):
    """This function plots a DFT transform of a signal"""
    pyplot.plot(n, dft)
    pyplot.ylabel("DFT")
    pyplot.xlabel("Frequency")
    pyplot.show()


# ##### Main #####
def main():

    # Retrieve data from raw file

    # name = "/accelerometer_raw_data" "2019-05-21"
    # date = "2019-05-21"
    # expectedx = 0.0
    # expectedy = 0.0
    # expectedz = -9.7994

    name = "/gyroscope_raw_data"
    date = "2019-05-27"
    expectedx = 0.0
    expectedy = 0.0
    expectedz = 0.0

    path = os.path.dirname(sys.modules['__main__'].__file__) + name
    data = readjson(path)
    datax = getdatafromraw(data, date, "x")
    datay = getdatafromraw(data, date, "y")
    dataz = getdatafromraw(data, date, "z")

    # Averages
    avex = average(datax)
    avey = average(datay)
    avez = average(dataz)
    print("#####      Average       #####")
    print("Average for x value: " + str(avex))
    print("Average for y value: " + str(avey))
    print("Average for z value: " + str(avez))
    print("")

    # Standard deviations
    standesx = standarddeviation(datax)
    standesy = standarddeviation(datay)
    standesz = standarddeviation(dataz)
    print("##### Standard deviation #####")
    print("Standard deviation for x value: " + str(standesx))
    print("Standard deviation for y value: " + str(standesy))
    print("Standard deviation for z value: " + str(standesz))
    print("")

    # Mean squared error
    msex = meansquarederror(datax, expectedx)
    msey = meansquarederror(datay, expectedy)
    msez = meansquarederror(dataz, expectedz)
    print("##### Mean square error  #####")
    print("Mean square error for x value: " + str(msex))
    print("Mean square error for y value: " + str(msey))
    print("Mean square error for z value: " + str(msez))
    print("")

    # Quantization 1.5e-5
    minamplitudestepx, amplitudestepsx, quantizationx = analycequantization(datax)
    minamplitudestepy, amplitudestepsy, quantizationy = analycequantization(datay)
    minamplitudestepz, amplitudestepsz, quantizationz = analycequantization(dataz)
    print("##### Quantization step  #####")
    print("First 100 amplitudes steps for x value:", str(amplitudestepsx[0:100]))
    print("Minumum amplitude step found for x value:", str(minamplitudestepx))
    print("Relations between them for x value:", str(quantizationx))
    print("First 100 amplitudes steps for y value:", str(amplitudestepsy[0:100]))
    print("Minumum amplitude step found for y value:", str(minamplitudestepy))
    print("Relations between them for y value:", str(quantizationy))
    print("First 100 amplitudes steps for z value:", str(amplitudestepsz[0:100]))
    print("Minumum amplitude step found for z value:", str(minamplitudestepz))
    print("Relations between them for z value:", str(quantizationz))

    timex = gettimefromraw(data, date)
    timey = gettimefromraw(data, date)
    timez = gettimefromraw(data, date)

    plotsignal(timex, datax, "x")
    plothistogram(datax, 1000, "x")
    plothistogram(datay, 1000, "x")
    plothistogram(dataz, 1000, "x")


if __name__ == "__main__":
    main()
