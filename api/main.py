from fastapi import FastAPI

app = FastAPI()


@app.get("/cafe/sarudahiko")
async def hello():
    sarudahiko = Cafe("sarudahiko", "kanagawa-ken")
    return {"message": sarudahiko.explanation()}


class Cafe:
    def __init__(self, name: str, region: str):
        self.name = name
        self.region = region

    def explanation(self):
        return f"{self.region}に{self.name}があります"
