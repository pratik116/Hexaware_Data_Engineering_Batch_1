import json

def get_column_details(json_file_path, column_name):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        
    columns = data.get('columns', [])
    print(columns)
    for column in columns:
        if column.get('name') == column_name:
            return column
    
    return None  # Return None if column_name is not found

# Example usage:
schema_json_file = 'test.json'
column_name_to_search = 'age'

column_details = get_column_details(schema_json_file, column_name_to_search)
if column_details:
    print("Column Details:")
    print(column_details)
else:
    print(f"Column '{column_name_to_search}' not found in schema.")
