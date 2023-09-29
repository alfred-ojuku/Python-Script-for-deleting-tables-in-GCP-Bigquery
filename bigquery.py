import os
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\Roam\\Desktop\\data-warehouse-355508-4c99e2f51463.json"

def delete_tables_with_pattern(project_id, dataset_id, pattern):
    client = bigquery.Client(project=project_id)
    dataset_ref = client.dataset(dataset_id)

    tables_to_delete = [
        table.table_id
        for table in client.list_tables(dataset_ref)
        if pattern in table.table_id
    ]
    print(tables_to_delete)
    for table_id in tables_to_delete:
        table_ref = dataset_ref.table(table_id)
        client.delete_table(table_ref)
        print(f"Deleted table: {table_id}")

if __name__ == "__main__":
    project_id = "roam-data-warehouse-355508"
    dataset_id = "Hubspot"
    pattern = "_airbyte_tmp_"  # Adjust this to your desired pattern

delete_tables_with_pattern(project_id, dataset_id, pattern)
