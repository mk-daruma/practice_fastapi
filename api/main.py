from fastapi import FastAPI

app = FastAPI()


@app.get("/cafe/star-backs")
async def star_backs():
    return {
        "message": "スターバックスのおすすめ商品はフラペチーノです！"
    }


@app.get("/cafe/komeda")
async def komeda():
    return {
        "message": "コメダのおすすめ商品はシロノワールです！"
    }
