"""
LRTA_star 2D (Learning Real-time A*)
@author: huiming zhou
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) +
                "/../../Search_based_Planning/")


from Search_2D import queue, plotting, env
import copy
import math
import json


def parseVisFile(file):
    paths = []
    visited = []
    with open(file) as json_data:
        result = json.load(json_data)
        paths = result["path"]
        visited = result["visited"]
        isKeepThinking = result["isKeepThinking"]
        committed = result["committed"]

    resultPaths = []
    resultVisitied = []
    resultCommitted = []

    for path in paths:
        path = [(int(point.split()[0]), int(point.split()[1]))
                for point in path]
        resultPaths.append(path)

    for pointList in visited:
        pointList = [(int(point.split()[0]), int(point.split()[1]))
                     for point in pointList]
        resultVisitied.append(pointList)

    for pointList in committed:
        pointList = [(int(point.split()[0]), int(point.split()[1]))
                     for point in pointList]
        resultCommitted.append(pointList)

    return resultPaths, resultVisitied, isKeepThinking, resultCommitted


def main():

    problemFile = '/home/aifs1/gu/phd/research/workingPaper/realtime-nancy/worlds/gridPathfinding/exampleworlds/small-3.gp'
    # resultVisFile = '/home/aifs1/gu/phd/research/workingPaper/metareasoning/build_debug/onecommitvis.s3.json'
    # resultVisFile = '/home/aifs1/gu/phd/research/workingPaper/metareasoning/build_debug/lsslrtavis.s3.json'
    resultVisFile = '/home/aifs1/gu/phd/research/workingPaper/metareasoning/build_debug/dtrts.small-3.json'

    # problemFile = '/home/aifs1/gu/phd/research/workingPaper/realtime-nancy/worlds/gridPathfinding/exampleworlds/small-2.gp'
    # resultVisFile = '/home/aifs1/gu/phd/research/workingPaper/metareasoning/build_debug/onecommitvis.s2.json'
    # resultVisFile = '/home/aifs1/gu/phd/research/workingPaper/metareasoning/build_debug/allthewaycommitvis.s2.json'
    # resultVisFile = '/home/aifs1/gu/phd/research/workingPaper/metareasoning/build_debug/vistest.json'

    # system.run('cpp executable -vis resultvisfile < input')

    plot = plotting.Plotting(problemFile)

    path, visited, isKeepThinking, committed = parseVisFile(resultVisFile)

    print("path", path)
    print("visited", visited)
    print("isKeepThinking", isKeepThinking)
    print("committed", committed)

    # plot.animation_one(path, visited, "Fixed Strategy: Commit One")
    # plot.animation_alltheway(path, visited, "Fixed Strategy: Commit All")
    plot.animation_deepthinking(path, visited, isKeepThinking, committed, "Our Approach")


if __name__ == '__main__':
    main()
