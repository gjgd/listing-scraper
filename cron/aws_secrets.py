# https://gist.github.com/abhimskywalker/f78a353a18c8246f9c0b20c110903a45
import boto3
import os

SST_APP = os.getenv("SST_APP")
SST_STAGE = os.getenv("SST_STAGE")

def get_secret(name):
    ssm = boto3.client("ssm")
    parameter = ssm.get_parameter(
        Name=f"/sst/{SST_APP}/{SST_STAGE}/Secret/{name}/value", WithDecryption=True
    )
    return parameter["Parameter"]["Value"]
