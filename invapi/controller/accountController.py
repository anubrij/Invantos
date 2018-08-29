from invapi.model import user, usersecurity
from .. import create_app
app = create_app()
@app.route("/")
def Hello():
    return "Hello"
