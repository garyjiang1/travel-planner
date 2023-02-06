import requests
import json
import boto3

AWSAccessKeyId = "AKIAZK46SAEWYBQYI72C"
AWSSecretKey = "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"


class NotificationMiddlewareHandler:
    sns_client = None

    def __init__(self):
        pass

    @classmethod
    def get_sns_client(cls):
        if NotificationMiddlewareHandler.sns_client is None:
            NotificationMiddlewareHandler.sns_client = sns = boto3.client("sns",
                                                                          aws_access_key_id=AWSAccessKeyId,
                                                                          aws_secret_access_key=AWSSecretKey,
                                                                          region_name="us-east-2"
                                                                          )
        return NotificationMiddlewareHandler.sns_client

    @classmethod
    def send_sns_message(cls, sns_topic, message):
        s_client = NotificationMiddlewareHandler.get_sns_client()
        response = s_client.publish(
            TargetArn=sns_topic,
            Message=json.dumps({'default': json.dumps(message)}),
            MessageStructure='json',
            Subject='Test'
        )
        print("Publish response = ", json.dumps(response, indent=2, default=str))
