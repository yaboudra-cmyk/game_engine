import tkinter as tk
import math

root = tk.Tk()
root.title("3D Creator")
root.geometry("500x500")
root.configure(bg="lightgray")


WIDTH, HEIGHT = 500, 500
SCALE = 100
OFFSET_X = WIDTH // 2
OFFSET_Y = HEIGHT // 2
ANGLE_X = 0
ANGLE_Y = 0
CAMERA = 5

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

vertices = [
    [0, 0, 0], [1, 0, 0],[1, 1, 0], [0, 1, 0],
    [0, 0, 1], [1, 0, 1],[1, 1, 1], [0, 1, 1]
]

polygons = [
    ((0,1,2,3),"red"),   
    ((4,5,6,7),"blue"),  
    ((1,5,6,2),"yellow"),
    ((4,0,3,7),"green"),
    ((3,2,6,7),"orange"),
    ((0,1,5,4),"purple")
]

scene_objects = [
    {"vertices": vertices, "position": [0,0,0], "angle": [1,0,0], "color": "green"},
]

def rotate_x(v, angle):
    x, y, z = v
    
    C = math.cos(angle)
    s = math.sin(angle)
    
    y_new = y*C - z*s
    z_new = y*s + z*C
    
    return [x,y_new,z_new]
    
def rotate_y(v, angle):
    x, y, z = v
    
    C = math.cos(angle)
    s = math.sin(angle)
    
    x_new = x*C + z*s
    z_new = -x*s + z*C
    
    return [x_new,y,z_new]
    
def rotate_z(v, angle):
    x, y, z = v
    
    C = math.cos(angle)
    s = math.sin(angle)
    
    x_new = x*C - y*s
    y_new = x*s + y*C
    
    return [x_new,y_new,z]

def project(v, camera):
    x,y,z = v
    
    factor = camera / (camera + z)
    
    sx = x * factor * SCALE + OFFSET_X
    sy = y * factor * SCALE + OFFSET_Y
    
    return sx, sy

def key_pressed(event):
    global ANGLE_Y
    global ANGLE_X
    if event.keysym == "Right":
        ANGLE_Y -= 0.03
    elif event.keysym == "Left":
        ANGLE_Y += 0.03
    elif event.keysym == "Up":
        ANGLE_X -= 0.03
    elif event.keysym == "Down":
        ANGLE_X += 0.03
        
def draw():
    canvas.delete("all")
    sorted_polygons = []
    
    for obj in scene_objects:
        centered_vertices = []
        
        vector_width = 0.5
        vector_height = 0.5
        vector_depth = 0.5
        
        for x,y,z in obj['vertices']:
            centered_vertices.append([x-vector_width, y-vector_height, z-vector_depth])
            
        for p, color in polygons:
            points = []
            z_sum = 0
            
            for i in p:
                x = centered_vertices[i][0]
                y = centered_vertices[i][1]
                z = centered_vertices[i][2]
                
                rx, ry, rz = rotate_x([x,y,z], ANGLE_X) 
                rx, ry, rz = rotate_y([rx,ry,rz], ANGLE_Y) 
                z_sum += rz
                
                sx, sy = project([rx,ry,rz], CAMERA)
                points.extend([sx,sy])
                
            sorted_polygons.append((z_sum, color, points))
    
    sorted_polygons.sort(key=lambda f: f[0], reverse=True)
    
    for _, color, points in sorted_polygons:
        canvas.create_polygon(points, fill=color, outline="black")
    
    root.after(10, draw)

draw()
root.bind("<KeyPress>", key_pressed)
root.mainloop()