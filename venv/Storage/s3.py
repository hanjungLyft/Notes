import boto3
import uuid


class S3Wrapper:

    __client = boto3.resource('s3', region_name='us-east-2')

    @classmethod
    def put(cls, data):
        file_id = str(uuid.uuid4())
        object = cls.__client.Object('hanjungsupers3bucket', file_id)
        object.put(Body=data)
        return id

    @classmethod
    def get(cls, file_id):
        object = cls.__client.Object('hanjungsupers3bucket', file_id)
        return object.get()
