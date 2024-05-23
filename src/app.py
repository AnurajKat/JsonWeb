import os
import sys
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from app_utils import AppUtils
import uvicorn

app = FastAPI()
app_utils: AppUtils

@app.get("/about/{author_name}", response_class=HTMLResponse)
async def root(author_name: str,request: Request):
    global app_utils
    return app_utils.render_html(author_name,request)


@app.get("/json/{author_name}", response_class=JSONResponse)
async def getAuthorDetails(author_name: str):
    global app_utils
    return app_utils.get_json(author_name)

@app.get("/",response_class=HTMLResponse)
async def about_me(request: Request):
    app_owner_name = os.environ.get("JSON_APP_OWNER")
    return app_utils.render_html(app_owner_name,request)

def get_port():
    port =  int(os.environ.get("APP_PORT"))
    if port is None:
        port = 8000
    return port

def main(args: list):
    global app_utils
    load_dotenv()
    app_utils = AppUtils(os.environ.get("APP_DATA_SRC"),os.environ.get("APP_DATA_LOCATION"))
    uvicorn.run(app,host="0.0.0.0",port=get_port())

if __name__ == "__main__":
    main(sys.argv[1:])


