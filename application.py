from flask import Flask
from flask_restful import Resource, Api

app=Flask(__name__)
api=Api(app)

application_info = {
    "service_name": "myapplication",
    "version": "1.0.0",
    "git_commit_sha": "abc57858585",
    "environment": {
    "service_port": "8080",
    "log_level": "INFO"
    }
    }
class Application(Resource):
    def get(self):
        return application_info

api.add_resource(Application,"/info")
app.run(port=8080,host="0.0.0.0")

