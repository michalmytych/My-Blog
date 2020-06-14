from flask.views import MethodView
import app



class PostsAPI(MethodView):

    def GET(self):
        return "To jest post!"

    def POST(self):
        return 0

    def PUT(self):
        return 0

    def DELETE(self):
        return 0
    

app.add_url_rule('/posts', view_func=PostsAPI.as_view('post'))
