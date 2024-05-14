from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import json
from dotenv import load_dotenv
from fastapi import Request
data_src = os.environ.get("APP_DATA_SRC")
data_location = os.environ.get("APP_DATA_LOCATION")
possible_sources=["file_system","document_datastore","Relational_database"]
    
def get_env():
    return Environment(loader=FileSystemLoader("src/templates/"),
    autoescape=select_autoescape(),
    variable_start_string="${",
    variable_end_string="}")
    
def render_html(user_name: str, env, request: Request):
    template = env.get_template("index.tmpl.html")
    return template.render(author_name = generate_json_link(user_name,request.base_url._url))
    
def generate_json_link(user_name:str, request_url:str):
    base_url = "{}json".format(request_url)
    return "{0}/{1}/".format(base_url,user_name)

# def get_base_url():
#     obj: str
#     obj = os.environ.get("")

def get_json(user_name:str):
    obj: str
    if data_src == possible_sources[0]:
        print(data_location)
        filename = "{}/{}.json".format(data_location,user_name)
        print(filename)
        with open(filename,"r") as fileContent:
            obj = fileContent.read()
    return json.loads(obj)