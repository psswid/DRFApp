from api.apps.core.renderers import ApiJSONRender


class UserJSONRenderer(ApiJSONRender):
    object_label = "user"
    pagination_object_label = "users"
    pagination_count_label = "userCount"
