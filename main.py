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


resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer,
}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        video = VideoModel.query.filter_by(id=video_id).first_or_404('id wasn\'t found')
        return video

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        video = VideoModel.query.filter_by(id=video_id).first()
        if video:
            video.name = args.get('name')
            video.likes = args.get('likes')
            video.views = args.get('views')
            db.session.add(video)
            db.session.commit()
        else:
            video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
            db.session.add(video)
            db.session.commit()
        return video

    def delete(self, video_id):
        args = video_put_args.parse_args()
        video = VideoModel.query.filter_by(id=video_id).first_or_404('id wasn\'t found')
        db.session.delete(video)
        db.session.commit()
        return ' ', 204

api.add_resource(Video, '/video/<int:video_id>')

if __name__ == "__main__":
    app.run(debug=True)