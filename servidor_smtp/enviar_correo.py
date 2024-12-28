import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from analisis_objetos.analisis import token, hash_blockchain
logging.basicConfig(level=logging.DEBUG)

def enviar_correo(token, hash_imagen, destinatario):
    mensaje = MIMEMultipart('alternative')
    mensaje['Subject'] = 'Información del Token y Hash de Imagen'
    mensaje['From'] = 'ucvcrypto@gmail.com'
    mensaje['To'] = destinatario

    try:
        servidor_smtp = 'smtp.gmail.com'
        puerto_smtp = 587
        remitente = 'ucvcrypto@gmail.com'
        contrasena = 'ruvx eslt pdub pgon'  # Asegúrate de usar una contraseña segura

        servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
        servidor.starttls()
        servidor.login(remitente, contrasena)

        mensaje_texto = f"Token: {token}\nHash de la imagen: {hash_imagen}"
        mensaje.attach(MIMEText(mensaje_texto, 'plain'))

        servidor.sendmail(remitente, destinatario, mensaje.as_string())
        print("Correo enviado exitosamente.")
    except smtplib.SMTPException as e:
        print(f"Error al enviar el correo: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        servidor.quit()

# Ejemplo de uso
token = token
hash_imagen = hash_blockchain
destinatario = "mixie.brighit01@gmail.com"

enviar_correo(token, hash_imagen, destinatario)