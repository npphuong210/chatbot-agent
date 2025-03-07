from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Conversation(models.Model):
    id = models.AutoField(primary_key=True)
    prompt_name = models.CharField(max_length=100) # character name
    gpt_model = models.CharField(max_length=100) # provider
    chat_history = ArrayField(models.JSONField(), default=list, null=True, blank=True) # {"message_type": "ai_message or human_message", "content": "hello"}
    meta_data = models.JSONField(default=dict, null=True, blank=True)

    def __str__(self):
        return f"{self.id}"

class SystemPrompt(models.Model):
    id = models.AutoField(primary_key=True)
    character = models.CharField(max_length=100, unique=True)
    prompt = models.TextField()
    def __str__(self):
        return self.character

class Lecture(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100)
    chapter = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return f"{self.subject} - {self.chapter}"