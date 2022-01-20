from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy


# INIT
app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "Video(name={name}, views={views}, likes={likes})"

# @app.before_first_request
# def before_first_request():
# db.create_all()


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Type should be string")
video_put_args.add_argument("views", type=int, help="Type should be int")
video_put_args.add_argument("likes", type=int, help="Type should be int")


videos = {

}

# def abort404(video_id):
#     if video_id not in videos:
#         abort(404, message=f"video id '{video_id}' not exists")
#
# def abort_if_video_exist(video_id):
#     if video_id not in videos:
#         abort(409, message=f"video id '{video_id}' already in records")

resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer,
}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        # abort404(video_id)
        return videos.get(video_id)

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        # abort_if_video_exist(video_id)
        video = VideoModel(id=args['id'], name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()

        videos[video_id] = args
        return {video_id: args}

    def delete(self, video_id):
        args = video_put_args.parse_args()
        # abort404(video_id)
        del videos[video_id]
        return ' ', 204

api.add_resource(Video, '/video/<int:video_id>')

if __name__ == "__main__":
    app.run(debug=True)