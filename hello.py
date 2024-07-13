from fastapi import FastAPI, Body, Header, Response
from fastapi.responses import HTMLResponse


app = FastAPI()

# http headers
# http -v localhost:8000/hi who:Mom
@app.post("/hi")
def greet(who: str = Header()):
    return f"Hello? {who}?"

# HTTP body
# http -v localhost:8000/hi who=Mom
@app.post("/hi")
def greet(who: str = Body(embed=True)):
    return f"Hello? {who}?"

# Query Parameter:

@app.get("/hi")
def greet(who: str):
    return f"Hello? {who}?"

@app.get("/hi")
def greet():
    return "Hello? World?"

# URL Path Parameter:

@app.get("/hi/{who}")
def greet(who: str):
    return f"Hello? {who}?"

# http header
@app.post("/hi")
def greet(who: str = Header()):
    return f"Hello? {who}?"


# custom headers
@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal body"


# html response 
@app.get("/html", response_class=HTMLResponse)
def get_html():
    return "<h1>Hello, HTML!</h1>"


@app.get("/happy")
def happy(status_code=200):
    return ":)"


@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal body"

from pydantic import BaseModel
from datetime import datetime

class TagIn(BaseModel):
    tag: str

class Tag(BaseModel):
    tag: str
    created: datetime
    secret: str

class TagOut(BaseModel):
    tag: str
    created: datetime

@app.post('/')
def create(tag_in: TagIn) -> TagIn:
    tag: Tag = Tag(tag=tag_in.tag, created=datetime.utcnow(), secret="shhhh")
    return tag_in

@app.get('/{tag_str}', response_model=TagOut)
def get_one(tag_str: str) -> TagOut:
    tag: Tag = Tag(tag=tag_str, created=datetime.utcnow(), secret="shhhh")
    return tag


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)
