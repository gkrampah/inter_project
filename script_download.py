def download_data_file_dataframe():
23     # Set up AWS credentials
24     aws_access_key_id = "AKIAUGA3LPW6WGFUXOY2"
25     aws_secret_access_key = "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"
26
27     # Connect to SQS queue
28     queue_url = "https://sqs.eu-west-1.amazonaws.com/287820185021/openaq-godwin"
29     sqs = boto3.client(
30         "sqs",
31         aws_access_key_id=aws_access_key_id,
32         aws_secret_access_key=aws_secret_access_key,
33         region_name="eu-west-1",
34     )
35
36     # Receive messages from the queue
37     response = sqs.receive_message(
38         QueueUrl=queue_url,
39         MaxNumberOfMessages=10,
40         VisibilityTimeout=30,
41         WaitTimeSeconds=20,
42     )
43
44     # Process the messages
45
46     messages = response.get("Messages", [])
47     data = []
48     for message in messages:
49         body = message["Body"]
50         record = json.loads(body)
51         for result in record["results"]:
52             data.append(result)
53
54     # Convert data to Pandas DataFrame
55     df = pd.DataFrame(data)
56
57     # Write data to file
58     df.to_csv("openaq_data.csv", index=False)

