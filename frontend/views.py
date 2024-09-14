from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Task
from django.shortcuts import render
import json


def list_view(request):
    return render(request, 'list.html')

def get_tasks(request):
    tasks = list(Task.objects.values())
    return JsonResponse(tasks, safe=False)

@csrf_exempt
def add_task(request):
    if request.method == "POST":
        data = json.loads(request.body)
        
        if 'title' not in data or data['title'].strip() == '':
            return JsonResponse({'error': 'Task title is required'}, status=400)

        task = Task.objects.create(title=data['title'].strip(), completed=False)
        return JsonResponse({'id': task.id, 'title': task.title, 'completed': task.completed})


@csrf_exempt
def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return JsonResponse({'message': 'Task deleted'})

@csrf_exempt
def delete_all_tasks(request):
    if request.method == "DELETE":
        Task.objects.all().delete()
        return JsonResponse({'message': 'All tasks deleted'})
    return JsonResponse({'error': 'Invalid method'}, status=405)
