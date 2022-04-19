#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 15:05:51 2017


@author: shirleydeng
"""

import random
import numpy as np
import matplotlib.pyplot as plt

def generate_random(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.randint(1,100))
    return list

def generate_random_normal(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.gauss(0,1))
    return list

def generate_random_exponential(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.expovariate(1))
    return list

def generate_random_poisson(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.poisson(1))
    return list

def generate_random_uniform(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.uniform(0,1))
    return list

def generate_random_binomial(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.binomial(100,0.5))
    return list

def generate_random_geometric(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.geometric(0.5))
    return list

def generate_random_chisquare(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.chisquare(1))
    return list

def generate_random_triangular(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.triangular(0,1,0.5))
    return list

def generate_random_paretovariate(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.paretovariate(1))
    return list

def generate_random_weibullvariate(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.weibullvariate(1,1))
    return list

def generate_random_lognormvariate(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.lognormvariate(0,1))
    return list

def generate_random_betavariate(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.betavariate(1,1))
    return list

def generate_random_vonmisesvariate(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.vonmisesvariate(0,1))
    return list

def generate_random_gammavariate(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.gammavariate(1,1))
    return list

def generate_random_gauss(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.gauss(0,1))
    return list

def generate_random_hypergeometric(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.hypergeometric(100,1,1))
    return list

def generate_random_logisticvariate(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.logisticvariate(1,1))
    return list

def generate_random_normalvariate(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.normalvariate(0,1))
    return list

def generate_random_fvariate(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.fvariate(1,1))
    return list

def generate_random_cunifvariate(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.cunifvariate(1,1))
    return list

def generate_random_scalar(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.random())
    return list

def generate_random_seed(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.seed(1))
    return list

def generate_random_getstate(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.getstate())
    return list

def generate_random_setstate(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.setstate())
    return list

def generate_random_choice(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.choice([1,2,3,4]))
    return list

def generate_random_shuffle(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.shuffle([1,2,3,4]))
    return list

def generate_random_sample(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.sample([1,2,3,4],1))
    return list

def generate_random_randrange(n):
    random.seed(1)
    list = []
    for i in range(n):
        list.append(random.randrange(1,100,1
