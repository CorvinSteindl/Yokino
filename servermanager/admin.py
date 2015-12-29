from django import forms
from django.contrib import admin

from .models import Server, ServerInstance

# Register your models here.

admin.site.register(ServerInstance)


class ServerAdminForm(forms.ModelForm):

    class Meta:
        exclude = []
        model = Server
        widgets = {
            'type': forms.Select(choices=(
                ('srcds.exe', 'CS:GO'), ('arma3server.exe', 'ARMA III'))
            )
        }


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    form = ServerAdminForm
