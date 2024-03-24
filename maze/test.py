import json
import os
APP_DIR = 'maze/'
with open(os.path.join('.','files/Maze.json')) as f:
    data = json.load(f)
    # return JsonResponse(data)
maze_json = data
wall_coord = []

offsetx = 10
offsety = 10
len_each = 30
for wall in maze_json["wall"]:
    y1, x1 = wall["coordinate"]
    if (wall["isHorizontal"]):
        x2, y2 = x1+len_each, y1
    else:
        x2, y2 = x1, y1+len_each
    x1, x2 = map(lambda k: k+offsetx, [x1,x2])
    y1, y2 = map(lambda k: k+offsety, [y1,y2])
    wall_coord.append({x1:x1, x2:x2, y1:y1, y2:y2})
maze_json["wall_coord"] = wall_coord
print(maze_json)