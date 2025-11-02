from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.dispatch import receiver

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    user_name = reset_password_token.user.username or reset_password_token.user.email
    reset_link = f"http://localhost:5173/password_reset?token={reset_password_token.key}"

    context = {
        "user": user_name,
        "reset_link": reset_link,
    }

    # 🔹 Renderizamos el HTML
    html_content = render_to_string(
    "api/email.html",
    {
        "email_adress": reset_password_token.user.email,
        "full_link": f"{settings.FRONTEND_BASE_URL}/password_reset?token={reset_password_token.key}"
    }
)


    text_content = f"Hola {user_name}, usa este enlace para restablecer tu contraseña: {reset_link}"

    print("📤 Enviando correo con contexto:", context)
    print("📄 HTML renderizado:", html_content[:200], "...")  # (muestra los primeros 200 caracteres)

    # 🔹 Creamos el mensaje en modo alternativo (texto + HTML)
    msg = EmailMultiAlternatives(
        subject="Restablecer tu contraseña - SIVE",
        body=text_content,  # texto plano
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[reset_password_token.user.email],
    )
    msg.attach_alternative(html_content, "text/html")
    print("📩 Contexto enviado:", {
    "user": reset_password_token.user.username,
    "reset_link": f"{settings.FRONTEND_BASE_URL}/password_reset?token={reset_password_token.key}",
    })

    # 🔹 Enviamos
    msg.send()
    print("✅ Correo enviado correctamente a", reset_password_token.user.email)
