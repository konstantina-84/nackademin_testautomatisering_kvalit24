import main


def test_sum_two_positives():
    # Arrange
    possitive_value_1 = 1
    possitive_value_2 = 4
    expected_result = {"result": 5}

    # Act
    result = main.addition(possitive_value_1, possitive_value_2)

    # Assert
    assert result == expected_result


# Lab tasks

## Complete the following tests


def test_sum_one_positive_one_negative():
    positive_value_1 = 5
    negative_value_2 = -6
    expected_result = {"result": -1}

    # Act
    result = main.addition(positive_value_1, negative_value_2)

    #     Assert
    assert result == expected_result


def test_sum_one_positive_one_string_value():
    positive_value = 6
    string_value = "hi"

    try:
        result = main.addition(positive_value, string_value)
    except TypeError:
        assert True
    else:
        assert False, "Expected TypeError but none was raised"


def test_divide_two_positive_values():
    positive_value_1 = 9
    positive_value_2 = 3
    expected_result = {"result": 3}

    # Act
    result = main.division(positive_value_1, positive_value_2)

    # Assert
    assert result == expected_result


def test_divide_by_zero():
    positive_value = 4
    zero_value = 0

    try:
        result = main.division(positive_value, zero_value)
    except ZeroDivisionError:
        assert True
    else:
        assert False, "Expected ZeroDivisionError but none was raised"
