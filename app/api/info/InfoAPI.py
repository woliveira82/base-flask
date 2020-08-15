from flask.views import MethodView


class InfoAPI(MethodView):


    def get(self):
        return 'Server is up!', 200
