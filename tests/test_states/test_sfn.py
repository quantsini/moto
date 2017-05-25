from __future__ import unicode_literals

from moto import mock_states
import boto3
import json

@mock_states
def test_thing():
    client = boto3.client('stepfunctions', 'us-east-1')
    result = client.start_execution(
        stateMachineArn='dummy',
        name='dummy',
        input=json.dumps(dict(cat='meow')),
    )
    print(result)