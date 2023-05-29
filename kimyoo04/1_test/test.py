import pandas
import numpy
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms

# 1. 데이터 불러오기
df = pandas.read_csv('data/Advertising.csv', index_col=0)
print(df.head())
print(df.tail())
print(df.shape)
