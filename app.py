from app import app
import os
if __name__ == "__main__":
    # app.secret_key = os.urandom(24)
    # app.config['SESSION_TYPE'] = 'filesystem'
    #
    # session.init_app(app)
    app.run()