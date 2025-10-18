# En un archivo como core/auth.py

from drf_spectacular.extensions import OpenApiAuthenticationExtension
from drf_spectacular.utils import extend_schema_security

class KnoxTokenScheme(OpenApiAuthenticationExtension):
    target_class = 'knox.auth.TokenAuthentication'
    name = 'tokenAuth' # Debe coincidir con el nombre en settings

    def get_security_definition(self, auto_schema):
        return {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': "Token-based authentication with Knox. Use the format 'Token <YOUR_TOKEN>'."
        }
