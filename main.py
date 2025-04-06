# src/main.py

import pygame
from pygame.locals import *
from OpenGL.GL import *

from clipping import cyrus_beck_3d
from rendering import draw_prism, draw_line, setup_opengl

# Define the prism boundaries (5x4x3)
prism_dimensions = ((0, 5), (0, 4), (0, 3))

# Sample line to clip (from outside to inside the prism)
line = [(2, 2, -2), (2, 2, 5)]  # Line from (2,2,-2) to (2,2,5)

# Clip the line using Cyrus-Beck
clipped_line = cyrus_beck_3d(line, prism_dimensions)
print("Cyrus-Beck Clipped Line:", clipped_line)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Set up OpenGL
    setup_opengl(display)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the prism
        draw_prism()

        # Draw the original line (red)
        draw_line(line, color=(1, 0, 0))

        # Draw the clipped line (blue)
        if clipped_line:
            draw_line(clipped_line, color=(0, 0, 1))

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()