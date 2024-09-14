"""
Python script using Pandas for descriptive statistics
Read a dataset (CSV or Excel)
Generate summary statistics (mean, median, standard deviation)
Create at least one data visualization
Deliverable:
Python script
Generated summary report (PDF or markdown)"""

import matplotlib.pyplot as plt
import pandas as pd
import polars as pl
from ydata_profiling import ProfileReport


def polars_describe(csv):
    """polars describe function in csv"""
    polars_df = pl.read_csv(csv)
    return polars_df.median(), polars_df.describe()


def pandas_describe(csv):
    """pandas Describe function in csv"""
    pandas_df = pd.read_csv(csv)
    return pandas_df.describe()


def polars_profilesummary(csv):
    """general describe function in csv"""
    polars_df = pl.scan_csv(csv)
    polars_df = polars_df.collect()
    profile = ProfileReport(polars_df.to_pandas(), title="Profiling Report")
    profile.to_file("polars.html")


def stats(csv):
    """Calculating relevant stats"""
    data_frame = pd.read_csv(csv)
    ror = data_frame.pct_change() * 100
    mean = ror.mean()
    median = ror.median()
    standard_deviation = ror.std()
    print(mean, median, standard_deviation)


def build_chart(csv):
    "visualisation of mean return vs risk"
    data_frame = pd.read_csv(csv)
    ror = data_frame.pct_change() * 100
    mean = ror.mean()
    standard_deviation = ror.std()
    plt.scatter(standard_deviation, mean, s=data_frame.mean(), alpha=0.4)
    plt.title("Mean Return vs Risk", fontsize=10, fontweight="bold")
    plt.xlabel("Risk (standard deviation)", fontsize=10)
    plt.ylabel("Mean Return", fontsize=10)
    plt.grid()
    plt.savefig("chart.png")


def generate_general_markdown(csv):
    """generate an md file with outputs"""
    markdown_table1, markdown_table2 = polars_describe(csv)
    markdown_table1 = str(markdown_table1)
    markdown_table2 = str(markdown_table2)

    # Write the markdown table to a file
    with open("stocks.md", "w", encoding="utf-8") as file:
        file.write("Median:\n")
        file.write(markdown_table1)
        file.write("\n\n")  # Add a new line
        file.write("Descriptive Statistics:\n")
        file.write(markdown_table2)
        file.write("\n\n")  # Add a new line
        file.write(
            "![StocksChart](chart.png)\n"
        )  # Embeds an image with alternative text Stocks Chart


def generate_summary(csv):
    """generates report of any dataset"""
    general_df = pd.read_csv(csv)
    profile = ProfileReport(general_df, title="Profiling Report")
    profile.to_file("profile.html")
