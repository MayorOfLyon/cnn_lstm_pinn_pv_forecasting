import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import StratifiedKFold
import csv
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
import lightgbm as lgb
from lightgbm import LGBMRegressor
from sklearn.tree import export_graphviz
import graphviz
import sys
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from func import  specialize_2,specialize_3, specialize_4
import time

def specialize(train_list_i, pred_label_final):
    ###specialize_2
    if(train_list[i] == 'train_2.csv'):
        
        pred_label_final = specialize_2(test_old['month'], test_old['hour'], test_old['min'], pred_label_final)
        
    ###specialize_3
    if(train_list[i] == 'train_3.csv'):
        
        pred_label_final = specialize_3(test_old['month'],  test_old['hour'], test_old['min'], pred_label_final)
        
    ###specialize_4
    if(train_list[i] == 'train_4.csv'):
        
        pred_label_final = specialize_4(test_old['month'], test_old['hour'], test_old['min'], pred_label_final)
        
    return pred_label_final