import requests

BASE_URL = "http://127.0.0.1:8000"


def test_addition():
    # Arrange
    possitive_value = 5
    negative_value = -6
    url_params = {"a": possitive_value, "b": negative_value}
    expected_result = {"result": -1}

    # Act
    response = requests.get(f"{BASE_URL}/addition", params=url_params)

    # Assert
    assert response.json() == expected_result


# Lab tasks

## Complete the following tests


def test_addition_with_string_value():
    positive_value = 6
    string_value = "hi"
    url_params = {"a": positive_value, "b": string_value}

    # Act
    response = requests.get(f"{BASE_URL}/addition", params=url_params)

    # Assert
    assert response.status_code == 422


def test_sum_one_positive_one_negative():
    possitive_value = 5
    negative_value = -6
    url_params = {"a": possitive_value, "b": negative_value}
    expected_result = {"result": -1}

    # Act
    response = requests.get(f"{BASE_URL}/addition", params=url_params)

    # Assert
    assert response.status_code == 200
    assert response.json() == expected_result


def test_divide_two_positive_values():
    positive_value_1 = 9
    positive_value_2 = 3
    url_params = {"a": positive_value_1, "b": positive_value_2}
    expected_result = {"result": 3}

    # Act
    response = requests.get(f"{BASE_URL}/division", params=url_params)

    # Assert
    assert response.status_code == 200
    assert response.json() == expected_result


def test_divide_by_zero():
    positive_value = 4
    zero_value = 0
    url_params = {"a": positive_value, "b": zero_value}

    response = requests.get(f"{BASE_URL}/division", params=url_params)

    assert response.status_code == 500
