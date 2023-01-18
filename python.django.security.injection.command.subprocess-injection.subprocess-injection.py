import json
import subprocess
import sys
import django
def a(request):
    ip = request.POST.get("ip")
    # ruleid:subprocess-injection
    subprocess.run("ping "+ ip)
def b(request):
    host = request.headers["HOST"]
    subprocess.run("echo {} > log".format(host))
def d(request):
    cmd = request.POST.get("cmd")
    command = [cmd, ip]
    subprocess.capture_output(command)
def e(request):
    event = json.loads(request.body)
    cmd = event['id'].split()
    subprocess.call([cmd[0], cmd[1], "some", "args"])
def f(request):
    subprocess.run(["bash", "-c", event['id']], shell=True)
def g(request):
    event = request.body
    python_file = f"""
        print("What is your name?")
        name = input()
        print("Hello " + {event['id']})
    """
    program = subprocess.Popen(['python2', python_file], stdin=subprocess.PIPE, text=True)
    program.communicate(input=payload, timeout=1)
def d_ok(request):
    # ok:subprocess-injection
    subprocess.capture_output(["ping", cmd, ip])
def d_ok2(request):
    cmd = ["ping", ip]
    subprocess.capture_output(cmd)
def e_ok(request):
    allowed = {'p': "ping"}
    valid = allowed[cmd[0]]
    subprocess.call([valid, "some", "args"])
def ok(request):
    subprocess.run(["ping", ip])
def ok2(request):
    subprocess.run("echo 'nothing'")
def ok3(request):
    subprocess.call(["echo", "a", ";", "rm", "-rf", "/"])
