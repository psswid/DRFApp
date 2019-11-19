from api.apps.core.renderers import ApiJSONRender


class EntryJSONRenderer(ApiJSONRender):
    object_label = "entry"
    pagination_object_label = "entries"
    pagination_count_label = "entriesCount"
