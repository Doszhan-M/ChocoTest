import json

from rest_framework.renderers import JSONRenderer


class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):

        errors = data.get('errors', None)
        token = data.get('token', None)

        if errors is not None:
            # Если ошибка стандартная, то передаем ее на JSONRenderer.
            return super(UserJSONRenderer, self).render(data)

        if token is not None and isinstance(token, bytes):
            # декодирует token если он имеет тип bytes.
            data['token'] = token.decode('utf-8')

        # Передать данные в пространстве имен 'user'.
        return json.dumps({
            'user': data
        })