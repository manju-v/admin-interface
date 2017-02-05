# Enter your subscriber id
_sid = '522480eb-1f7f-443b-93b0-e7ce8b736b46'

# Please specify the mode in which you want to operate
# _mode = 'Active'/'Monitor';
_mode = 'Monitor'
# Note: Enable this only if you are hosting your applications on Linux environments.
_async_http_post = True

# Timeout in seconds should be between max 1 seconds
_timeout_value = 1.0 # 

# Change this value if your servers are behind a firewall or proxy
_ipaddress = 'REMOTE_ADDR'

# Enter the URL pattern for the JavaScript Data Collector view

# Set the ShieldSquare domain based on your Server Locations
#    US/Europe      -        'ss_scus.shieldsquare.net'
     #India/Asia     -    'ss_sa.shieldsquare.net'
#    Australia      -    'ss_au.shieldsquare.net'
#    South America  -    'ss_br.shieldsquare.net'
#    North America  -    'ss_scus.shieldsquare.net'
_ss2_domain = 'ss_sa.shieldsquare.net'
  
_logger= False
import logging
LOG_FILENAME = 'responsetime.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

def write_log(msg):
    logging.info(msg)




