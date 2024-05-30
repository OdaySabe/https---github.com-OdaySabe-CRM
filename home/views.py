from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from .models import Agents
from login.models import Role
from .permissions import has_edit_perm,has_create_perm,has_delete_perm,has_view_perm
import json


@has_view_perm    
def home(request):
    if hasattr(request.user, 'role'):
        user_role = request.user.role.type
    elif request.user.is_staff:
         user_role='Admin'
    if request.method == "GET":
        agents = Agents.objects.all().order_by('id')
        role_choices = Role.ROLE_CHOICES
    return render(request, "home.html", {"pagename": "home", 'agents': agents, 'role_choices': role_choices,'user_role':user_role})

@has_create_perm
def create_agent(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('UTF-8')).get('data')
        try:
            role = Role(type=data.get('role'))
            if data.get('role') != 'OnlyAgent':
                user=User(username=data.get('first_name')+'.'+data.get('last_name'),password=data.get('password'))
                user.set_password(user.password)
                user.save()
                role.user=user
            role.save()
            agent = Agents(first_name=data.get('first_name'), last_name=data.get('last_name'), role=role, country=data.get('country'), age=data.get('age'), balance=data.get('balance'))
            agent.save()
            return JsonResponse({'Success': True, 'ID': agent.id})
        except Exception as e:
            return JsonResponse({'Success': False, 'error': str(e)})
    else:
        return JsonResponse({'Success': False, 'error': 'Method not allowed'}, status=405)
    
@has_delete_perm
def delete_agent(request):
    if request.method == 'DELETE':
        data = json.loads(request.body.decode('UTF-8')).get('data')
        try:
            Agents.objects.get(id=data).delete()
            return JsonResponse({'Success': True, 'ID': data})
        except Exception as e:
            return JsonResponse({'Success': False, 'error': str(e)})
    else:
        return JsonResponse({'Success': False, 'error': 'Method not allowed'}, status=405)
@has_edit_perm
def update_agent(request):
    if request.method == 'PUT':
        data = json.loads(request.body.decode('UTF-8')).get('data')
        agent = Agents.objects.get(id=data.get('id'))
        del data['id']
        for key, value in data.items():
            if key=='role':
                agent.role.type=data.get('role')
                agent.role.save()
            else:
                setattr(agent, key, value)
        agent.save()
        return JsonResponse({'Success': True})
    else:
        return JsonResponse({'Success': False, 'error': 'Method not allowed'}, status=405)

        
