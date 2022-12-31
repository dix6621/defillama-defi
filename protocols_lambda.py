import json
from s3_functions import s3_pd_read_csv, s3_write_json
from llama_functions import llama_protocols

import datetime
end_date = datetime.date.today()

def lambda_handler(event, context):
    
    data_dict = {'protocols': llama_protocols()}

    s3_write_json('dataspartan-test-bucket', f'defillama-analytics/raw-data/protocols/results/llama_protocols_{end_date}.json', data_dict)
