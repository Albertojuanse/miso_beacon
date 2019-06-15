from miso_beacon_analysis.calculate_statistics import getdatafromraw, gettimefromraw, average, standarddeviation, readjson, plothistogram, plotsignal
import json
import os
import sys
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from numpy import linspace


# ##### Raw data extracting and plotting #####
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


def kinematics(t, g, data_accelerometer_x, data_accelerometer_y, data_accelerometer_z):

    ax, vx, px = [], [], []
    ay, vy, py = [], [], []
    az, vz, pz = [], [], []

    ax_inst, vx_inst, px_inst = 0, 0, 0
    ay_inst, vy_inst, py_inst = 0, 0, 0
    az_inst, vz_inst, pz_inst = 0, 0, 0

    for item in data_accelerometer_x:
        ax_inst += item * g
        ax.append(ax_inst)
        vx_inst -= ax_inst * t
        vx.append(vx_inst)
        px_inst += (1.0 / 2.0) * vx_inst * t
        px.append(px_inst)

    for item in data_accelerometer_y:
        ay_inst += item * g
        ay.append(ay_inst)
        vy_inst -= ay_inst * t
        vy.append(vy_inst)
        py_inst += (1.0 / 2.0) * vy_inst * t
        py.append(py_inst)

    for item in data_accelerometer_z:
        az_inst += item * g
        az.append(az_inst)
        vz_inst -= az_inst * t
        vz.append(vz_inst)
        pz_inst += (1.0 / 2.0) * vz_inst * t
        pz.append(pz_inst)

    return ax, vx, px, ay, vy, py, az, vz, pz


def attitude(t, data_gyroscope_x, data_gyroscope_y, data_gyroscope_z):

    dp, dr, dy = [], [], []
    dp_inst, dr_inst, dy_inst = 0, 0, 0

    for item in data_gyroscope_x:
        dp_inst += item * t
        dp.append(dp_inst)

    for item in data_gyroscope_y:
        dr_inst += item * t
        dr.append(dr_inst)

    for item in data_gyroscope_z:
        dy_inst += item * t
        dy.append(dy_inst)

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

    a_x_plot.plot(time_accelerometer_x, ax)
    a_x_plot.set_xlabel("Time")
    a_x_plot.set_ylabel("Acceleration x")
    v_x_plot.plot(time_accelerometer_x, vx)
    v_x_plot.set_xlabel("Time")
    v_x_plot.set_ylabel("Velocity x")
    p_x_plot.plot(time_accelerometer_x, px)
    p_x_plot.set_xlabel("Time")
    p_x_plot.set_ylabel("Position x")

    a_y_plot.plot(time_accelerometer_y, ay)
    a_y_plot.set_xlabel("Time")
    a_y_plot.set_ylabel("Acceleration y")
    v_y_plot.plot(time_accelerometer_y, vy)
    v_y_plot.set_xlabel("Time")
    v_y_plot.set_ylabel("Velocity y")
    p_y_plot.plot(time_accelerometer_y, py)
    p_y_plot.set_xlabel("Time")
    p_y_plot.set_ylabel("Position y")

    a_z_plot.plot(time_accelerometer_z, az)
    a_z_plot.set_xlabel("Time")
    a_z_plot.set_ylabel("Acceleration z")
    v_z_plot.plot(time_accelerometer_z, vz)
    v_z_plot.set_xlabel("Time")
    v_z_plot.set_ylabel("Velocity x")
    p_z_plot.plot(time_accelerometer_z, pz)
    p_z_plot.set_xlabel("Time")
    p_z_plot.set_ylabel("Position z")

    plt.show()


def plotattitude(time_gyroscope_x, time_gyroscope_y, time_gyroscope_z, dp, dr, dy):

    fig = plt.figure()
    dp_plot = fig.add_subplot(311)
    dr_plot = fig.add_subplot(312)
    dy_plot = fig.add_subplot(313)

    dp_plot.plot(time_gyroscope_x, dp)
    dp_plot.set_xlabel("Time")
    dp_plot.set_ylabel("Pitch around x axis")
    dr_plot.plot(time_gyroscope_y, dr)
    dr_plot.set_xlabel("Time")
    dr_plot.set_ylabel("Roll around y axis")
    dy_plot.plot(time_gyroscope_z, dy)
    dy_plot.set_xlabel("Time")
    dy_plot.set_ylabel("Yaw around z axis")

    plt.show()


def plotpath(px, py, pz):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(px, py, pz)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()


# ##### White noise analysis #####
def noiseanalysis(amplitudethreshold, data_accelerometer_x, data_gyroscope_x, data_accelerometer_y,
                  data_gyroscope_y, data_accelerometer_z, data_gyroscope_z):

    fig = plt.figure()

    accelerometer_x_index = 1
    accelerometer_x_sum = 0
    accelerometer_x_ave = 0
    accelerometer_x_noise = []
    for item in data_accelerometer_x:

        if abs(accelerometer_x_ave - item) > amplitudethreshold:
            break

        if item != 0:
            accelerometer_x_sum += item
            accelerometer_x_ave = accelerometer_x_sum / accelerometer_x_index
            accelerometer_x_noise.append(item)

        accelerometer_x_index += 1

    accelerometer_x_standarddeviation = standarddeviation(accelerometer_x_noise)

    accelerometer_x_plot = fig.add_subplot(321)
    accelerometer_x_plot.hist(accelerometer_x_noise, bins=500)
    accelerometer_x_plot.axvline(x=accelerometer_x_ave, color='k', linestyle='--')
    accelerometer_x_plot.axvline(x=(accelerometer_x_ave+accelerometer_x_standarddeviation), color='r', linestyle='--')
    accelerometer_x_plot.axvline(x=(accelerometer_x_ave-accelerometer_x_standarddeviation), color='r', linestyle='--')
    accelerometer_x_plot.set_ylabel("Initial Noise of x accelerometer")
    accelerometer_x_plot.set_xlabel("Deviation")

    accelerometer_y_index = 1
    accelerometer_y_sum = 0
    accelerometer_y_ave = 0
    accelerometer_y_noise = []
    for item in data_accelerometer_y:

        if abs(accelerometer_y_ave - item) > amplitudethreshold:
            break

        if item != 0:
            accelerometer_y_sum += item
            accelerometer_y_ave = accelerometer_y_sum / accelerometer_y_index
            accelerometer_y_noise.append(item)

        accelerometer_y_index += 1

    accelerometer_y_standarddeviation = standarddeviation(accelerometer_y_noise)

    accelerometer_y_plot = fig.add_subplot(323)
    accelerometer_y_plot.hist(accelerometer_y_noise, bins=500)
    accelerometer_y_plot.axvline(x=accelerometer_y_ave, color='k', linestyle='--')
    accelerometer_y_plot.axvline(x=(accelerometer_y_ave+accelerometer_y_standarddeviation), color='r', linestyle='--')
    accelerometer_y_plot.axvline(x=(accelerometer_y_ave-accelerometer_y_standarddeviation), color='r', linestyle='--')
    accelerometer_y_plot.set_ylabel("Initial Noise of y accelerometer")
    accelerometer_y_plot.set_xlabel("Deviation")

    accelerometer_z_index = 1
    accelerometer_z_sum = 0
    accelerometer_z_ave = 0
    accelerometer_z_noise = []
    for item in data_accelerometer_z:

        if abs(accelerometer_z_ave - item) > amplitudethreshold:
            break

        accelerometer_z_sum += item
        accelerometer_z_ave = accelerometer_z_sum / accelerometer_z_index
        accelerometer_z_noise.append(item)

        accelerometer_z_index += 1

    accelerometer_z_standarddeviation = standarddeviation(accelerometer_z_noise)

    accelerometer_z_plot = fig.add_subplot(325)
    accelerometer_z_plot.hist(accelerometer_z_noise, bins=500)
    accelerometer_z_plot.axvline(x=accelerometer_z_ave, color='k', linestyle='--')
    accelerometer_z_plot.axvline(x=(accelerometer_z_ave+accelerometer_z_standarddeviation), color='r', linestyle='--')
    accelerometer_z_plot.axvline(x=(accelerometer_z_ave-accelerometer_z_standarddeviation), color='r', linestyle='--')
    accelerometer_z_plot.set_ylabel("Initial Noise of z accelerometer")
    accelerometer_z_plot.set_xlabel("Deviation")

    gyroscope_x_index = 1
    gyroscope_x_sum = 0
    gyroscope_x_ave = 0
    gyroscope_x_noise = []
    for item in data_gyroscope_x:

        if abs(gyroscope_x_ave - item) > 2*amplitudethreshold:
            break

        if item != 0:
            gyroscope_x_sum += item
            gyroscope_x_ave = gyroscope_x_sum / gyroscope_x_index
            gyroscope_x_noise.append(item)

        gyroscope_x_index += 1

    gyroscope_x_standarddeviation = standarddeviation(gyroscope_x_noise)

    gyroscope_x_plot = fig.add_subplot(322)
    gyroscope_x_plot.hist(gyroscope_x_noise, bins=500)
    gyroscope_x_plot.axvline(x=gyroscope_x_ave, color='k', linestyle='--')
    gyroscope_x_plot.axvline(x=(gyroscope_x_ave+gyroscope_x_standarddeviation), color='r', linestyle='--')
    gyroscope_x_plot.axvline(x=(gyroscope_x_ave-gyroscope_x_standarddeviation), color='r', linestyle='--')
    gyroscope_x_plot.set_ylabel("Initial Noise of x gyroscope")
    gyroscope_x_plot.set_xlabel("Deviation")

    gyroscope_y_index = 1
    gyroscope_y_sum = 0
    gyroscope_y_ave = 0
    gyroscope_y_noise = []
    for item in data_gyroscope_y:

        if abs(gyroscope_y_ave - item) > 2*amplitudethreshold:
            break

        if item != 0:
            gyroscope_y_sum += item
            gyroscope_y_ave = gyroscope_y_sum / gyroscope_y_index
            gyroscope_y_noise.append(item)

        gyroscope_y_index += 1

    gyroscope_y_standarddeviation = standarddeviation(gyroscope_y_noise)

    gyroscope_y_plot = fig.add_subplot(324)
    gyroscope_y_plot.hist(gyroscope_y_noise, bins=500)
    gyroscope_y_plot.axvline(x=gyroscope_y_ave, color='k', linestyle='--')
    gyroscope_y_plot.axvline(x=(gyroscope_y_ave+gyroscope_y_standarddeviation), color='r', linestyle='--')
    gyroscope_y_plot.axvline(x=(gyroscope_y_ave-gyroscope_y_standarddeviation), color='r', linestyle='--')
    gyroscope_y_plot.set_ylabel("Initial Noise of y gyroscope")
    gyroscope_y_plot.set_xlabel("Deviation")

    gyroscope_z_index = 1
    gyroscope_z_sum = 0
    gyroscope_z_ave = 0
    gyroscope_z_noise = []
    for item in data_gyroscope_z:

        if abs(gyroscope_z_ave - item) > 2*amplitudethreshold:
            break

        if item != 0:
            gyroscope_z_sum += item
            gyroscope_z_ave = gyroscope_z_sum / gyroscope_z_index
            gyroscope_z_noise.append(item)

        gyroscope_z_index += 1

    gyroscope_z_standarddeviation = standarddeviation(gyroscope_z_noise)

    gyroscope_z_plot = fig.add_subplot(326)
    gyroscope_z_plot.hist(gyroscope_z_noise, bins=500)
    gyroscope_z_plot.axvline(x=gyroscope_z_ave, color='k', linestyle='--')
    gyroscope_z_plot.axvline(x=(gyroscope_z_ave+gyroscope_z_standarddeviation), color='r', linestyle='--')
    gyroscope_z_plot.axvline(x=(gyroscope_z_ave-gyroscope_z_standarddeviation), color='r', linestyle='--')
    gyroscope_z_plot.set_ylabel("Initial Noise of z gyroscope")
    gyroscope_z_plot.set_xlabel("Deviation")

    plt.show()


# ##### Main #####
def main():

    # Configuration
    t = 1/100
    g = 9.7994

    # Retrieve data from raw file

    data_accelerometer_x, data_gyroscope_x, data_accelerometer_y, \
    data_gyroscope_y, data_accelerometer_z, data_gyroscope_z = preparedata()

    time_accelerometer_x, time_gyroscope_x, time_accelerometer_y, \
    time_gyroscope_y, time_accelerometer_z, time_gyroscope_z = preparetimes()

    # ##### Raw information #####

    # Print basic statistics

    printstatistics(data_accelerometer_x, data_gyroscope_x, data_accelerometer_y, data_gyroscope_y,
                    data_accelerometer_z, data_gyroscope_z)

    # Plot raw data

    plotraw(data_accelerometer_x, data_gyroscope_x, data_accelerometer_y, data_gyroscope_y, data_accelerometer_z,
            data_gyroscope_z, time_accelerometer_x, time_gyroscope_x, time_accelerometer_y, time_gyroscope_y,
            time_accelerometer_z, time_gyroscope_z)

    # Calculate kinematics and attitude
    ax, vx, px, ay, vy, py, az, vz, pz = kinematics(t, g, data_accelerometer_x, data_accelerometer_y, data_accelerometer_z)

    dp, dr, dy = attitude(t, data_gyroscope_x, data_gyroscope_y, data_gyroscope_z)

    # Plot kinematics and attitude
    plotkinematics(time_accelerometer_x, time_accelerometer_y, time_accelerometer_z, ax, vx, px, ay, vy, py, az, vz, pz)
    plotattitude(time_gyroscope_x, time_gyroscope_y, time_gyroscope_z, dp, dr, dy)
    plotpath(px, py, pz)

    # ##### White noise analysis #####

    # Initial noise is analyzed with as many initial samples as found before a step higher than this amplitude threshold
    amplitudethreshold = 0.04

    noiseanalysis(amplitudethreshold, data_accelerometer_x, data_gyroscope_x, data_accelerometer_y,
                  data_gyroscope_y, data_accelerometer_z, data_gyroscope_z)


if __name__ == "__main__":
    main()
