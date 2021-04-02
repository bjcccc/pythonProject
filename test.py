import urllib.request

result = urllib.request.urlopen("http://www.cwl.gov.cn/kjxx/ssq/kjgg/")
print(result.read())
