"""
Test goes here

"""

from main import polars_describe, build_chart, generate_general_markdown

csv = "stocks.csv"


def test_general_describe():
    """Function calling general_describe which tests different parts of
    the dataset"""

    # only works for the example_csv link
    median_test, describe_test = polars_describe(csv)

    # mean
    assert median_test["XOM"][0] == 78.50218963623047
    # standard deviation of XOM
    assert describe_test["XOM"][3] == 14.255035788410192
    # mean of XOM column
    assert describe_test["XOM"][2] == 75.71046022384886


def test_build_chart():
    """Function calling build chart"""
    build_chart(csv)


def test_markdown_file():
    """Function that generates markdown file"""
    build_chart(csv)
    generate_general_markdown(csv)


if __name__ == "__main__":
    test_general_describe()
    test_build_chart()
    test_markdown_file()
