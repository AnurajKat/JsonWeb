import os
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import app_utils
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
    return app_utils.render_html(os.environ.get("APP_DATA_OWNER"),render_engine,request)
