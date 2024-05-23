from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import json
from fastapi import Request
from starlette.datastructures import URL

possible_sources=["file_system","document_datastore","Relational_database"]

class AppUtils:
    def __init__(self,data_src,data_location):
        self.data_src = data_src
        self.data_location = data_location
        self.render_engine = self.get_env()
        
    def get_env(self):
        return Environment(loader=FileSystemLoader("src/templates/"),
        autoescape=select_autoescape(),
        variable_start_string="${",
        variable_end_string="}")
    
    def render_html(self,user_name: str, request: Request):
        template = self.render_engine.get_template("index.tmpl.html")
        return template.render(author_name = self.generate_json_link(user_name,request.base_url))
        
    def generate_json_link(self, user_name:str, request_url:URL):
        env_base_url = os.environ.get("APP_BASE_URL")
        base_url: str
        if env_base_url is not None:
            base_url = "{}/json".format(env_base_url)        
        elif request_url.is_secure:
            base_url = request_url._url
        else:
            base_url = "https://{}/json".format(request_url.hostname)
        return "{0}/{1}".format(base_url,user_name)

    def get_json(self, user_name:str):
        obj: str
        if self.data_src == possible_sources[0]:
            filename = "{}/{}.json".format(self.data_location,user_name)
            with open(filename,"r") as fileContent:
                obj = fileContent.read()
        return json.loads(obj)