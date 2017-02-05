import math
import random
import time
import urllib
import uuid
import ujson as json
import ss2_config
from django.conf import settings 
import httplib
import threading
from datetime import datetime



class MyThread(threading.Thread):
    def __init__(self,url,payload,timeout):
        threading.Thread.__init__(self)
        self.url=url
        self.payload=payload
        self.timeout=timeout
    def run(self):
        shieldsquare_post_async(self.url, self.payload, self.timeout)

class ShieldSquareRequest:

    _zpsbd0 = "false"
    _zpsbd1 = ""
    _zpsbd2 = ""
    _zpsbd3 = ""
    _zpsbd4 = ""
    _zpsbd5 = ""
    _zpsbd6 = ""
    _zpsbd7 = ""
    _zpsbd8 = ""
    _zpsbd9 = ""
    _zpsbda = ""
    __uzma  = ""
    __uzmb  = 0
    __uzmc  = ""
    __uzmd  = 0


class ShieldSquareCurlResponseCode:

    error_string = ""
    responsecode = 0


class ShieldSquareResponse(object):

    pid          = ""
    responsecode = 0
    url          = ""
    reason       = ""


class ShieldSquareCodes:

    ALLOW   = 0
    CAPTCHA = 2
    BLOCK   = 3
    FFD     = 4
    ALLOW_EXP = -1

def shield_square_validate_request(shieldsquare_call_type,
                                  request):
    shieldsquare_username = ''
    shieldsquare_low  = 10000
    shieldsquare_high = 99999

    shieldsquare_request      = ShieldSquareRequest()
    shieldsquare_return_codes = ShieldSquareCodes()
    shieldsquare_response     = ShieldSquareResponse()

    shieldsquare_curl_response = ShieldSquareCurlResponseCode()
    shieldsquare_service_url   = ss2_config._ss2_domain
    cookie_value_dict    = dict()
    shieldsquare_ex_time = (3600 * 24 * 365 * 10) + (1 * 1 * 3 * 60 * 60)
    shieldsquare_pid = shieldsquare_generate_pid(ss2_config._sid, request)
    shieldsquare_uzma = request.COOKIES['__uzma'] if request.COOKIES.has_key('__uzma') else str(uuid.uuid1())
    cookie_value_dict["__uzma"] = {"value": shieldsquare_uzma, "age": shieldsquare_ex_time}
    shieldsquare_request.__uzma = shieldsquare_uzma

    if request.COOKIES.has_key('__uzmc'):
        shieldsquare_uzmc = request.COOKIES["__uzmc"]
        shieldsquare_uzmc = int(shieldsquare_uzmc[5:-5])
        shieldsquare_a    = ((shieldsquare_uzmc - 7) / 3) + 1
        shieldsquare_uzmc = str(random.randint(shieldsquare_low, shieldsquare_high)) + \
            str(7 + shieldsquare_a * 3) + str(random.randint(shieldsquare_low, shieldsquare_high))
    else:
        shieldsquare_uzmc = str(random.randint(shieldsquare_low, shieldsquare_high)) + \
            str(7 + 1 * 3) + str(random.randint(shieldsquare_low, shieldsquare_high))

    cookie_value_dict["__uzmc"] = {"value": shieldsquare_uzmc, "age": shieldsquare_ex_time}
    shieldsquare_request.__uzmc = shieldsquare_uzmc

    shieldsquare_uzmb = request.COOKIES['__uzmb'] if request.COOKIES.has_key('__uzmb') else int(time.time())
    cookie_value_dict["__uzmb"] = {"value": shieldsquare_uzmb, "age": shieldsquare_ex_time}
    shieldsquare_request.__uzmb = shieldsquare_uzmb

    shieldsquare_time = int(time.time())
    cookie_value_dict["__uzmd"] = {"value": shieldsquare_time, "age": shieldsquare_ex_time}
    shieldsquare_request.__uzmd = shieldsquare_time

    shieldsquare_request._zpsbd0 = 'true' if ss2_config._mode == "Active" else 'false'

    shieldsquare_request._zpsbd1 = ss2_config._sid #if ss2_config._sid is not None else ''
    shieldsquare_request._zpsbd2 = shieldsquare_pid #if 
    shieldsquare_request._zpsbd3 = request.META.get('HTTP_REFERER') if request.META.get('HTTP_REFERER') is not None else ''
    shieldsquare_request._zpsbd4 = request.build_absolute_uri() if request.build_absolute_uri() is not None else ''
    shieldsquare_request._zpsbd5 = request.COOKIES.get(settings.SESSION_COOKIE_NAME) if request.COOKIES.get(settings.SESSION_COOKIE_NAME) is not None else ''
    shieldsquare_request._zpsbd6 = request.META.get(ss2_config._ipaddress) if request.META.get(ss2_config._ipaddress) is not None else '0.0.0.0'
    shieldsquare_request._zpsbd7 = request.META.get('HTTP_USER_AGENT') if request.META.get('HTTP_USER_AGENT') is not None else ''
    shieldsquare_request._zpsbd8 = shieldsquare_call_type
    shieldsquare_request._zpsbd9 = shieldsquare_username if shieldsquare_username is not None else ''
    shieldsquare_request._zpsbda = shieldsquare_time

    shieldsquare_json_obj = json.dumps(shieldsquare_request.__dict__)

    if ss2_config._mode == "Active":
        shieldsquare_response = handle_active_mode(shieldsquare_response,
                                                   shieldsquare_service_url,
                                                   shieldsquare_json_obj,
                                                   shieldsquare_return_codes,
                                                   shieldsquare_curl_response)
    else:
        shieldsquare_response = handle_monitor_mode(shieldsquare_response,
                                                    shieldsquare_service_url,
                                                    shieldsquare_json_obj,
                                                    shieldsquare_return_codes,
                                                    shieldsquare_curl_response)
    shieldsquare_response.dynamic_JS = "var __uzdbm_c = 2+2"
    shieldsquare_response.pid = shieldsquare_pid
    return shieldsquare_response.__dict__, cookie_value_dict


def handle_active_mode(shieldsquare_response,
                       shieldsquare_service_url,
                       shieldsquare_json_obj,
                       shieldsquare_return_codes,
                       shieldsquare_curl_response):
    

    shieldsquare_curl_response = shieldsquare_post_sync(shieldsquare_service_url,
                                                        shieldsquare_json_obj,
                                                        ss2_config._timeout_value)
    if str(shieldsquare_curl_response[1]) != '200':
        shieldsquare_response.responsecode = shieldsquare_return_codes.ALLOW_EXP
        shieldsquare_response.reason = shieldsquare_curl_response[0]
    else:
        shieldsquare_response_from_ss = json.loads(str(shieldsquare_curl_response[0]))
        shieldsquare_response.dynamic_JS = shieldsquare_response_from_ss['dynamic_JS']
        response_code = int(shieldsquare_response_from_ss['ssresp'])

        if response_code   == 0:
            shieldsquare_response.responsecode = shieldsquare_return_codes.ALLOW
        elif response_code == 1:
            shieldsquare_response.responsecode = shieldsquare_return_codes.MONITOR
        elif response_code == 2:
            shieldsquare_response.responsecode = shieldsquare_return_codes.CAPTCHA
        elif response_code == 3:
            shieldsquare_response.responsecode = shieldsquare_return_codes.BLOCK
        elif response_code == 4:
            shieldsquare_response.responsecode = shieldsquare_return_codes.FFD
        else:
            shieldsquare_response.responsecode = shieldsquare_return_codes.ALLOW_EXP
            shieldsquare_response.reason = str(shieldsquare_curl_response[1])
    return shieldsquare_response


def handle_monitor_mode(shieldsquare_response,
                        shieldsquare_service_url,
                        shieldsquare_json_obj,
                        shieldsquare_return_codes,
                        shieldsquare_curl_response):
    shieldsquare_response.responsecode = shieldsquare_return_codes.ALLOW
    if ss2_config._async_http_post:
        try:
            th= MyThread(shieldsquare_service_url,
                                            shieldsquare_json_obj,
                                                    ss2_config._timeout_value)
            th.start()
        except OSError:
            return shieldsquare_response
        except:
            return shieldsquare_response

        return shieldsquare_response
    else:
        shieldsquare_curl_response = shieldsquare_post_sync(shieldsquare_service_url,
                                                            shieldsquare_json_obj, 
                                                            ss2_config._timeout_value)

        if str(shieldsquare_curl_response[1]) != '200':
            shieldsquare_response.responsecode = shieldsquare_return_codes.ALLOW_EXP
            shieldsquare_response.reason = str(shieldsquare_curl_response[0])
        return shieldsquare_response
def shieldsquare_post_async(url, payload, timeout):
    dt=datetime.now()
    try:
        h1 = httplib.HTTPConnection(url,port=80)
        headers = {"Content-type":"application/x-www-form-urlencoded","Accept":"application/json"}
        h1.request('POST','/getRequestData',urllib.quote(payload),headers)
        h1.sock.settimeout(timeout)
        h1.close()
    except:
        pass
    if ss2_config._logger==True:
        ss2_config.write_log("total time of processing by async method"+str(datetime.now()-dt))    

def shieldsquare_post_sync(url, params, timeout):
    dt=datetime.now()
    try:     
        h1 = httplib.HTTPConnection(url,port=80)
        headers = {"Content-type":"application/x-www-form-urlencoded","Accept":"application/json"}
        h1.request('POST','/getRequestData',urllib.quote(params),headers)
        h1.sock.settimeout(timeout)
        response= h1.getresponse()
        data=response.read()
        code=response.status
        response=[data,code]
        h1.close()      
    except:
        response = ["Request Timed Out/Server Not Reachable", "0"]
    if ss2_config._logger==True:
        ss2_config.write_log("total time of processing by async method"+str(datetime.now()-dt)) 
    return response


def shieldsquare_generate_pid(shieldsquare_sid, request):
    t = '%f %d' % math.modf(time.time())
    tm = t.split(" ")
    _, _, _, p4, _ = shieldsquare_sid.split("-")
    sid_min = int(p4, 16)
    rmstr1 = "00000000" + "%x" % int(tm[1])
    rmstr2 = "0000" + "%x" % int(round(float(tm[0]) * 65536))
    return '%08s-%04x-%04s-%04s-%04x%04x%04x' % (shieldsquare_ip2hex(request), sid_min, rmstr1[-4:], rmstr2[-4:],
                                                 random.randint(0, 0xffff), random.randint(0, 0xffff), random.randint(0, 0xffff))


def shieldsquare_ip2hex(request):
    ip = get_client_IP(request)
    part = ip.split('.')
    hexx = ""

    for i in range(0, len(part)):
        dt = "0" + "%x" % int(part[i])
        hexx = hexx + dt[-2:]
    return hexx

def get_client_IP(request):
    if ss2_config._ipaddress == "HTTP_X_FORWARDED_FOR":
        ip_tuple = request.META.get("HTTP_X_FORWARDED_FOR")
        client_ip = ip_tuple.split(',')[0]
        return client_ip
    elif ss2_config._ipaddress == "X_FORWARDED_FOR":
        ip_tuple = request.META.get("X_FORWARDED_FOR")
        client_ip = ip_tuple.split(',')[0]
        return client_ip
    else:
        ip = request.META.get(ss2_config._ipaddress)
        return ip

def set_cookie_in_response(response, cookie_values_dict):
    for cookie_name in cookie_values_dict:
        response.set_cookie(cookie_name, cookie_values_dict[cookie_name]["value"], max_age=cookie_values_dict[cookie_name]["age"])
    return response


        
