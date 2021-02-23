import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices_cube = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
)

edges_cube = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),
)

vertices_pyr = (
    (0, 0, 1),
    (-1, 0, 0),
    (0, -1, 0),
    (1, 0, 0),
    (0, 1, 0),
)

edges_pyr = (
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 1),

)

surfaces_cube = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6),
)

colors_cube = (
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

def Cube():
    glBegin(GL_QUADS) #colors cube
    for surface_cube in surfaces_cube:
        x = 0
        for vertex_cube in surface_cube:
            x += 1
            glColor3fv(colors_cube[x])
            glVertex3fv(vertices_cube[vertex_cube])

    glEnd()

    glBegin(GL_LINES) #puts together a cube.
    for edge_cube in edges_cube:
        for vertex_cube in edge_cube:
            glVertex3fv(vertices_cube[vertex_cube])
    glEnd()
def Pyramid():
    glBegin(GL_LINES) #puts together a pyramid# .
    for edge_pyr in edges_pyr:
        for vertex_pyr in edge_pyr:
            glVertex3fv(vertices_pyr[vertex_pyr])
    glEnd()
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)#originally the pers was 45
    glTranslatef(0, 0, -40) ## allows you to zoom out to see the cube
    glRotatef(0, 0, 0, 0) #degrees x, y, and z

    while True:
        for event in pygame.event.get(): #allows to close pygame window easily
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #below: how to control space
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: #controlling character right now
                    glTranslatef(1, 0, 0) # flip the signs if you want to control the cube or control "character"
                if event.key == pygame.K_RIGHT:
                    glTranslatef(-1, 0, 0)
                if event.key == pygame.K_UP:
                    glTranslatef(0, -1, 0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, 1, 0)
                if event.key == pygame.K_SPACE:
                        glTranslatef(0, 0, -30)

        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #constants -> we wanna clear this stuff specifically or else face extreme lag
        glTranslatef(0, 0, 0.1)
        glColor3f(1.0, 0.0, 2.0) #line color = pink
        Cube()
        # Pyramid()
        pygame.display.flip()
        pygame.time.wait(10)
main()
