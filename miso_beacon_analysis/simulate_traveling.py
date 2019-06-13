from miso_beacon_analysis.calculate_statistics import getdatafromraw, gettimefromraw, average, standarddeviation, readjson, plothistogram, plotsignal
import json
import os
import sys
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# ##### Raw data extracting and plotting
def preparedata():

    # Retrieve data from raw file

    name = "/travel_raw_data_1"
    date = "2019-06-13"
    expectedx = 0.0
    expectedy = 0.0
    expectedz = -9.7994

    path = os.path.dirname(sys.modules['__main__'].__file__) + name
    data = readjson(path)
    data_accelerometer_x = getdatafromraw(data, date, "x", "accelerometer")
    data_gyroscope_x = getdatafromraw(data, date, "x", "gyroscope")
    data_accelerometer_y = getdatafromraw(data, date, "y", "accelerometer")
    data_gyroscope_y = getdatafromraw(data, date, "y", "gyroscope")
    data_accelerometer_z = getdatafromraw(data, date, "z", "accelerometer")
    data_gyroscope_z = getdatafromraw(data, date, "z", "gyroscope")

    return data_accelerometer_x, data_gyroscope_x, data_accelerometer_y, \
           data_gyroscope_y, data_accelerometer_z, data_gyroscope_z


def preparetimes():
    name = "/travel_raw_data_1"
    date = "2019-06-13"
    path = os.path.dirname(sys.modules['__main__'].__file__) + name
    data = readjson(path)
    time_accelerometer_x = gettimefromraw(data, date, "accelerometer")
    time_gyroscope_x = gettimefromraw(data, date, "gyroscope")
    time_accelerometer_y = gettimefromraw(data, date, "accelerometer")
    time_gyroscope_y = gettimefromraw(data, date, "gyroscope")
    time_accelerometer_z = gettimefromraw(data, date, "accelerometer")
    time_gyroscope_z = gettimefromraw(data, date, "gyroscope")

    return time_accelerometer_x, time_gyroscope_x, time_accelerometer_y, \
           time_gyroscope_y, time_accelerometer_z, time_gyroscope_z


def printstatistics(data_accelerometer_x, data_gyroscope_x, data_accelerometer_y, data_gyroscope_y,
                    data_accelerometer_z, data_gyroscope_z):
    # Averages
    ave_accelerometer_x = average(data_accelerometer_x)
    ave_gyroscope_x = average(data_gyroscope_x)
    ave_accelerometer_y = average(data_accelerometer_y)
    ave_gyroscope_y = average(data_gyroscope_y)
    ave_accelerometer_z = average(data_accelerometer_z)
    ave_gyroscope_z = average(data_gyroscope_z)

    print("#####      Average       #####")
    print("Average for accelerometer x value: " + str(ave_accelerometer_x))
    print("Average for gyroscope x value: " + str(ave_gyroscope_x))
    print("Average for accelerometer y value: " + str(ave_accelerometer_y))
    print("Average for gyroscope y value: " + str(ave_gyroscope_y))
    print("Average for accelerometer z value: " + str(ave_accelerometer_z))
    print("Average for gyroscope z value: " + str(ave_gyroscope_z))
    print("")

    # Standard deviations
    standes_accelerometer_x = standarddeviation(data_accelerometer_x)
    standes_gyroscope_x = standarddeviation(data_gyroscope_x)
    standes_accelerometer_y = standarddeviation(data_accelerometer_y)
    standes_gyroscope_y = standarddeviation(data_gyroscope_y)
    standes_accelerometer_z = standarddeviation(data_accelerometer_z)
    standes_gyroscope_z = standarddeviation(data_gyroscope_z)
    print("##### Standard deviation #####")
    print("Standard deviation for accelerometer x value: " + str(standes_accelerometer_x))
    print("Standard deviation for gyroscope x value: " + str(standes_gyroscope_x))
    print("Standard deviation for accelerometer y value: " + str(standes_accelerometer_y))
    print("Standard deviation for gyroscope y value: " + str(standes_gyroscope_y))
    print("Standard deviation for accelerometer z value: " + str(standes_accelerometer_z))
    print("Standard deviation for gyroscope z value: " + str(standes_gyroscope_z))
    print("")


def plotraw(data_accelerometer_x, data_gyroscope_x, data_accelerometer_y, data_gyroscope_y, data_accelerometer_z,
            data_gyroscope_z, time_accelerometer_x, time_gyroscope_x, time_accelerometer_y, time_gyroscope_y,
            time_accelerometer_z, time_gyroscope_z):
    fig = plt.figure()
    accelerometer_x_plot = fig.add_subplot(231)
    gyroscope_x_plot = fig.add_subplot(234)
    accelerometer_y_plot = fig.add_subplot(232)
    gyroscope_y_plot = fig.add_subplot(235)
    accelerometer_z_plot = fig.add_subplot(233)
    gyroscope_z_plot = fig.add_subplot(236)
    accelerometer_x_plot.plot(time_accelerometer_x, data_accelerometer_x)
    accelerometer_x_plot.set_xlabel("Time")
    accelerometer_x_plot.set_ylabel("Accelerometer x")
    gyroscope_x_plot.plot(time_gyroscope_x, data_gyroscope_x)
    gyroscope_x_plot.set_xlabel("Time")
    gyroscope_x_plot.set_ylabel("Gyroscope x")

    accelerometer_y_plot.plot(time_accelerometer_y, data_accelerometer_y)
    accelerometer_y_plot.set_xlabel("Time")
    accelerometer_y_plot.set_ylabel("Accelerometer y")
    gyroscope_y_plot.plot(time_gyroscope_y, data_gyroscope_y)
    gyroscope_y_plot.set_xlabel("Time")
    gyroscope_y_plot.set_ylabel("Gyroscope y")

    accelerometer_z_plot.plot(time_accelerometer_z, data_accelerometer_z)
    accelerometer_z_plot.set_xlabel("Time")
    accelerometer_z_plot.set_ylabel("Accelerometer z")
    gyroscope_z_plot.plot(time_gyroscope_z, data_gyroscope_z)
    gyroscope_z_plot.set_xlabel("Time")
    gyroscope_z_plot.set_ylabel("Gyroscope z")

    plt.show()


def kinematics(t, data_accelerometer_x, data_accelerometer_y, data_accelerometer_z):

    return ax, vx, px, ay, vy, py, az, vz, pz


def attitude(t, data_gyroscope_x, data_gyroscope_y, data_gyroscope_z):

    return dp, dr, dy


def plotkinematics(time_accelerometer_x, time_accelerometer_y, time_accelerometer_z, ax, vx, px, ay, vy, py, az, vz, pz):

    fig = plt.figure()
    a_x_plot = fig.add_subplot(331)
    v_x_plot = fig.add_subplot(334)
    p_x_plot = fig.add_subplot(337)
    a_y_plot = fig.add_subplot(332)
    v_y_plot = fig.add_subplot(335)
    p_y_plot = fig.add_subplot(338)
    a_z_plot = fig.add_subplot(333)
    v_z_plot = fig.add_subplot(336)
    p_z_plot = fig.add_subplot(339)

    accelerometer_x_plot.plot(time_accelerometer_x, data_accelerometer_x)
    accelerometer_x_plot.set_xlabel("Time")
    accelerometer_x_plot.set_ylabel("Accelerometer x")
    gyroscope_x_plot.plot(time_gyroscope_x, data_gyroscope_x)
    gyroscope_x_plot.set_xlabel("Time")
    gyroscope_x_plot.set_ylabel("Gyroscope x")

    accelerometer_y_plot.plot(time_accelerometer_y, data_accelerometer_y)
    accelerometer_y_plot.set_xlabel("Time")
    accelerometer_y_plot.set_ylabel("Accelerometer y")
    gyroscope_y_plot.plot(time_gyroscope_y, data_gyroscope_y)
    gyroscope_y_plot.set_xlabel("Time")
    gyroscope_y_plot.set_ylabel("Gyroscope y")

    accelerometer_z_plot.plot(time_accelerometer_z, data_accelerometer_z)
    accelerometer_z_plot.set_xlabel("Time")
    accelerometer_z_plot.set_ylabel("Accelerometer z")
    gyroscope_z_plot.plot(time_gyroscope_z, data_gyroscope_z)
    gyroscope_z_plot.set_xlabel("Time")
    gyroscope_z_plot.set_ylabel("Gyroscope z")

    plt.show()

def plotattitude(time_gyroscope_x, time_gyroscope_y, time_gyroscope_z, dp, dr, dy):


# ##### Main #####
def main():

    # Configuration
    t = 1/100

    # Retrieve data from raw file

    data_accelerometer_x, data_gyroscope_x, data_accelerometer_y, \
    data_gyroscope_y, data_accelerometer_z, data_gyroscope_z = preparedata()

    time_accelerometer_x, time_gyroscope_x, time_accelerometer_y, \
    time_gyroscope_y, time_accelerometer_z, time_gyroscope_z = preparetimes()

    # Print basic statistics

    printstatistics(data_accelerometer_x, data_gyroscope_x, data_accelerometer_y, data_gyroscope_y,
                    data_accelerometer_z, data_gyroscope_z)

    # Plot raw data

    plotraw(data_accelerometer_x, data_gyroscope_x, data_accelerometer_y, data_gyroscope_y, data_accelerometer_z,
            data_gyroscope_z, time_accelerometer_x, time_gyroscope_x, time_accelerometer_y, time_gyroscope_y,
            time_accelerometer_z, time_gyroscope_z)

    # Calculate kinematics and attitude
    ax, vx, px, ay, vy, py, az, vz, pz = kinematics(t, data_accelerometer_x, data_accelerometer_y, data_accelerometer_z)

    dp, dr, dy = attitude(t, data_gyroscope_x, data_gyroscope_y, data_gyroscope_z)

    # Plot kinematics and attitude
    plotkinematics(time_accelerometer_x, time_accelerometer_y, time_accelerometer_z, ax, vx, px, ay, vy, py, az, vz, pz)
    plotattitude(time_gyroscope_x, time_gyroscope_y, time_gyroscope_z, dp, dr, dy)


if __name__ == "__main__":
    main()
