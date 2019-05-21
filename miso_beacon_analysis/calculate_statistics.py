"""This functions calculate some statistics from real data obtained from real devices"""

import json
import sys
from math import pow, sqrt
from matplotlib import pyplot
from numpy import linspace


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

    plot(data, "x")
    plot(data, "y")
    plot(data, "z")


if __name__ == "__main__":
    main()
