import json
from starlette.responses import Response
from fastapi import APIRouter

router = APIRouter()

data = {
    "list_of_operations": [

    ]
}


def create_json():
    with open('new_file.json', 'w') as f:
        json.dump(data, f, indent=4)


@router.get("/task1")
async def task1(x: int, y: int, operation: str):
    if y == 0 and operation == '/':
        return Response("ZeroDivisionError", status_code=422)
    else:
        if operation in ['+', "/", "*", "-"]:
            new_data = {"x": x,
                        "y": y,
                        "operation": operation,
                        "status": "waiting"
                        }
            try:
                with open('new_file.json', "r+") as file:
                    file_data = json.load(file)
                    file_data["list_of_operations"].append(new_data)
                    file.seek(0)
                    json.dump(file_data, file, indent=4)
            except FileNotFoundError:
                create_json()
                with open('new_file.json', "r+") as file:
                    file_data = json.load(file)
                    file_data["list_of_operations"].append(new_data)
                    file.seek(0)
                    json.dump(file_data, file, indent=4)

        else:
            return "Введите операцию над числами"

    with open('new_file.json', 'r+') as file:
        file_data = json.load(file)
        id_oper = len(file_data['list_of_operations'])
    return f"Id операции = {id_oper}"


@router.get('/task2')
async def task2(operation_id: int):
    with open('new_file.json') as f:
        data = json.load(f)
    data['list_of_operations'][operation_id - 1]["status"] = 'OK'
    try:
        if data['list_of_operations'][operation_id - 1]["operation"] == '+':
            ans = data['list_of_operations'][operation_id - 1]['x'] + data['list_of_operations'][operation_id - 1]['y']
        elif data['list_of_operations'][operation_id - 1]["operation"] == '-':
            ans = data['list_of_operations'][operation_id - 1]['x'] - data['list_of_operations'][operation_id - 1]['y']
        elif data['list_of_operations'][operation_id - 1]["operation"] == '*':
            ans = data['list_of_operations'][operation_id - 1]['x'] * data['list_of_operations'][operation_id - 1]['y']
        else:
            ans = data['list_of_operations'][operation_id - 1]['x'] / data['list_of_operations'][operation_id - 1]['y']

    except ZeroDivisionError:
        data['list_of_operations'][operation_id - 1]["status"] = 'ZeroDivisionError'
        ans = "Делить на ноль нельзя!"

    with open('new_file.json', "wt") as f:
        json.dump(data, f, indent=4)
    return ans



@router.get('/task3')
async def task3():
    with open('new_file.json', 'r+') as file:
        file_data = json.load(file)
        ans = []
        for data in file_data['list_of_operations']:
            ans.append(f"операция = {data['x']} {data['operation']} {data['y']}, status = {data['status']}")
        return ans
