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
import polars as pl
from ydata_profiling import ProfileReport


def polars_describe(csv):
    """polars describe function in csv"""
    polars_df = pl.read_csv(csv)
    return polars_df.median(), polars_df.describe()


print(polars_describe("stocks.csv"))


def pandas_describe(csv):
    """pandas Describe function in csv"""
    pandas_df = pd.read_csv(csv)
    return pandas_df.describe()


# print(pandas_describe("stocks.csv"))


def polars_profilesummary(csv):
    """general describe function in csv"""
    polars_df = pl.scan_csv(csv)
    profile = ProfileReport(polars_df, title="Profiling Report")
    profile.to_file("polars.html")


polars_profilesummary("stocks.csv")


def stats(csv):
    df = pd.read_csv(csv)
    ror = df.pct_change() * 100
    mean = ror.mean()
    median = ror.median()
    sd = ror.std()
    print(mean, median, sd)


# stats("stocks.csv")


def build_chart(csv):
    "visualisation of mean return vs risk"
    df = pd.read_csv(csv)
    ror = df.pct_change() * 100
    mean = ror.mean()
    median = ror.median()
    sd = ror.std()
    plt.scatter(sd, mean, s=df.mean(), alpha=0.4)
    plt.title("Mean Return vs Risk", fontsize=10, fontweight="bold")
    plt.xlabel("Risk (standard deviation)", fontsize=10)
    plt.ylabel("Mean Return", fontsize=10)
    plt.grid()
    plt.savefig("chart.png")
    return


# build_chart("stocks.csv")


def generate_general_markdown(csv):
    """generate an md file with outputs"""
    markdown_table1, markdown_table2 = polars_describe(csv)
    markdown_table1 = str(markdown_table1)
    markdown_table2 = str(markdown_table2)

    # Write the markdown table to a file
    with open("congress_summary.md", "w", encoding="utf-8") as file:
        file.write("Describe:\n")
        file.write(markdown_table1)
        file.write("\n\n")  # Add a new line
        file.write("Median:\n")
        file.write(markdown_table2)
        file.write("\n\n")  # Add a new line
        file.write("![congress_viz](Chart.png)\n")


def generate_summary(csv):
    """generates report of any dataset"""
    general_df = pd.read_csv(csv)
    profile = ProfileReport(general_df, title="Profiling Report")
    profile.to_file("profile.html")


# generate_summary("stocks.csv")
