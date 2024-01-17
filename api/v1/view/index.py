from api.v1.views import app_views
from flack import jsonify
from models.engine import storage
from models.engine.db_storage import classes


@app_views.route('/status' )
def status():
    return jsonify({ "status": "OK" })

@app_views.route('/stats')
def stats_handler():

    stats =  { \
            [key.lower() + "s" \
            if not key.endswith("y") \
            else key.lower()[:-1] + "is"]: storage.count(cls) \
            for key, cls in classes.items() \
            if storage.count(cls) > 0 \
    }


    return jsonify(stats)

