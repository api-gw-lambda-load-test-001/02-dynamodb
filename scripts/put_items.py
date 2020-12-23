import hashlib
import boto3
import os


def get_dynamodb_table_name():
    client = boto3.client('cloudformation')
    option = {
        'StackName': os.environ['STACK_NAME'],
        'LogicalResourceId': 'DataTable'
    }
    resp = client.describe_stack_resource(**option)
    return resp['StackResourceDetail']['PhysicalResourceId']


def create_md5_hexdigest(num: int) -> str:
    raw = str(num).encode()
    return hashlib.md5(raw).hexdigest()


def create_batch_writer(table_name: str):
    resource = boto3.resource("dynamodb")
    table = resource.Table(table_name)
    return table.batch_writer()


def main():
    table_name = get_dynamodb_table_name()
    with create_batch_writer(table_name) as batch:
        for i in range(110000):
            item = {
                'id': create_md5_hexdigest(i + 1)
            }
            batch.put_item(item)


if __name__ == '__main__':
    main()
