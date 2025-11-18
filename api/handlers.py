# api/handlers.py
from corsheaders.signals import check_request_enabled

def cors_allow_my_frontend(sender, request, **kwargs):
    origin = request.META.get('HTTP_ORIGIN')
    # Permitir el origen de tu frontend
    if origin == "https://sive-00qf.onrender.com":
        return True
    return None

check_request_enabled.connect(cors_allow_my_frontend)
