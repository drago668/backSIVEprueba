from django.utils import timezone
from django.template.loader import render_to_string
from django.http import HttpResponse
from xhtml2pdf import pisa
from io import BytesIO
from api.controllers.optical_controller import OpticalTopViewedController
from permissions import IsAdminUser
from api.models import Optical, User  # Asegúrate de importar tu modelo Optical
from rest_framework import status, generics

class createReport(generics.GenericAPIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        # 🔹 Obtener directamente las ópticas más vistas (Top 5)
        top_opticals = Optical.objects.order_by('-view')[:5]

        # 🔹 Datos del administrador
        name_admin = request.user.get_full_name()

        # 🔹 Contexto del template
        context = {
            'titulo': "Reporte de Ópticas Más Vistas",
            'nombre_admin': name_admin,
            'top_opticas': top_opticals,
            'fecha_generacion': timezone.now(),
        }

        # 🔹 Renderizar el HTML del reporte
        html_string = render_to_string('reportOptical.html', context)

        # 🔹 Crear el PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="reporte_opticas_mas_vistas.pdf"'
        buffer = BytesIO()

        pisa_status = pisa.pisaDocument(
            BytesIO(html_string.encode("UTF-8")),
            buffer,
            link_callback=lambda uri, rel: request.build_absolute_uri(uri)
        )

        if not pisa_status.err:
            response.write(buffer.getvalue())
            return response

        return HttpResponse(
            f"Error al generar el PDF: {pisa_status.err}",
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )