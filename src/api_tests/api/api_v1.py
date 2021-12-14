from flask import Blueprint, url_for
from markupsafe import escape

bp = Blueprint('api_v1', __name__, url_prefix="/api/v1")

@bp.route('/testing/<string:api_endpoint>')
def testing(api_endpoint:str):
    return (
        f"<p>you requested the endpoint <b>{escape(api_endpoint)}</b>?<br>"
        + f"I delivered!"
    )
