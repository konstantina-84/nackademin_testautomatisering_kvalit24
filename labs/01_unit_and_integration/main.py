from fastapi import FastAPI

app = FastAPI()

"I love python 1 2 3"


def format_response(data):
    return {"result": data}


@app.get("/addition")
def addition(a: int, b: int):
    response_int = a + b
    response_object = format_response(response_int)
    return response_object


@app.get("/substraction")
def substraction(a: int, b: int):
    response_int = a - b
    response_object = format_response(response_int)
    return response_object


@app.get("/multiplication")
def multiplication(a: int, b: int):
    response_int = a * b
    response_object = format_response(response_int)
    return response_object


@app.get("/division")
def division(a: int, b: int):
    response_int = a / b
    response_object = format_response(response_int)
    return response_object
