import urllib
import urllib.request

try:
    site=urllib.request.urlopen('https://www.cursoemvideo.com/')
except urllib.error.URLError:
    print('O site está inacecível no momento.')
else:
    print('O site do Gustavinho está disponível igual o adm!')