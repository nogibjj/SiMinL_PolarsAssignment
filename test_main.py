"""
Test goes here

"""

from main import description, stats, build_chart


def test_stat():
    result1 = stats()
    assert result1 is not None


def test_description():
    result2 = description()
    assert result2 is None


def test_chart():
    result2 = build_chart()
    assert result2 is None


if __name__ == "__main__":
    test_calculate_stat()
    build_histogram()


def test_markdown_file():
    """Function that generates markdown file"""
    generate_vis_general_polars_congress(example_csv)
    generate_general_markdown(example_csv)


if __name__ == "__main__":
    test_general_describe()
    # test_viz_general()
    # test_markdown_file()
