from manim import *
import numpy as np
from PIL import Image

cmap = ["#D0CCD0", "#FBFCFF", "#605856", "#1C6E8C", "#274156"]
sizes = [0.07+0.01*i for i in range(2, 8, 2)]
g_layouts = ["spring", "kamada_kawai"]

class GraphTool:
    def __init__(self, vertice_num: int, edge_num: int, random_seed: int = 7):
        self.random_seed = random_seed
        self.vertice_num = vertice_num
        self.edge_num = edge_num
        self.vertices = self.gen_vertices()
        self.edges = self.gen_edges()

    def gen_vertices(self):
        return [v+1 for v in range(self.vertice_num)]

    def gen_edges(self):

        np.random.seed(self.random_seed)
        edges = [(tuple(pair)) for pair in np.random.choice(self.vertices, size=(self.edge_num, 2), replace=True)]
        unique_edges = []

        for edge in edges:
            if edge not in unique_edges and (edge[1], edge[0]) not in unique_edges and edge[0] != edge[1]:
                unique_edges.append(edge)

        return unique_edges

class MyGraph(Scene):
    def construct(self):
        self.camera.background_color = "#f2f2f2"

        me = ImageMobject(Image.open("static/image/logo.png"))
        me.scale(0.4)

        my_graph = GraphTool(vertice_num=30, edge_num=30 * (30 - 20) // 2, random_seed=5)
        vertices = my_graph.vertices
        unique_edges = my_graph.edges

        layout = {v : [np.random.choice([e/2 for e in range(-6, 6)])+v/(my_graph.vertice_num), np.random.choice([e/3 for e in range(-6, 6)]), 1] for v in vertices}
        vertex_config = {v : {"fill_color": np.random.choice(cmap), "fill_opacity": 1, "radius": np.random.choice(sizes)} for v in vertices}
        edge_config = {e : {"stroke_color": "#777777"} for e in unique_edges}

        g = Graph(
            vertices, unique_edges,
            layout="kamada_kawai",
            vertex_config=vertex_config,
            edge_config=edge_config,
            )
        
        #self.play(me.animate.shift([0, -0.4, 1]))
        #self.play(me.animate.scale(1.15), run_time=0.4)
        
        me.z_index = 1
        g.z_index = 0

        #self.play(Create(g, fade=0.5))
        self.play(FadeIn(g))
        for g_layout in g_layouts:
            
            s = [0, np.random.choice([e/10 for e in range(10, 15)]), 0]
            
            
            self.play(g.animate.change_layout(g_layout))
            self.play(g.animate.rotate(np.random.choice([e/10 for e in range(-10, 10, 5)])))
            
        self.wait() 
