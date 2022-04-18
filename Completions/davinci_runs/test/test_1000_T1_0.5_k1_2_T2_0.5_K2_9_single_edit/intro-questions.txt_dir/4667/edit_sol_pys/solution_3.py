
import re
def get_ip_addresses(input_string):
    # your code here
    return re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', input_string)
