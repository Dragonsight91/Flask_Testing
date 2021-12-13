from markupsafe import escape

def api_call(endpoint:str, group:str) -> str:
    return f"you requested the endpoint {escape(endpoint)} in the {escape(group)} group? I delivered"