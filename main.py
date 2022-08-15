from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/nsfw_trap/")
async def trap():
    return { 'url' : requests.get("https://api.waifu.pics/nsfw/trap").json().get("url") }

@app.get("/is/{stuff}/{value}")
async def checker(stuff:str, value : str):
    answer = "idk"
    if stuff == "13":
        answer = (value == "thirteen") | (value == "13")
    elif stuff == "highright":
        yes = ["genius", "handsome"]
        no = ["stupid", "ugly"]
        if value in yes:
            answer = True
        if value in no:
            answer = False
    elif stuff == "r2turntrue":
        answer = (value == "ugly")

    if answer.__str__() == "True":
        answer = "yes"
    elif not answer:
        answer = "no"
    return { f"is {stuff} {value}": answer }

@app.get("/stupid_machine")
async def stupid_machine():
    return { '1.1 + 0.1 == 1.2' : 1.1 + 0.1 == 1.2 }