import boto3
class InstanceWrapper:
    """Encapsulates Amazon RDS DB instance actions."""
    def __init__(self, rds_client):
        """
        :param rds_client: A Boto3 Amazon RDS client.
        """
        self.rds_client = rds_client

def from_client():
    rds_client = boto3.client('rds')
    return rds_client
