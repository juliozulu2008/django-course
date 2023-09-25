from django.db import models
from datetime import datetime

# Create your models here.
#Os modelos (Models) definem a estrutura do banco de dados
# Unica Fonte definitiva de acesso aos Dados

class Post(models.Model): # Classe post é um subclasse de Model
    autor = models.CharField(max_length=255) # Limitaçao de 255 caracteres
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(default=datetime.now())

"""
Baseado nessa classe o Django ira criar uma tabela no Db com as colunas autor,
titulo, subtitulo, conteúdo, e data de publicação, os campos serao do yipo varchar, timestamp
"""
