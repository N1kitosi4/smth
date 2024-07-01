from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data_new": "index_new"}
