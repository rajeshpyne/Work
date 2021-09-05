from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)


class OlympicsMedal(Resource):
    def get(self):
        return {"weightlifting": "Mirabhai Chanu"}


api.add_resource(OlympicsMedal, "/")

if __name__ == "__main__":
    app.run(port=8081)
