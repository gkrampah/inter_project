"""Module provides a function for downloading data in the sqs queue"""
import os
import boto3


def download_data_file_dataframe():
    """downloads the data in the sqs queue using boto3"""
    # Set up AWS credentials
    aws_access_key_id = "removed for security but saved as environment variable "
    aws_secret_access_key = "removed for security but saved as environment variable "

    # Connect to SQS queue
    queue_url = "removed for security but saved as environment variable"
    sqs = boto3.client(
        "sqs",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name="eu-west-1",
    )

    # Receive messages from the queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=10,
        VisibilityTimeout=30,
        WaitTimeSeconds=20,
    )

    # Process the messages

    messages = response.get("Messages", [])
    for message in messages:
        message_body = message["Body"]
        message_id = message["MessageId"]
        os.makedirs("messages2", exist_ok=True)
        with open(f"messages/{message_id}.txt", "w", encoding="utf-8") as file_:
            file_.write(message_body)


# if __name__ == "__main__":
# download_data_file_dataframe()
