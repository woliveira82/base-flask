from app.inc import ResponseException


class Valid:
    

    def __init__(self, required=False, location='json', type=str, default=None):
        self.required = required if required in [True, False] else False
        self.location = location if location in ['json', 'form', 'args'] else 'json'
        self.type = str
        self.default = None if required else default


class Parser:


    def __init__(self, request):
        self.request = request

    
    def parse(self, kwargs):
        data = {}
        for k, v in kwargs.items():
            if not isinstance(v, Valid):
                raise ResponseException(k, status=500, message='Wrong validation required')

            location = getattr(self.request, v.location)
            value = location.get(k, v.default) if location else None
            if v.required and not value:
                raise ResponseException(k, status=400, message=f'The field \'{k}\' is mandatory')
            
            data.update({k: value})

        return data
