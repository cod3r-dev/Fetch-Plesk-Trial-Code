import re
import requests
test_str = requests.get('https://trialplesk.domainhizmetleri.com').text
result = re.findall(r"]\('(.*?)'\+'-'\+'(.*?)'\+'-'\+'(.*?)'\+'-'\+'(.*?)'\+'-'\+'(.*?)'\);",test_str)
print(result[0][0] + "-" + result[0][1] + "-" + result[0][2] + "-" + result[0][3] + "-" + result[0][4])
