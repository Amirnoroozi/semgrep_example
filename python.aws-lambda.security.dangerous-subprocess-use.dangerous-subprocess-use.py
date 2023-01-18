import subprocess
import sys
def handler(event, context):
  # ok:dangerous-subprocess-use
  subprocess.call("echo 'hello'")
  subprocess.call(["echo", "a", ";", "rm", "-rf", "/"])
  # ruleid:dangerous-subprocess-use
  subprocess.call("grep -R {} .".format(event['id']))
  cmd = event['id'].split()
  subprocess.call([cmd[0], cmd[1], "some", "args"])
  subprocess.call("grep -R {} .".format(event['id']), shell=True)
  subprocess.call("grep -R {} .".format(event['id']), shell=True, cwd="/home/user")
  subprocess.run("grep -R {} .".format(event['id']), shell=True)
  subprocess.run(["bash", "-c", event['id']], shell=True)
  python_file = f"""
      print("What is your name?")
      name = input()
      print("Hello " + {event['id']})
  """
  program = subprocess.Popen(['python2', python_file], stdin=subprocess.PIPE, text=True)
  program.communicate(input=payload, timeout=1)
