def handler(event, context):
    # ok:tainted-code-exec
    exec("x = 1; x = x + 2")
    blah1 = "import requests; r = requests.get('https://example.com')"
    exec(blah1)
    dynamic1 = "import requests; r = requests.get('{}')"
    # ruleid:tainted-code-exec
    exec(dynamic1.format(event['url']))
    eval("x = 1; x = x + 2")
    blah2 = "import requests; r = requests.get('https://example.com')"
    eval(blah2)
    dynamic2 = "import requests; r = requests.get('{}')"
    eval(dynamic2.format(event['url']))
