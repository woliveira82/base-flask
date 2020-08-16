class Response:


    def __init__(self, data, status=200, message=None, simple_response=False):
        self.data = self._set_data(data, simple_response)
        self.status = status
        self. message = message


    def _set_data(self, data, simple_response):
        if simple_response:
            return data
        
        if type(data) is list:
            return [instance.to_dict() for instance in data]

        if not data:
            return {}
        
        if isinstance(data, dict):
            return data

        return data.to_dict()


    def to_dict(self):
        http_success_status = {
            100: 'Continue',
            101: 'Switching Protocols',
            103: 'Early Hints',
            200: 'OK',
            201: 'Created',
            202: 'Accepted',
            203: 'Non-Authoritative Information',
            204: 'No Content',
            205: 'Reset Content',
            206: 'Partial Content',
            300: 'Multiple Choices',
            301: 'Moved Permanently',
            302: 'Found',
            303: 'See Other',
            304: 'Not Modified',
            307: 'Temporary Redirect',
            308: 'Permanent Redirect'
        }

        response = {
            'data': self.data,
            'message': self.message if self.message else http_success_status.get(self.status, ''),
            'status': self.status
        }
        return response, self.status
