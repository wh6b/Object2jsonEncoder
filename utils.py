import ctypes
import json
import logging
import re
from datetime import datetime

class Object2jsonEncoder(json.JSONEncoder):
  def default(self, obj):
    #logging.debug(o)
    #logging.debug(type(o))
    try :
      return { str(obj) : obj.__dict__ }
    except:
      if isinstance(obj, datetime):
        return {'<datetime>': obj.replace(microsecond=0).isoformat()}
      #elif isinstance(obj, some_type):
        # Put here your custom format
      else:
        return "{}".format(str(obj))
