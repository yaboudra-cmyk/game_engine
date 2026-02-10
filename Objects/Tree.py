vertices_trunk = [
    [0.15, -1, 0], [0.35, -1, 0],[0.35, 1, 0], [0.15, 1, 0],
    [0, -1, 0.15], [0, -1, 0.35],[0, 1, 0.35], [0, 1, 0.15],
    [0.15, -1, 0.5], [0.35, -1, 0.5],[0.35, 1, 0.5], [0.15, 1, 0.5],
    [0.5, -1, 0.15], [0.5, -1, 0.35],[0.5, 1, 0.35], [0.5, 1, 0.15],
]

vertices_leaves = [
    [0, 0, 0], [1, 0, 0],[1, 1, 0], [0, 1, 0],
    [0, 0, 1], [1, 0, 1],[1, 1, 1], [0, 1, 1]
]

polygons_trunk = [
    ((0,1,2,3),"brown"),   
    ((4,5,6,7),"brown"),     
    ((0,4,7,3),"brown"),
    ((5,8,11,6),"brown"),
    ((8,9,10,11),"brown"), 
    ((12,13,14,15),"brown"),  
    ((1,12,15,2),"brown"),  
    ((13,9,10,14),"brown"),  
]

polygons_leaves = [
    ((0,1,2,3),"green"),   
    ((4,5,6,7),"green"),  
    ((0,4,5,1),"green"),  
    ((0,4,7,3),"green"),  
    ((1,5,6,2),"green"), 
]

Tree = {
    "meshes": [
        {"vertices": vertices_trunk, "polygons": polygons_trunk, "position": [0,0,0], "angle": [1,0,0], "color": "green"},
        {"vertices": vertices_leaves, "polygons": polygons_leaves, "position": [-0.25,-1.5,-0.25], "angle": [1,0,0], "color": "green"}
    ]
}