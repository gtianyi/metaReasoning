"""
LRTA_star 2D (Learning Real-time A*)
@author: huiming zhou
"""

import os
import sys
import copy
import math
import json

sys.path.append(os.path.dirname(os.path.abspath(__file__)) +
                "/../../Search_based_Planning/")

from Search_2D import queue, plotting, env

def parseVisFile(file):
    paths = []
    visited = []
    with open(file) as json_data:
        result = json.load(json_data)
        paths = result["path"]
        visited = result["visited"]

    resultPaths= []
    resultVisitied= []

    for path in paths:
        path = [(int(point.split()[0]), int(point.split()[1]))
                for point in path]
        resultPaths.append(path)

    for pointList in visited:
        pointList = [(int(point.split()[0]), int(point.split()[1]))
                     for point in pointList]
        resultVisitied.append(pointList)

    return resultPaths, resultVisitied


def main():

    problemFile = '/home/aifs1/gu/phd/research/workingPaper/realtime-nancy/worlds/gridPathfinding/exampleworlds/small-3.gp'
    # resultVisFile = '/home/aifs1/gu/phd/research/workingPaper/metareasoning/build_debug/onecommitvis.s3.json'
    # resultVisFile = '/home/aifs1/gu/phd/research/workingPaper/metareasoning/build_debug/lsslrtavis.s3.json'
    resultVisFile = '/home/aifs1/gu/phd/research/workingPaper/metareasoning/build_debug/vistest.json'

    # system.run('cpp executable -vis resultvisfile < input')

    plot = plotting.Plotting(problemFile)

    path, visited = parseVisFile(resultVisFile)

    print("path", path)
    print("visited", visited)

    # plot.animation_one(path, visited, "Fixed Strategy: Commit One")
    plot.animation_alltheway(path, visited, "Fixed Strategy: Commit All")


if __name__ == '__main__':
    main()
