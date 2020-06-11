from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface


class GroupModelView(ModelView):
    datamodel = SQLAInterface(Post)
    related_views = [PostModelView]


class PostModelView(ModelView):
    datamodel = SQLAInterface(Post)
