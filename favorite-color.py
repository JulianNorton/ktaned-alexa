from lambda_function import lambda_handler
import json

#with open('sample.json', 'r') as f:
event_data = json.load(open('sample.json'))
print(lambda_handler(event_data,''))