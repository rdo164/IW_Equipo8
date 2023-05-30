import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email(destinatario, asunto, contenido):
    # Configuración del servidor SMTP y credenciales de autenticación
    servidor_smtp = 'smtp.gmail.com'
    puerto_smtp = 587
    remitente = 'alex.cue@opendeusto.es'
    password = 'zcfabkixwmwailyw'

    # Crear el objeto de mensaje MIME
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto

    # Agregar el contenido del mensaje
    cuerpo_mensaje = MIMEText(contenido, 'plain')
    mensaje.attach(cuerpo_mensaje)

    # Establecer conexión con el servidor SMTP
    servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
    servidor.starttls()
    servidor.login(remitente, password)

    # Enviar el correo electrónico
    servidor.send_message(mensaje)
    servidor.quit()