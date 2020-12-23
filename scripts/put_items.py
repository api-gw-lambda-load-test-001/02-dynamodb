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


def main():
    table_name = get_dynamodb_table_name()
    print(table_name)


if __name__ == '__main__':
    main()
