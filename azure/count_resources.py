
"""
References:

https://docs.microsoft.com/en-us/azure/governance/resource-graph/overview
https://docs.microsoft.com/en-us/azure/governance/resource-graph/first-query-python
"""

import csv
from datetime import datetime

# Azure Libraries
import azure.mgmt.resourcegraph as azr_resource_graph
from azure.mgmt.resource import SubscriptionClient
from azure.identity import AzureCliCredential


def controller():
    results = query_azr_resource_graph("Resources | summarize count() by subscriptionId, type, location | order by subscriptionId, type, location")
    data = results.data
    now = datetime.now()
    datetime_formatted = now.strftime("%Y%m%d-%H%M%S")

    with open(f'azure-resources-{datetime_formatted}.csv', 'w') as f:
        """
        Sample output in CSV file:
            subscription,resource_type,location,count
            42ca202f-3115-486f-9316-45ebb32683db,microsoft.storage/storageaccounts,southeastasia,1
        """
        writer = csv.writer(f)
        writer.writerow(['subscription','resource_type', 'location', 'count'])
        for item in data:
            writer.writerow([
                item.get('subscriptionId'),
                item.get('type'),
                item.get('location'),
                item.get('count_')]
            )


def query_azr_resource_graph(strQuery):
    """
    Sample output of resource graph query:
        {
            'additional_properties': {},
            'total_records': 1,
            'count': 1,
            'result_truncated': 'false',
            'skip_token': None,
            'data': [
                {'subscriptionId': '42ca202f-3115-486f-9316-45ebb32683db', 'type': 'microsoft.storage/storageaccounts', 'location': 'southeastasia', 'count_': 1},
                ...
            ], 
            'facets': []
        }
    """
    # Fetch credentials
    credentials = AzureCliCredential()

    subsClient = SubscriptionClient(credentials)
    subscriptions = subsClient.subscriptions.list()
    print('------------')
    print('The following subscriptions will be included in the Resource Graph Query')
    for sub in subscriptions:
        print(f"Subscription id: {sub.subscription_id}, name: {sub.display_name}")
    print('------------')

    subscription_ids = [sub.get('subscription_id') for sub in subscriptions]

    # Create Azure Resource Graph client and set options
    argClient = azr_resource_graph.ResourceGraphClient(credentials)
    argQueryOptions = azr_resource_graph.models.QueryRequestOptions(result_format="objectArray")

    # Create query
    argQuery = azr_resource_graph.models.QueryRequest(subscriptions=subscription_ids, query=strQuery, options=argQueryOptions)

    # Run query
    argResults = argClient.resources(argQuery)
    return argResults


if __name__ == "__main__":
    controller()
