from email.message import EmailMessage
import ssl
import smtplib

def contacto(ingreso_asunto, ingreso_cuerpo ):

    email_emisor = "contaco.gim@gmail.com"
    email_contraseña = "nizvcnffjdwvxfij"
    email_receptor = "contaco.gim@gmail.com"

    asunto = ingreso_asunto
    cuerpo = ingreso_cuerpo

    em = EmailMessage()

    em["from"] = email_emisor
    em["To"] = email_receptor
    em["Subject"] = asunto
    em.set_content(cuerpo)

    contexto = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = contexto) as smtp:
        smtp.login(email_emisor, email_contraseña)
        smtp.sendmail(email_emisor, email_receptor, em.as_string())




#-------------------------------------------------------------------------------------
"""

email_emisor = "contaco.gim@gmail.com"
email_contraseña = "nizvcnffjdwvxfij"
email_receptor = "fabian.diego@gmail.com"

asunto = "Correo de contacto"
cuerpo = "Hola como estas"

em = EmailMessage()

em["from"] = email_emisor
em["To"] = email_receptor
em["Subject"] = asunto
em.set_content(cuerpo)

contexto = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = contexto) as smtp:
    smtp.login(email_emisor, email_contraseña)
    smtp.sendmail(email_emisor, email_receptor, em.as_string())

"""