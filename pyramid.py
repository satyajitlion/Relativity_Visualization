import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (0, 0, 1),
    (-1, 0, 0),
    (0, -1, 0),
    (1, 0, 0),
    (0, 1, 0),
)

edges = (
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 1),

)

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6),
)

colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
)

def Pyramid():
    glBegin(GL_LINES) #puts together a pyramid.
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)#originally the pers was 45
    glTranslatef(0, 0, -5) ## allows you to zoom out to see the cube
    glRotatef(0, 0, 0, 0) #degrees x, y, and z

    while True:
        for event in pygame.event.get(): #allows to close pygame window easily
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #constants -> we wanna clear this stuff specifically or else face extreme lag
        #glTranslatef(0, 0, 0.1)
        glColor3f(1.0, 0.0, 2.0) #line color = pink
        Pyramid()
        pygame.display.flip()
        pygame.time.wait(10)
main()
