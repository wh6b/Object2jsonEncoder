# Object2jsonEncoder
Custom JSON

WARNING : Do not use in production orsecure it with reverse proxy or webapp authentication
because eval() is used without sanitization easy codeinjection and information extraction


Example with starlette

add to your view
```
from your.package import Object2jsonEncoder
# [...]
  @app.route("/debug/{item}", methods=["GET"])

  def debug_get_item(request):
    v = json.dumps( eval( request.path_params['item'] ), indent=4, cls=Object2jsonEncoder )
    return JSONResponse({"session": json.loads(v) })
