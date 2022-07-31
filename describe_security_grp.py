# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError
import json

AWS_REGION = input("Please enter the AWS_REGION")

# this is the configration for the logger

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

vpc_client = boto3.client("ec2", region_name=AWS_REGION)


def describe_group(tag, tag_values, max_items):

    try:
        paginator = vpc_client.get_paginator('describe_group')

        response_iterator = paginator.paginate(
            Filters=[{
                'Name': f'tag:{tag}',
                'Values': tag_values
            }],
            PaginationConfig={'MaxItems': max_items})

        full_result = response_iterator.build_full_result()

        security_groups_list = []

        for page in full_result['SecurityGroups']:
            security_groups_list.append(page)

    except ClientError:
        logger.exception('Security Groups can not be describe.')
        raise
    else:
        return security_groups_list


if __name__ == '__main__':
    TAG = 'Name'
    TAG_VALUES = ['Techhub_template_grp']
    MAX_ITEMS = 10
    security_groups = describe_group(TAG, TAG_VALUES, MAX_ITEMS)
    logger.info('This is your Security Groups details: ')
    for security_group in security_groups:
        logger.info(json.dumps(security_groups, indent=4) + '\n')