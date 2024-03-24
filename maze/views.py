from django.shortcuts import render
import json
from django.http import JsonResponse
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_ABSOLUTE_DIR = os.path.join(BASE_DIR, 'maze/')
APP_DIR = 'maze/'
# import appname
# pth = os.path.dirname(appname.__file__)
# Create your views here.

posts = [
    {
        'Name': 'A',
        'content': 'a',
        'date': '2024/1/1'
    },
    {
        'Name': 'B',
        'content': 'b',
        'date': '2024/1/2'
    }
]

def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'maze/home.html', context)

def play(request):
    # maze_json_file = open('Maze.json')
    # maze_json = json.load(maze_json_file)
    maze_json = {}
    try:
        with open(os.path.join(APP_DIR,'files/Maze.json')) as f:
            data = json.load(f)
        # return JsonResponse(data)
        maze_json = data
        svg = {}
        wall_coord = []

        offsetx = 10
        offsety = 10
        len_each = 30
        lineWidth = 3.5
        for wall in maze_json["wall"]:
            x1 = wall["coordinate"][1]*len_each
            y1 = wall["coordinate"][0]*len_each
            if (wall["isHorizontal"]):
                x2, y2 = x1+len_each, y1
                x1 -= lineWidth/2
                x2 += lineWidth/2
            else:
                x2, y2 = x1, y1+len_each
                y1 -= lineWidth/2
                y2 += lineWidth/2
            x1, x2 = map(lambda k: k+offsetx, [x1,x2])
            y1, y2 = map(lambda k: k+offsety, [y1,y2])
            wall_coord.append({'x1':x1, 'x2':x2, 'y1':y1, 'y2':y2})
        svg["width"] = max([i['x2'] for i in wall_coord])+offsetx
        svg["height"] = max([i['y2'] for i in wall_coord])+offsety
        svg["wall_coord"] = wall_coord
        svg["lineWidth"] = lineWidth
        svg["color"] = "black"
        maze_json["svg"] = svg

        # print(maze_json)
            
    except FileNotFoundError:
        maze_json = {'error': 'File not found'}
        # return JsonResponse({'error': 'File not found', 'path': f'{os.getcwd()} ./files/Maze.json {BASE_DIR}'}, status=404)
    except Exception as e:
        maze_json = {'error': str(e)}
        # return JsonResponse({'error': str(e)}, status=500)
    context = {
        'title': 'Play',
        'posts': posts,
        'maze': maze_json
    }
    return render(request, 'maze/play.html', context)

def get_maze_json(request):
    try:
        with open(os.path.join(APP_DIR,'files/Maze.json')) as f:
            data = json.load(f)
        return JsonResponse(data)
    except FileNotFoundError:
        return JsonResponse({'error': 'File not found', 'path': f'{os.getcwd()} ./files/Maze.json {BASE_DIR}'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def test(request):
    context = {
        'title': 'test'
    }
    return render(request, 'maze/test.html', context)