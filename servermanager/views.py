from os import kill
from signal import SIGKILL
from subprocess import Popen

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
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


@login_required(login_url='login')
def params_server(request, server_id):
    server = get_object_or_404(Server, pk=server_id)
    print(request.POST)
    if 'params' in request.POST:
        server.params = request.POST['params']
        server.save()
        return HttpResponse()
    else:
        print('cant find params')
        return HttpResponseBadRequest()
