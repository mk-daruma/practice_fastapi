from fastapi import FastAPI

app = FastAPI()


@app.get("/cafe/star-backs")
async def first_visit():
    star_backs = StarBacks(
        "スターバックス",
        "フラペチーノ",
        3,
        False
    )

    return {
        "explanation": star_backs.explanation(),
        "stock": star_backs.check_stock(),
        "info": star_backs.check_one_more_coffee()
    }


@app.get("/cafe/star-backs/repeat")
async def repeat():
    star_backs = StarBacks(
        "スターバックス",
        "フラペチーノ",
        0,
        True
    )
    return {
        "explanation": star_backs.explanation(),
        "stock": star_backs.check_stock(),
        "info": star_backs.check_one_more_coffee()
    }


@app.get("/cafe/komeda")
async def hello():
    komeda = Cafe("コメダ珈琲", "シロノワール")
    return {
        "message": komeda.explanation()
    }


class Cafe:
    def __init__(
            self,
            name: str,
            product: str,
            stock: int
    ):
        self.name = name
        self.product = product
        self.stock = stock

    def explanation(self):
        return f"{self.name}のおすすめ商品は{self.product}です！"

    def check_stock(self):
        if self.stock > 0:
            return f"{self.product}は残り{self.stock}個です！"
        if self.stock == 0:
            return "売り切れです！"


class StarBacks(Cafe):
    def __init__(
            self,
            name: str,
            product: str,
            stock: int,
            one_more_coffee: bool
    ):
        super().__init__(name, product, stock)
        self.one_more_coffee = one_more_coffee

    def check_one_more_coffee(self):
        if self.one_more_coffee:
            return "100円でコーヒーが飲める！"

        if not self.one_more_coffee:
            return "おかわりは100円でコーヒーが飲める！"
