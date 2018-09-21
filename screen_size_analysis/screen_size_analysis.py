#!/usr/bin/env python3
import matplotlib.pyplot as plt
from matplotlib import colors
import statistics as sts
import math

def unpack_row(row):
    """Generates a tuple of user device attributes

    :param row: String - comma delimited input like DIMENSIONS, DEVICE_TYPE, NUMBER_OF_OCCURRENCES
    :return: Tuple(s) defining width, height, area, aspect ratio
    """
    exploded = row.split(',')
    num_occurences = len(exploded)
    try:
        width, height = tuple([ int(i) for i in exploded[0].split('x') ])
    except ValueError as e:
        #print("Unable to find dimensions from {0}".format(row))
        return None
    
    area = width * height
    aspect = width / height
    device_type = exploded[1]

    # print("Width: {0}, Height: {1}".format(width, height))
    # print("Number of observations: {0}".format(num_occurences))
    # print("Area: {0}, Aspect Ratio: {1}".format(area, aspect))

    # for the number of observations, return a corresponding number of tuples
    flattend_rows = []
    for _ in range(num_occurences):
        flattend_rows.append(tuple([width, height, area, aspect, device_type]))
    return tuple(flattend_rows)

def flatten(source, device_type=None):
    """Compresses a histogram list of user attributes

    :param source: File path of histogram file
    :return: Tuples
    """
    rows = []
    with open(source, "r") as fs:
        for line in fs:
            observations = unpack_row(line)
            if observations != None:
                for o in observations:
                    rows.append(o)
    if device_type == None:
        return rows
    else:
        return [row for row in rows if row[4] == device_type]

def clean_observations(observations):
    """Remove observations below 600x400 resolution

    :param observations:
    :return:
    """
    return [ o for o in observations if o[0] > 600 and o[1] > 400 ]

def get_dimensions(observations):
    """Returns tuples
    """
    widths, heights = [], []
    for o in observations:
        widths.append(o[0])
        heights.append(o[1])
    return(widths,heights)


def get_stats(l):
    """Get a statistics overview of a list of numerical values

    :param list: numerical values
    :return: Dict - statistical metrics of list
    """
    c = list(l)
    c.sort()
    d = {}
    d["stdev"] = math.floor(sts.stdev(c))
    d["mean"] = math.floor(sts.mean(c))
    d["max"] = c[-1]
    d["min"] = c[0]
    d["confidence_1_sigma"] = range(d["mean"] - d["stdev"], d["mean"] + d["stdev"] + 1)
    d["confidence_2_sigma"] = range(d["mean"] - 2 * d["stdev"], d["mean"] + 2 * d["stdev"] + 1)
    return d

def plot_browser_sizes(observations):
    """Generate a plot of all the types browser sizes used

    :param observations: A list of tuples each representing a user browser session
    :return:
    """
    widths, heights = get_dimensions(clean_observations(observations))

    plt.plot(widths, heights, 'ro', markersize=2)
    plt.xlabel("Width")
    plt.ylabel("Height")
    plt.show()

def calc_browser_size_stats(source, device_type='desktop'):
    """Generate statistics about user browser window sizes

    :param collection: numbers
    :param device_type: str
    """
    observations = flatten(source, device_type)
    observations = clean_observations(observations)
    widths, heights = get_dimensions(observations)
    d = {}
    d["population_size"] = min(len(widths), len(heights))
    d["browser_width_stats"] = get_stats(widths)
    d["browser_height_stats"] = get_stats(heights)
    return d

def plot_width_height_distributions(widths, heights):
    fig, axs = plt.subplots(1,2, sharey=True, tight_layout=True)
    num_bins = 60
    axs[0].hist(widths, bins=num_bins)
    axs[1].hist(heights, bins=num_bins)

    plt.show()
