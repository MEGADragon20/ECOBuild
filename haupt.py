######Gunnar#####

import pygame
import os
import random as r

# Initialisierung von Pygame
pygame.init()

# Fenstergröße
WIDTH, HEIGHT = 1024, 768
WINDOW_SIZE = (WIDTH, HEIGHT)

# Farben
GREEN = (181, 230, 29)
WHITE = (255, 255, 255)
BLACK = (0,0,0)

# Bildpfade IU - G, F - P
GARDEN_IMAGE_PATH = "garden.png"
PARK_IMAGE_PATH = "park.png"

# Fenster erstellen
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Drag and Drop")

# Hausbilder laden
garden_image = pygame.image.load(GARDEN_IMAGE_PATH)
park_image = pygame.image.load(PARK_IMAGE_PATH)

class garden:
    def __init__(self, x, y):
        self.rect = garden_image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dragging = False

    def draw(self, surface):
        surface.blit(garden_image, self.rect)

class park:
    def __init__(self, x, y):
        self.rect = park_image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dragging = False

    def draw(self, surface):
        surface.blit(park_image, self.rect)


# Liste zum Speichern der zusätzlichen Häuser und Villen
gardens = []
parks = []

# Button erstellen
button_font = pygame.font.Font(None, 36)
button_text = button_font.render("Weiteres Haus", True, WHITE)
button_rect = button_text.get_rect()
button_rect.center = (WIDTH // 2, HEIGHT - 50)

def locate_place():
    a = r.randint(64, 960)
    b = r.randint(64, 702)
    for industrial_unit in gardens:
        if a == industrial_unit.rect.x and b == industrial_unit.rect.y or a == industrial_unit.rect.x +64 and b == industrial_unit.rect.y +64:
            return locate_place()
    return a, b

# Hauptschleife
running = True
while running:
    # Ereignisse überprüfen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Prüfen, ob das Mausereignis innerhalb eines zusätzlichen Hauses stattfindet
            for industrial_unit in gardens:
                if industrial_unit.rect.collidepoint(event.pos):
                    industrial_unit.dragging = True
                    break
            # Prüfen, ob das Mausereignis innerhalb einer park stattfindet
            for factory in parks:
                if factory.rect.collidepoint(event.pos):
                    factory.dragging = True
                    break
            # Prüfen, ob der Button geklickt wurde
            if button_rect.collidepoint(event.pos):
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                x2, y2 = locate_place()
                new_industrial_unit = garden(x2,y2)
                gardens.append(new_industrial_unit)
        elif event.type == pygame.MOUSEBUTTONUP:
            # Beenden des Ziehens aller Häuser und Villen
            for industrial_unit in gardens:
                industrial_unit.dragging = False
            for factory in parks:
                factory.dragging = False

            # Überprüfen auf Zusammenführung der Häuser
            for industrial_unit in gardens:
                for tester in gardens:
                    if tester != industrial_unit:
                        if industrial_unit.rect.colliderect(tester):
                            new_Factory = park(tester.rect.x, tester.rect.y)
                            parks.append(new_Factory)
                            gardens.remove(industrial_unit)
                            gardens.remove(tester)

        elif event.type == pygame.MOUSEMOTION:
            # Häuser und Villen verschieben, wenn sie gezogen werden
            for industrial_unit in gardens:
                if industrial_unit.dragging:
                    industrial_unit.rect.x += event.rel[0]
                    industrial_unit.rect.y += event.rel[1]
            for factory in parks:
                if factory.dragging:
                    factory.rect.x += event.rel[0]
                    factory.rect.y += event.rel[1]

    # Hintergrund färben
    window.fill(GREEN)

    # Zusätzliche Häuser zeichnen
    for industrial_unit in gardens:
        industrial_unit.draw(window)

    # Villen zeichnen
    for factory in parks:
        factory.draw(window)

    # Button zeichnen
    pygame.draw.rect(window, BLACK, button_rect)
    window.blit(button_text, button_rect)

    # Fenster aktualisieren
    pygame.display.update()

# Pygame beenden
pygame.quit()