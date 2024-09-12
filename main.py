"""
Python script using Pandas for descriptive statistics
Read a dataset (CSV or Excel)
Generate summary statistics (mean, median, standard deviation)
Create at least one data visualization
Deliverable:
Python script
Generated summary report (PDF or markdown)"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Read a dataset
stocks = pd.read_csv("stocks.csv")
stocks = pd.DataFrame(stocks)


def description():
    describe = stocks.describe()
    print(describe)
    return describe


description()

ror = stocks.pct_change() * 100
mean = ror.mean()
median = ror.median()
sd = ror.std()


def stats():
    ror = stocks.pct_change() * 100
    mean = ror.mean()
    median = ror.median()
    sd = ror.std()
    print(mean, median, sd)


stats()


def build_chart():
    plt.scatter(sd, mean, s=stocks.mean(), alpha=0.4)
    plt.title("Mean Return vs Risk", fontsize=10, fontweight="bold")
    plt.xlabel("Risk (standard deviation)", fontsize=10)
    plt.ylabel("Mean Return", fontsize=10)
    plt.grid()
    plt.show()
    plt.savefig("Chart.png")
    return


build_chart()
