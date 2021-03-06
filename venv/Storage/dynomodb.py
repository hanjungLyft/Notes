import boto3
import dateutil.parser
from venv.Storage.keyvalue_store import KeyValueStore


class DynomoDB(KeyValueStore):

    __client = boto3.resource('dynamodb', region_name='us-east-2')
    __table = __client.Table('notes')

    def set(self, id_of : str, properties : dict):
        # table.put_item(Item={'name':'tom', 'age':40, 'height':6, 'fans':10000})
        self.__table.put_item(Item={
                                    'id':str(properties['id']),
                                    'name':str(properties['name']),
                                    'parent':str(properties['parent']),
                                    'created_time':properties['created_time'].isoformat()})
        pass

    def get(self, pattern : str):
        items = self.__table.scan()
        #yourdate = dateutil.parser.parse(datestring)
        return items['Items']
