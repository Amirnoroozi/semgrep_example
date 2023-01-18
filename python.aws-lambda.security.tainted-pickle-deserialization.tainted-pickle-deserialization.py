import _pickle
import cPickle
from dill import loads
import shelve
def lambda_handler(event, context):
  # ruleid: tainted-pickle-deserialization
  _pickle.load(event['exploit_code'])
  obj = cPickle.loads(f"foobar{event['exploit_code']}")
  loads(event['exploit_code'])(123)
  with shelve.open(f"/tmp/path/{event['object_path']}") as db:
    db['eggs'] = 'eggs'
  # ok: tainted-pickle-deserialization
  _pickle.loads('hardcoded code')
  code = '/file/path'
  cPickle.load(code)
  name = 'foobar'
  shelve.open(f"/tmp/path/{name}")
