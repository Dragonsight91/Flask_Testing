from markupsafe import escape
from flask import url_for


def api_call(api_endpoint: str) -> str:
    return (
        f"<p>you requested the endpoint <b>{escape(api_endpoint)}</b> ?"
        + f"I delivered, but wait, this is something new!!</p><p>URL: {url_for('api', version='v1', api_endpoint=api_endpoint)}</p>"
    )
