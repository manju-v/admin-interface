from connector import ss2, ss2_config
from connector.ss2 import set_cookie_in_response
from datetime import datetime

class ShieldSquareMiddleware(object):

    def __init__(self):
        self.shield_square_response = None
        self.cookie_values          = None

    def process_request(self, request):
        """
        Call Types
            1 - Page Load
            2 - Form Submission
            3 - AJAX Request
        """
        dt=datetime.now()
        if 'favicon.ico' in request.path:
            return None
        shield_square_call_type = 1

        if request.method == "POST":
            shield_square_call_type = 2
        elif request.is_ajax():
            shield_square_call_type = 3
        request.shield_square_response, request.cookie_values = ss2.shield_square_validate_request(shield_square_call_type,
                                                                                           request)
        if ss2_config._logger==True:
            ss2_config.write_log("total time for response"+str(datetime.now()-dt))
        return None 

    def process_response(self, request, response):
        if request.cookie_values is None:
            return response
        else:
            set_cookie_in_response(response, request.cookie_values)

        if 'favicon.ico' in request.path \
            or request.shield_square_response is None \
            or request.is_ajax():
            return response
        else:
            response.write(
                """<script>
                    var __uzdbm_a = "{0}";
                   </script>
                   <div id="ss_098786_234239_238479_190541"></div>
                   <script src ="https://cdn.perfdrive.com/static/jscall_min.js" async="true"></script>
                """.format(request.shield_square_response['pid'])
            )

        return response














