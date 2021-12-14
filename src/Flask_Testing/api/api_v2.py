from flask import Blueprint, url_for
from markupsafe import escape

bp = Blueprint('api_v2', __name__, url_prefix="/api/v2")

@bp.route('/testing/<string:api_endpoint>')
def testing(api_endpoint:str):
    return (
        f"<p>you requested the endpoint <b>{escape(api_endpoint)}</b>?</br>"
        + f"I delivered, but wait, this is something new!!</p><p>URL: {url_for('api_v1.testing', api_endpoint=api_endpoint)}</p>"
    )
