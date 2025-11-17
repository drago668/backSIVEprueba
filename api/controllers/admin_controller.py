from rest_framework.decorators import api_view, permission_classes
from permissions import IsAdminUser
from rest_framework.response import Response
from api.models.user import User
from api.serializers import UsersSerializers , OpticalListSerializers
from api.models import Optical , User, Role

# Listar ópticas pendientes
@api_view(['GET'])
@permission_classes([IsAdminUser])
def pending_optics(request):
    pending = Optical.objects.filter(is_verified=False)
    data = [
        {
            "id_optical": o.id_optical,
            "name": o.nameOp,
            "user_id": o.user.id,
            "user_email": o.user.email,
            "peding" : o.is_verified
        } for o in pending
    ]
    return Response(data, status=200)

# Aprobar dueño
@api_view(['POST'])
@permission_classes([IsAdminUser])
def approve_optic_owner(request, optic_id):
    try:
        optic = Optical.objects.get(id_optical=optic_id, is_verified=False)
    except Optical.DoesNotExist:
        return Response({"error": "Óptica no encontrada"}, status=404)

    user = optic.user
    if not user:
        return Response({"error": "Usuario no encontrado"}, status=404)

    optic.is_verified = True
    optic.save()

    user.role = Role.objects.get(id=2)  # Asignar rol de dueño
    user.is_verified_owner = True
    user.save()

    return Response({"message": "Dueño aprobado correctamente"}, status=200)

# Rechazar dueño
@api_view(['POST'])
@permission_classes([IsAdminUser])
def reject_optic_owner(request, optic_id):
    try:
        optic = Optical.objects.get(id_optical=optic_id, is_verified=False)
    except Optical.DoesNotExist:
        return Response({"error": "Óptica no encontrada"}, status=404)

    user = optic.user
    if not user:
        return Response({"error": "Usuario no encontrado"}, status=404)

    # Eliminar la óptica y mantener al usuario con rol normal
    optic.delete()
    user.is_verified_owner = False
    user.save()

    return Response({"message": "Dueño rechazado correctamente"}, status=200)

