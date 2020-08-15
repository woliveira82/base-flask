from flask import Blueprint
from .InfoAPI import InfoAPI

info = Blueprint('info', __name__)

info_api = InfoAPI.as_view('config_api')
info.add_url_rule(None, view_func=info_api, methods=['GET'])
