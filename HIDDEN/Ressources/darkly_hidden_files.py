import requests
import re
import time

def fetch_result(path):
    r = requests.get(path)
    contents = r.content.decode('utf-8')
    if "<h1>Index of" in contents:
        results = re.findall('<a href="(.*)">', contents)
        for res in results:
            if ".." not in res and "." not in res:
                #print(path+res)
                time.sleep(0.01)
                fetch_result(path+res)
    else:
        print(contents)

url = "http://10.11.100.93/.hidden/"
fetch_result(url)
