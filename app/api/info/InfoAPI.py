from flask.views import MethodView
from app.inc import Response


class InfoAPI(MethodView):


    def get(self):
        return Response(None, message='Server is up!').to_dict()
