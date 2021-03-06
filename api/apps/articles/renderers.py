from api.apps.core.renderers import ApiJSONRender


class ArticleJSONRenderer(ApiJSONRender):
    object_label = "article"
    pagination_object_label = "articles"
    pagination_count_label = "articlesCount"
