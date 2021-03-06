import json

from rest_framework.renderers import JSONRenderer


class ApiJSONRender(JSONRenderer):
    """Base api json render format with errors returning"""
    charset = "utf-8"
    object_label = "object"
    pagination_object_label = "objects"
    pagination_object_count = "count"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if data.get("results", None):
            return json.dumps(
                {
                    self.pagination_object_label: data["results"],
                    self.pagination_count_label: data["count"],
                }
            )

        elif data.get("errors", None):
            return super(ApiJSONRender, self).render(data)

        else:
            return json.dumps({self.object_label: data})
