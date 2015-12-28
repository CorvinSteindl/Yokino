from os import kill
from subprocess import Popen
from signal import SIGKILL

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone

from .models import Server, ServerInstance


# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'servermanager/index.html', {
        'serverl': Server.objects.filter(owner=request.user)
    })


@login_required(login_url='login')
def server(request, server_id):
    server = get_object_or_404(Server, pk=server_id)
    return render(request, 'servermanager/server.html', {
        'serverl': Server.objects.filter(owner=request.user),
        'server': server
    })


@login_required(login_url='login')
def start_server(request, server_id):
    server = get_object_or_404(Server, pk=server_id)
    p = Popen([server.path + server.type, server.params])
    ServerInstance(pid=p.pid,
                   server=server,
                   start=timezone.now()).save()
    return redirect('server', server_id)


@login_required(login_url='login')
def stop_server(request, server_id):
    server = get_object_or_404(Server, pk=server_id)
    try:
        si = ServerInstance.objects.get(server=server)
    except DoesNotExist:
        return redirect('server', server_id)
    kill(si.pid, SIGKILL)
    si.delete()
    return redirect('server', server_id)
