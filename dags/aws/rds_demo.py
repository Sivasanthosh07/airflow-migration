import boto3
import time
from aws.InstanceWrapper import from_client
import logging
class RdsInstanceScenario:
    """Runs a scenario that shows how to get started using Amazon RDS DB instances."""
    def __init__(self, instance_wrapper):
        """
        :param instance_wrapper: An object that wraps Amazon RDS DB instance actions.
        """
        self.instance_wrapper = instance_wrapper

        """
        Shows how to get the parameters contained in a custom parameter group and
        update some of the parameter values in the group.

        :param parameter_group_name: The name of the parameter group to query and modify.
        """
      

    def create_instance(self, instance_name):
        """
        Shows how to create a DB instance that contains a database of a specified
        type and is configured to use a custom DB parameter group.

        :param instance_name: The name given to the newly created DB instance.
        :param db_name: The name given to the created database.
        :param db_engine: The engine of the created database.
        :param parameter_group: The parameter group that is associated with the DB instance.
        :return: The newly created DB instance.
        """
        print("Checking for an existing DB instance.")
        db_inst =None
        try:
            db_inst = self.instance_wrapper.describe_db_instances(DBInstanceIdentifier=instance_name)
        except:
            print("Error Occured")
        if db_inst is None:
            print("Let's create a DB instance.")
            admin_username = "postgres"
            admin_password = "postgres"
            db_inst = self.instance_wrapper.create_db_instance( 
                AllocatedStorage=10,
                DBName="test",
                DBInstanceIdentifier=instance_name,
                DBInstanceClass="db.t3.micro",
                Engine="postgres",
                MasterUsername="postgres",
                MasterUserPassword="postgres",
                Port=5432,
                MultiAZ=False)
            while db_inst.get('DBInstanceStatus') != 'available':
                time.sleep(10)
                db_inst = self.instance_wrapper.describe_db_instances(DBInstanceIdentifier=instance_name)
        print("Instance data:")
        print(db_inst)
        print('-'*88)
        return db_inst

    def display_connection(self,instance_name):
        """
        Displays connection information about a DB instance and tips on how to
        connect to it.

        :param db_inst: The DB instance to display.
        """
        db_inst=self.instance_wrapper.describe_db_instances(DBInstanceIdentifier=instance_name)
        db_inst=db_inst["DBInstances"][0]
        print(db_inst)
        print(f"\n {db_inst['Endpoint']['Address']} -P {db_inst['Endpoint']['Port']} "
              f"-u {db_inst['MasterUsername']} -p\n")
        # print("For more information, see the User Guide for Amazon RDS:\n"
        #       "\thttps://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html#CHAP_GettingStarted.Connecting.MySQL")
        print('-'*88)
        return db_inst['Endpoint']['Address'],db_inst['Endpoint']['Port']


    def run_scenario(self, instance_name):
        logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

        print('-'*88)
        print("Welcome to the Amazon Relational Database Service (Amazon RDS)\n"
              "get started with DB instances demo.")
        print('-'*88)


        db_inst = self.create_instance(instance_name)
        # self.display_connection(self.instance_wrapper.describe_db_instances(DBInstanceIdentifier=instance_name))
        print('-'*88)
        
    def run_crete_db(instance_name):
        scenario = RdsInstanceScenario(from_client())
        scenario.run_scenario(instance_name)
    def get_connection(instance_name):
        scenario = RdsInstanceScenario(from_client())
        return scenario.display_connection(instance_name)


if __name__ == '__main__':
    try:
        scenario = RdsInstanceScenario(from_client())
        scenario.run_scenario('docexampledb')
    except Exception:
        logging.exception("Something went wrong with the demo.")

