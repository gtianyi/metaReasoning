"""
Plot tools 2D
@author: huiming zhou
"""

import os
import sys
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.abspath(__file__)) +
                "/../../Search_based_Planning/")

from Search_2D import env


class Plotting:
    def __init__(self, problemFile):
        self.env = env.Env(problemFile)
        self.xI = self.env.xI
        self.xG = self.env.xG
        self.obs = self.env.obs

    def animation_one(self, path, visited, name):
        self.plot_grid(name)
        plt.pause(15)
        cl = self.color_list_2()
        path_combine = []

        for k in range(len(path)):
            self.plot_visited(visited[k], cl[0])
            plt.pause(0.2)
            self.plot_path(path[k])
            plt.cla()
            self.plot_grid(name, path[k][-1])
            path_combine += path[k]
            self.plot_path(path_combine)
            plt.pause(0.2)
        if self.xI in path_combine:
            path_combine.remove(self.xI)
        self.plot_path(path_combine)
        plt.show()

    def animation_alltheway(self, path, visited, name):
        self.plot_grid(name)
        plt.pause(15)
        cl = self.color_list_2()
        path_combine = []

        for k in range(len(path)):
            self.plot_visited(visited[k], cl[0])
            plt.pause(0.2)
            # self.plot_path(path[k])
            path_combine += path[k]
            self.plot_path(path_combine)
            for i in range(len(path[k])):
                plt.cla()
                self.plot_grid(name, path[k][i])
                self.plot_path(path_combine)
                plt.pause(0.2)
                
            plt.pause(0.2)
        if self.xI in path_combine:
            path_combine.remove(self.xI)
        self.plot_path(path_combine)
        plt.show()

    def animation_deepthinking(self, path, visited, isKeepThinking, name):
        self.plot_grid(name)
        plt.pause(15)
        cl = self.color_list_2()
        path_combine = []

        keepThinkingVisitied = []
        for k in range(len(path)):
            # print("k", k)
            self.plot_visited(visited[k], cl[0])
            plt.pause(0.2)
            # self.plot_path(path[k])
            path_combine += path[k]
            self.plot_path(path_combine)
            plt.cla()
            self.plot_grid(name, path[k][-1])
            self.plot_path(path_combine)

            if not isKeepThinking[k]:
                keepThinkingVisitied=list(visited[k])
            else:
                keepThinkingVisitied+=visited[k]
                self.plot_visited(keepThinkingVisitied, cl[2], 0.00001)

            plt.pause(0.2)
            

        if self.xI in path_combine:
            path_combine.remove(self.xI)
        self.plot_path(path_combine)
        plt.show()



    def plot_grid(self, name, newStart = []):
        obs_x = [x[0] for x in self.obs]
        obs_y = [x[1] for x in self.obs]
        
        if newStart:
            plt.plot(newStart[0], newStart[1], "bs")
        else:
            plt.plot(self.xI[0], self.xI[1], "bs")

        plt.plot(self.xG[0], self.xG[1], "gs")
        plt.plot(obs_x, obs_y, "sk")
        plt.title(name)
        plt.axis("equal")

    def plot_visited(self, visited, cl='gray', pauseDuration=0.001):
        if self.xI in visited:
            visited.remove(self.xI)

        if self.xG in visited:
            visited.remove(self.xG)

        count = 0

        for x in visited:
            count += 1
            plt.plot(x[0], x[1], color=cl, marker='o')
            plt.gcf().canvas.mpl_connect('key_release_event',
                                         lambda event: [exit(0) if event.key == 'escape' else None])

            if count < len(visited) / 3:
                length = 20
            elif count < len(visited) * 2 / 3:
                length = 30
            else:
                length = 40
            #
            # length = 15

            if count % length == 0:
                plt.pause(pauseDuration)
        plt.pause(pauseDuration * 10)

    def plot_path(self, path, cl='r', flag=False):
        path_x = [path[i][0] for i in range(len(path))]
        path_y = [path[i][1] for i in range(len(path))]

        if not flag:
            plt.plot(path_x, path_y, linewidth='3', color='r')
        else:
            plt.plot(path_x, path_y, linewidth='3', color=cl)

        plt.plot(self.xI[0], self.xI[1], "bs")
        plt.plot(self.xG[0], self.xG[1], "gs")

        plt.pause(0.01)

    @staticmethod
    def color_list():
        cl_v = ['silver',
                'wheat',
                'lightskyblue',
                'royalblue',
                'slategray']
        cl_p = ['gray',
                'orange',
                'deepskyblue',
                'red',
                'm']
        return cl_v, cl_p

    @staticmethod
    def color_list_2():
        cl = ['silver',
              'steelblue',
              'dimgray',
              'cornflowerblue',
              'dodgerblue',
              'royalblue',
              'plum',
              'mediumslateblue',
              'mediumpurple',
              'blueviolet',
              ]
        return cl
