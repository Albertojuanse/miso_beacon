"""This functions do operations over signals such as filtering, equalization..."""

from miso_beacon_analysis.calculate_statistics import average, standarddeviation, meansquarederror


def quitaverage(signal):
    """This function transforms a signal with no null average into a null average one"""
    # Calculate the average
    r = []
    ave = average(signal)
    for item in signal:
        r.append(item - ave)
    return r


def filtergaussiannoise(signal, n, average, standardeviation):
    """This function performs a n samples FIR filter for eliminating gaussian noise"""
