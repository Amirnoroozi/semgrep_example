def test_bad_1():
    from requests import get
    from django.shortcuts import render
    def send_to_redis(request):
        # ruleid: ssrf-injection-requests
        bucket = request.GET.get("bucket")
        inner_response = get("http://my.redis.foo/{}".format(bucket), data=3)
        return render({"response_code": inner_response.status_code})
def test_bad_2():
    from django.http import HttpResponse
        return HttpResponse(body = {"response_code": inner_response.status_code})
def test_bad_3():
        inner_response = get(f"http://my.redis.foo/{bucket}", data=3)
def test_bad_4():
        bucket = request.headers.get("bucket")
def test_bad_5():
        bucket = request.GET["bucket"]
def test_bad_6():
        bucket = request.headers["bucket"]
