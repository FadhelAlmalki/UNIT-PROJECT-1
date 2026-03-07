import json

def load_json(file_path):
    '''Load JSON data from a file'''
    with open(file_path, 'r', encoding="utf-8") as file:
        return json.load(file)
    
def save_json(file_path, data):
    '''Save JSON data to a file'''
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)