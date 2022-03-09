import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

mensagem = MIMEMultipart()
mensagem_enviada = 'Relatorio semanal de atividades da sua residência'

senha = '   '  # Senha do email
mensagem['De'] = '  ' # Seu e-mail
mensagem['Para'] = ' ' # E-mail do destinatário
mensagem['Assunto'] = 'Relatório Semanal'

mensagem.attach(MIMEText(mensagem_enviada, 'plain'))
servidor = smtplib.SMTP('smtp.office365.com', port=587) # Protocolo SMTP do Outlook
servidor.starttls()
servidor.login(mensagem['De'], senha)
servidor.sendmail(mensagem['De'], mensagem['Para'], mensagem.as_string())
servidor.quit()


