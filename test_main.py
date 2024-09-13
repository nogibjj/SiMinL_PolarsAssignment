"""
Test goes here

"""

from main import polars_describe, stats, build_chart

csv = "stocks.csv"


def test_general_describe():
    """Function calling general_describe which tests different parts of
    the dataset"""

    # only works for the example_csv link
    median_test, desribe_test = polars_describe(csv)

    # mean
    assert median_test["XOM"][0] == 78.50218963623047
    # standard deviation of XOM
    assert desribe_test[["describe", "XOM"]][3, 1] == 18.900877
    # mean of XOM column
    assert desribe_test[["describe", "XOM"]][2, 1] == 139.345759


if __name__ == "__main__":
    test_general_describe()
    # test_viz_general()
    # test_markdown_file()
