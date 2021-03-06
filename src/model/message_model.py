import os

from pynamodb.attributes import UnicodeAttribute

from .base_model import BaseModel


class MessageModel(BaseModel):
    class Meta:
        host = os.environ['DYNAMODB_HOST'] if os.environ.get('DYNAMODB_HOST') else 'http://localhost:18000'
        table_name = os.environ['DYNAMODB_TABLE'] if os.environ.get('DYNAMODB_TABLE') else 'messages'
        region = os.environ['REGION'] if os.environ.get('REGION') else 'us-west-1'
        write_capacity_units = 10
        read_capacity_units = 10

    id = UnicodeAttribute(hash_key=True)
    user_id = UnicodeAttribute(range_key=True)
    body = UnicodeAttribute()
