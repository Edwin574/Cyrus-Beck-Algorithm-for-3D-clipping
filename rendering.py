# src/rendering.py

from OpenGL.GL import *
from OpenGL.GLU import *

# Define the vertices of the prism (5x4x3)
vertices = [
    (0, 0, 0), (5, 0, 0), (5, 4, 0), (0, 4, 0),  # Bottom face
    (0, 0, 3), (5, 0, 3), (5, 4, 3), (0, 4, 3)     # Top face
]

# Define the edges of the prism
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Bottom face
    (4, 5), (5, 6), (6, 7), (7, 4),  # Top face
    (0, 4), (1, 5), (2, 6), (3, 7)   # Connecting edges
]

def draw_prism():
    """Draws the 3D prism as a wireframe."""
    glBegin(GL_LINES)
    glColor3f(0, 1, 1)  # Cyan color for the prism
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_line(line, color=(1, 0, 0)):
    """Draws a line with the specified color."""
    glColor3f(*color)
    glBegin(GL_LINES)
    glVertex3fv(line[0])
    glVertex3fv(line[1])
    glEnd()

def setup_opengl(display):
    """Sets up the OpenGL environment."""
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(-2.5, -2, -15)  # Move the camera back to view the prism
    glEnable(GL_DEPTH_TEST)