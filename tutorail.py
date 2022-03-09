from fastapi import FastAPI

app=FastAPI()



@app.get("/shikha")
def Func():
    return {"message":"welocome"}

