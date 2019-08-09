from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Question


# Question Admin
class QuestionAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Question, QuestionAdmin)
