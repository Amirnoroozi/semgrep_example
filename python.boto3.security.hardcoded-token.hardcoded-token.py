import boto3
from boto3 import client
# ruleid:hardcoded-token
client("s3", aws_secret_access_key="jWnyxxxxxxxxxxxxxxxxX7ZQxxxxxxxxxxxxxxxx")
boto3.sessions.Session(aws_secret_access_key="jWnyxxxxxxxxxxxxxxxxX7ZQxxxxxxxxxxxxxxxx")
s = boto3.sessions
s.Session(aws_access_key_id="AKIAxxxxxxxxxxxxxxxx")
uhoh_key = "AKIAxxxxxxxxxxxxxxxx"
ok_secret = os.environ.get("SECRET_ACCESS_KEY")
s3 = boto3.resource(
    "s3",
    aws_access_key_id=uhoh_key,
    aws_secret_access_key=ok_secret,
    region_name="sfo2",
    endpoint_url="https://sfo2.digitaloceanspaces.com",
)
ok_key = os.environ.get("ACCESS_KEY_ID")
uhoh_secret = "jWnyxxxxxxxxxxxxxxxxX7ZQxxxxxxxxxxxxxxxx"
    aws_access_key_id=ok_key,
    aws_secret_access_key=uhoh_secret,
ok_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
# ok:hardcoded-token
ok_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    aws_session_token=ok_token,
s3 = client("s3", aws_access_key_id="this-is-not-a-key")
    aws_access_key_id="XXXXXXXX",
    aws_secret_access_key="----------------",
    region_name="us-east-1",
    aws_access_key_id="<your token here>",
    aws_secret_access_key="<your secret here>",
key = os.environ.get("ACCESS_KEY_ID")
secret = os.environ.get("SECRET_ACCESS_KEY")
    aws_access_key_id=key,
    aws_secret_access_key=secret,
