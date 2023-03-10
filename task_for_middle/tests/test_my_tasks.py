from tests.conftest import client
import pytest


@pytest.mark.parametrize(
    "x,y,operation,status_code",
    [
        (10, 0, '/', 422),
        (10, 20, '+', 200),
        (10, 0, '*', 200),
        (30, 20, '-', 200),
    ],
)
def test_task_1(x: int,
                y: int,
                operation: str,
                status_code: int,
):
    response = client.get('/task1', params={
        "x": x,
        "y": y,
        "operation": operation
    })

    assert response.status_code == status_code


@pytest.mark.parametrize(
    "operation_id, result, status_code",
    [
        (1, 30, 200),
        (2, 0, 200),
        (3, 10, 200),
    ],
)
def test_task_2(operation_id: int,
                result: int,
                status_code: int,
):
    response = client.get('/task2', params={
        "operation_id": operation_id
    })

    assert response.status_code == status_code


def test_task_3():
    response = client.get('/task3')


    assert response.json() == [
  "операция = 10 + 20, status = OK",
  "операция = 10 * 0, status = OK",
  "операция = 30 - 20, status = OK"
]

