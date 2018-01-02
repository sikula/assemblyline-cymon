import json

from assemblyline.al.service.base import ServiceBase
from assemblyline.al.common.result import Result, ResultSection, SCORE
from assemblyline.common.exceptions import RecoverableError

class CymonAPIService(ServiceBase):
    SERVICE_CATEGORY        = "External"
    SERVICE_DESCRIPTION     = "This service checks the file hash against the Cymon API"
    SERVICE_VERSION         = "1"

    SERVICE_ACCEPTS         = ".*"
    SERVICE_REVISION        = ServiceBase.parse_revision("$Id$")
    SERVICE_ENABLED         = True

    SERVICE_IS_EXTERNAL     = True
    SERVICE_STAGE           = "CORE"
    SERVICE_DEFAULT_CONFIG  = {
        'API_KEY': '',
        'BASE_URL': 'https://api.cymon.io/v2/ioc/search/sha256'
    }

    def __init__(self, cfg=None):
        super(CymonAPIService, self).__init__(cfg)
        self.api_key = self.cfg.get('API_KEY')


    # `requests` is needed to communicate with the API
    def import_service_deps(self):
        global requests
        import requests


    def start(self):
        self.log.debug("CymonAPIService Started")

    
    def execute(self, request):
        response = self.process_file(request)
        result   = self.parse_results(response)
        requests.result = result




    def process_file(self, request):
        url = self.cfg.get('BASE_URL') + request.sha256
        params = requests.get(url)

        try:
            json_response = r.json()
        except ValueError:
            self.log.warn(
                "Invalid response from Cymon, ",
                "HTTP Code: %s",
                "content length: %i",
                "headers: %s" % (r.status_code, len(r.content), repr(r.headers))    
            )
            if len(r.content) == 0:
                raise RecoverableError("Cymon didn't return a JSON object, HTTP code %s" % r.status_code)
            raise
        return json_response


    def parse_results(self, request):
        pass