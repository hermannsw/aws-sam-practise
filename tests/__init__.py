import os

os.environ['DYNAMODB_HOST'] = 'http://localhost:18001'
os.environ['DYNAMODB_TABLE'] = 'messages'
os.environ['REGION'] = 'us-west-1'
