import requests as req
import requests
some_url = "https://example.com"
# ok:disabled-cert-validation
r = req.get(some_url, stream=True)
r = requests.post(some_url, stream=True)
# ruleid:disabled-cert-validation
r = req.get(some_url, stream=True, verify=False)
r = requests.post(some_url, stream=True, verify=False)
r = requests.post(some_url, verify=False, stream=True)
