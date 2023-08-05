from fastapi import FastAPI

app = FastAPI()


@app.get("/cafe/star-backs")
async def hello():
    star_backs = Cafe("スターバックス", "フラペチーノ")
    return {
        "message": star_backs.explanation()
    }


@app.get("/cafe/komeda")
async def hello():
    komeda = Cafe("コメダ珈琲", "シロノワール")
    return {
        "message": komeda.explanation()
    }


class Cafe:
    def __init__(self, name: str, product: str):
        self.name = name
        self.product = product

    def explanation(self):
        return f"{self.name}のおすすめ商品は{self.product}です！"
