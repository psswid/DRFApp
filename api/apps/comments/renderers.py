from api import ApiJSONRender


class CommentJSONRenderer(ApiJSONRender):
    object_label = 'comment'
    pagination_object_label = 'comments'
    pagination_count_label = 'commentsCount'
