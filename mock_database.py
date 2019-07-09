import json

def mock_database_write(data, file_name):
    json_data = mock_database_read(file_name)
    IDX = len(json_data) + 1
    json_data[IDX] = data
    with open(file_name, 'w') as cj:
        json.dump(json_data, cj, ensure_ascii=False, indent=4)

def mock_database_read(file_name):
    data = {}
    try:
        with open(file_name) as cj:
            data = json.load(cj)
    except IOError as ie:
        pass
    finally:        
        return data
