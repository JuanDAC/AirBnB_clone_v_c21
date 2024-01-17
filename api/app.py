from models import storage 
from api.v1.views import app_view
from flask import Flask
from os import getenv


app = Flack(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_storage(exception):
    storage.close()



if __name__ == "__main__":
    host = getenv(HBNB_API_HOST)
    port = getenv(HBNB_API_PORT)
    app.run(host=host, port=port, threaded=True)



