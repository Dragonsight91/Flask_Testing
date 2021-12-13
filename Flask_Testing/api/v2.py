from markupsafe import escape
from flask import url_for

def api_call(api_endpoint:str, api_group:str) -> str:
    return f"<p>you requested the endpoint <b>{escape(api_endpoint)}</b> in the <b>{escape(api_group)}</b> group? I delivered, but wait, this is something new!!</p><p>URL: {url_for('api', version='v1', api_group=api_group, api_endpoint=api_endpoint)}</p>"