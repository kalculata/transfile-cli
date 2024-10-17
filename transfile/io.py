import json


def read_json_file(file_path):
  """Read and parse a JSON file."""
  with open(file_path, 'r', encoding='utf-8') as f:
    return json.load(f)
    
def read_properties_file(file_path):
  """Read and parse a .properties file."""
  properties = {}
  with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
      # Ignore comments and empty lines
      if line.strip() and not line.startswith('#'):
        key, value = line.split('=', 1)
        properties[key.strip()] = value.strip()
  return properties