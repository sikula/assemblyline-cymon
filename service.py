from assemblyline.al.service.base import ServiceBase
from assemblyline.al.common.result import Result, ResultSection, SCORE

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
        'BASE_URL': 'https://api.cymon.io/v2/ioc/search'
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
        result  = Result()
        section = ResultSection(SCORE.NULL, "Cymon API Service Complete")
        section.add_line("Nothing done.")
        result.add_section(section)
        request.result = result