# from django.db import models
# from django.contrib.auth.models import User
#
#
# class ContactForm(models.Model):
#     name = models.CharField(max_length=200, help_text="Name of the sender")
#     email = models.EmailField(max_length=200)
#     subject = models.CharField(max_length=200)
#     message = models.TextField(max_length=500)
#     date = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name_plural = "Feedback"
#
#     def __str__(self):
#         return self.name + "-" + self.email
