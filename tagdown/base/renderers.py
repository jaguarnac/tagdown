'''
'''
import json
from bson import json_util
def mongo_json_serializer(obj, default):
    return json.dumps(obj, default=json_util.default)