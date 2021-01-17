class HttpResponse(object):

    def __init__(self, response):
        self.status_code = response.status_code
        if response.text != '':
            self.content = response.json()
        else:
            self.content = {}
