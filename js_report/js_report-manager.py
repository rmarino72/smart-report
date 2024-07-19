import requests
from basic.basic_resource import BasicResource
from log.btkg_logger import BtkgLogger


class JsReportManager(BasicResource):
    __url: str | None

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    def __init__(self, url: str | None = None, logger: BtkgLogger | None = None):
        self.logger = logger
        self.__url = url

    @staticmethod
    def compose_excel_options(excel_encoded_template: str, data: {}, content: str = "{{{xlsxPrint}}}") -> {}:
        return {
            "template": {
                "recipe": "xlsx",
                "engine": "handlebars",
                "content": content,
                "xlsx": {
                    "templateAsset": {
                        "content": excel_encoded_template,
                        "encoding": "base64"
                    }
                }
            },
            "data": data
        }

    def generate(self, content):
        headers = {            
            'Content-Type': "application/json"
        }
        response = requests.post(self.url, json=content, headers=headers)
        r: [] = [chunk for chunk in response]
        return r