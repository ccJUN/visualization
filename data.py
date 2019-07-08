import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt

def getdata():
    refferer = pd.read_csv('referrer.csv')
    print(refferer)
    return True

def drawechat():
    return True

if __name__=='__main__':
    getdata()
    drawechat()