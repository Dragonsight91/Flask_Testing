from markupsafe import escape

def api_call(api_endpoint:str) -> str:
    return f"you requested the endpoint {escape(api_endpoint)}? I delivered"