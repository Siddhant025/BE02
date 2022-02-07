import queue
import boto3
import json
import env

def SNS():
    topicArn = 'arn:aws:sns:us-east-1:484958538548:practo'
    snsClient = boto3.client(
        'sns',
        aws_access_key_id=env.AWSAccessKeyId,
        aws_secret_access_key=env.AWSSecretKey,
        region_name='us-east-1'
    )

    publishObject = {'transactionId':654 , 'amount': 120}

    response = snsClient.publish(TopicArn=topicArn,
                                Message=json.dumps(publishObject),
                                Subject='PURCHASE',
                                MessageAttributes = { "TransactionType" :{"DataType":"String","StringValue":"PURCHASE"}}
    )

    print(response['ResponseMetadata']['HTTPStatusCode'])


def SQS():
    sqsResource = boto3.client(
        'sqs',
        aws_access_key_id=env.AWSAccessKeyId,
        aws_secret_access_key=env.AWSSecretKey,
        region_name='us-east-1'
    )

    QueueUrl = "https://queue.amazonaws.com/484958538548/pacto"
    response = sqsResource.receive_message(
        QueueUrl=QueueUrl,
        AttributeNames=[
        'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
        'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )

    print(response)

    # queue = sqsResource.get_queue_by_name(QueueName = 'pacto')

    # for message in queue.receive_messages():
    #     print(message.body)
    #     print(message.url)




SNS()
SQS()