from fastapi import FastAPI
app = FastAPI()

app.post("/plus")
async def plus_form(num1: int = Form(...), num2: int = Form(...)):
    result = num1 + num2
    return {"msg":f"{num1}+{num2}={result}"}