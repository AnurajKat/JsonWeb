import os
import sys
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import app_utils
import uvicorn

app = FastAPI()
render_engine = app_utils.get_env()

@app.get("/about/{author_name}", response_class=HTMLResponse)
async def root(author_name: str,request: Request):
    return app_utils.render_html(author_name,render_engine,request)


@app.get("/json/{author_name}", response_class=JSONResponse)
async def getAuthorDetails(author_name: str):
    return app_utils.get_json(author_name)

@app.get("/me", response_class=HTMLResponse)
async def about_me(request: Request):
    app_owner_name = os.environ.get("JSON_APP_OWNER")
    return app_utils.render_html(app_owner_name,render_engine,request)

def get_port():
    port =  int(os.environ.get("APP_PORT"))
    if port is None:
        port = 8000
    return port

def main(args: list):
    load_dotenv()
    uvicorn.run(app,host="0.0.0.0",port=get_port())

if __name__ == "__main__":
    main(sys.argv[1:])


