import logging
from flask.views import MethodView
from flask import render_template, request
from versionfinder import find_version

from biweeklybudget.flaskapp.app import app
from biweeklybudget.version import VERSION, PROJECT_URL
from biweeklybudget.settings import DB_CONNSTRING

logger = logging.getLogger(__name__)

for lname in ['versionfinder', 'pip', 'git']:
    l = logging.getLogger(lname)
    l.setLevel(logging.CRITICAL)
    l.propagate = True


class PoolView(MethodView):
    """
    Render the GET /pool view using the ``pool.html`` template.
    """

    def get(self):
        return render_template(
            'pool.html',
            version=VERSION,
            url=PROJECT_URL,
            ua_str=request.headers.get('User-Agent', 'unknown'),
            db_uri=DB_CONNSTRING
        )


app.add_url_rule('/pool', view_func=PoolView.as_view('pool_view'))
