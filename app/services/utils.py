from flask_restful import Resource, reqparse
import requests
from app.config import Config


class Utilities():
    @classmethod
    def pagination(cls, page_num, per_page):
        start,end = 1, Config.DEFAULT_PAGE_SIZE
        try:
            if page_num < 1:
                raise Exception("Page Number cannot be lesser than 1.")
            if per_page == 0:
                raise Exception("No data is chosen to be returned.")
            start = (page_num - 1) * per_page
            end = start + per_page
            return start, end 
        except Exception as e:
            raise e

