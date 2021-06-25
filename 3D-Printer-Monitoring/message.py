import smtplib # Biblioteca do python
import numpy as np    
    
with open('contatos.txt','r') as x: # Abre o arquivo com os contatos que receberam o e-mail
    contatos = x.read().split()
    
with open('mensagem.txt','r') as y: # Abre a mensagem que será enviada 
    mensagem = y.read()
    
# with open('mensagem2.txt','r') as z: # Mensagem de finalização 
#     mensagem2 = z.read()

# Login na conta que enviará a mensagem

gmail_user = 'echinho.ras@gmail.com' 
gmail_password = 'mariobordon' # Não me hackeia xD

sent_from = gmail_user
to = contatos
subject = 'Status sobre a Impressora 3D'
body = mensagem

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465) # Conectando ao servidor
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('O e-mail foi enviado com sucesso!')
except:
    print('Não foi possível enviar o e-mail.')