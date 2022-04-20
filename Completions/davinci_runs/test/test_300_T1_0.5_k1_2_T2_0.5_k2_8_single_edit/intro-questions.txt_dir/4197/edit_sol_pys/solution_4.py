# coding: utf-8

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
import matplotlib.ticker as ticker
import matplotlib.font_manager as fm

# グラフに日本語を使うための設定
fp = fm.FontProperties(fname='/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc')

def draw_bar_chart(data, title, xlabel, ylabel, x_min, x_max, y_min, y_max, xticks, yticks, save_name):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(data[0], data[1], width=0.5)
    ax.set_title(title, fontproperties=fp)
    ax.set_xlabel(xlabel, fontproperties=fp)
    ax.set_ylabel(ylabel, fontproperties=fp)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    plt.savefig(save_name, bbox_inches="tight")
    plt.show()

def draw_histogram(data, title, xlabel, ylabel, x_min, x_max, y_min, y_max, xticks, yticks, save_name):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(data, bins=100, range=(0, 100))
    ax.set_title(title, fontproperties=fp)
    ax.set_xlabel(xlabel, fontproperties=fp)
    ax.set_ylabel(ylabel, fontproperties=fp)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    plt.savefig(save_name, bbox_inches="tight")
    plt.show()

def draw_scatter_plot(data, title, xlabel, ylabel, x_min, x_max, y_min, y_max, xticks, yticks, save_name):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(data[0], data[1])
    ax.set_title(title, fontproperties=fp)
    ax.set_xlabel(xlabel, fontproperties=fp)
    ax.set_ylabel(ylabel, fontproperties=fp)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    plt.savefig(save_name, bbox_inches="tight")
    plt.show()

def draw_contour_plot(data, title, xlabel, ylabel, x_min, x_max, y_min, y_max, xticks, yticks, save_name):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.contour(data[0], data[1], data[2])
    ax.set_title(title, fontproperties=fp)
    ax.set_xlabel(xlabel, fontproperties=fp)
    ax.set_ylabel(ylabel, fontproperties=fp)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    plt.savefig(save_name, bbox_inches="tight")
    plt.show()

def draw_heat_map(data, title, xlabel, ylabel, x_min, x_max, y_min, y_max, xticks, yticks, save_name):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.imshow(data, cmap=cm.jet)
    ax.set_title(title, fontproperties=fp)
    ax.set_xlabel(xlabel, fontproperties=fp)
    ax.set_ylabel(ylabel, fontproperties=fp)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    plt.savefig(save_name, bbox_inches="tight")
    plt.show()

def draw_3d_plot(data, title, xlabel, ylabel, x_min, x_max, y_min, y_max, xticks, yticks, save_name):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(data[0], data[1], data[2], rstride=1, cstride=1, cmap=cm.jet)
    ax.set_title(title, fontproperties=fp)
    ax.set_xlabel(xlabel, fontproperties=fp)
    ax.set_ylabel(ylabel, fontproperties=fp)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    plt.savefig(save_name, bbox_inches="tight")
    plt.show()

def draw_heat_map_2(data, title, xlabel, ylabel, x_min, x_max, y_min, y_max, xticks, yticks, save_name):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.imshow(data, cmap=cm.jet)
    ax.set_title(title, fontproperties=fp)
    ax.set_xlabel(xlabel, fontproperties=fp)
    ax.set_ylabel(ylabel, fontproperties=fp)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    plt.savefig(save_name, bbox_inches="tight")
    plt.show()

def draw_bar_chart_2(data, title, xlabel, ylabel, x_min, x_max, y_min, y_max, xticks, yticks, save_name):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(data[0], data[1], width=0.5)
    ax.set_title(title, fontproperties=fp)
    ax.set_xlabel(xlabel, fontproperties=fp)
    ax.set_ylabel(ylabel, fontproperties=fp)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    plt.savefig(save_name, bbox_inches="tight")
    pl


N = int(input())
A = [int(i) for i in input().split()]

for i in range(N):
    print(A.index(i+1)+1, end=' ')
