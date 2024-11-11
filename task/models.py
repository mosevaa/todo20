from django.db.models import (
    CharField,
    DateTimeField,
    TextField,
    ForeignKey,
    Model, 
    CASCADE,
    SET_NULL,
    TextChoices
)
from django.utils.translation import gettext_lazy as _
from user.models import User
from project.models import Project

class Task(Model):
    class TaskStatus(TextChoices):
        NEW = "NEW", _("Новая")
        PROCESSING = "PROCESSING", _("В процессе")
        DONE = "DONE", _("Сделана")

    name = CharField(max_length=50, null=False)
    description = TextField(null=True)
    project = ForeignKey(Project, null=False, on_delete=CASCADE)
    created_by = ForeignKey(User, on_delete=SET_NULL, null=True, related_name="creator")
    created_at = DateTimeField(null=False, auto_now_add=True)
    performer = ForeignKey(User, on_delete=SET_NULL, null=True, related_name="performer")
    status = CharField(max_length=30, choices=TaskStatus.choices, default=TaskStatus.NEW)
