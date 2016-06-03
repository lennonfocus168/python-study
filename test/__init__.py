import base64
import urllib

username = "abc"
username_ = urllib.quote(username)
username = base64.encodestring(username_)[:-1]

print(username_)
print(username)
