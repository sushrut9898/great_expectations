from ruamel import yaml
import great_expectations as ge
from integration.code.connecting_to_your_data.database.util import (
    load_data_into_database,
)


sfAccount = "oca29081.us-east-1"
sfUser = "will"
sfPswd = "F24th4r@2234we"

CONNECTION_STRING = "snowflake://<user_login_name>:<password>@<account_name>/<database_name>/<schema_name>?warehouse=<warehouse_name>&role=<role_name>"

CONNECTION_STRING = f"""snowflake://{sfUser}:{sfPswd}@{sfAccount}/SUPERCONDUCTIVE/NYC_TAXI?warehouse=COMPUTE_WH"""
load_data_into_database(
    "taxi_data",
    "./data/reports/yellow_tripdata_sample_2019-01.csv",
    CONNECTION_STRING,
)

#context = ge.get_context()
context = ge.DataContext(
    context_root_dir="../../../fixtures/runtime_data_taxi_monthly/great_expectations"
)

# with a connection_string
config = """
name: my_snowflake_datasource
class_name: Datasource
execution_engine:
  class_name: SqlAlchemyExecutionEngine
  connection_string: <YOUR_CONNECTION_STRING_HERE>
data_connectors:
   default_runtime_data_connector_name:
       class_name: RuntimeDataConnector
       batch_identifiers:
           - default_identifier_name
   default_inferred_data_connector_name:
       class_name: InferredAssetSqlDataConnector
       name: whole_table
"""
config = config.replace("<YOUR_CONNECTION_STRING_HERE>", CONNECTION_STRING)

# with a environment_variable
config = """
name: my_snowflake_datasource
class_name: Datasource
execution_engine:
  class_name: SqlAlchemyExecutionEngine
  connection
data_connectors:
   default_runtime_data_connector_name:
       class_name: RuntimeDataConnector
       batch_identifiers:
           - default_identifier_name
   default_inferred_data_connector_name:
       class_name: InferredAssetSqlDataConnector
       name: whole_table
"""
config = config.replace("<YOUR_CONNECTION_STRING_HERE>", CONNECTION_STRING)




context.add_datasource(**yaml.load(config))

# First test for RuntimeBatchRequest using a query
batch_request = ge.core.batch.RuntimeBatchRequest(
    datasource_name="my_snowflake_datasource",
    data_connector_name="default_runtime_data_connector_name",
    data_asset_name="default_name",  # this can be anything that identifies this data_asset for you
    runtime_parameters={"query": "SELECT * from TAXI_DATA LIMIT 10"},
    batch_identifiers={"default_identifier_name": "something_something"},
)
suite = context.create_expectation_suite("my_test_suite", overwrite_existing=True)
# profiler

my_validator = context.get_validator(
  batch_request=batch_request,
  expectation_suite=suite
)

print(my_validator.head())

# # Second test for BatchRequest naming a table
batch_request = ge.core.batch.BatchRequest(
    datasource_name="my_snowflake_datasource",
    data_connector_name="default_inferred_data_connector_name",
    data_asset_name="TAXI_DATA",  # this is the name of the table you want to retrieve
)
context.create_expectation_suite(
    expectation_suite_name="test_suite", overwrite_existing=True
)
validator = context.get_validator(
    batch_request=batch_request, expectation_suite_name="test_suite"
)
print(validator.head())
