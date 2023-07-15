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

# Bildpfade
INDUSTRIAL_UNIT_IMAGE_PATH = "Industrial_unit.png"
FACTORY_IMAGE_PATH = "Factory.png"

# Fenster erstellen
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Drag and Drop")

# Hausbilder laden
industrial_unit_image = pygame.image.load(INDUSTRIAL_UNIT_IMAGE_PATH)
Factory_image = pygame.image.load(FACTORY_IMAGE_PATH)

class Industrial_unit:
    def __init__(self, x, y):
        self.rect = industrial_unit_image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dragging = False

    def draw(self, surface):
        surface.blit(industrial_unit_image, self.rect)

class Factory:
    def __init__(self, x, y):
        self.rect = Factory_image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dragging = False

    def draw(self, surface):
        surface.blit(Factory_image, self.rect)


# Liste zum Speichern der zusätzlichen Häuser und Villen
industrial_units = []
factories = []

# Button erstellen
button_font = pygame.font.Font(None, 36)
button_text = button_font.render("Fabrik", True, WHITE)
button_rect = button_text.get_rect()
button_rect.center = (WIDTH // 2, HEIGHT - 50)

def locate_place():
    a = r.randint(64, 960)
    b = r.randint(64, 702)
    for industrial_unit in industrial_units:
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
            for industrial_unit in industrial_units:
                if industrial_unit.rect.collidepoint(event.pos):
                    industrial_unit.dragging = True
                    break
            # Prüfen, ob das Mausereignis innerhalb einer Factory stattfindet
            for factory in factories:
                if factory.rect.collidepoint(event.pos):
                    factory.dragging = True
                    break
            # Prüfen, ob der Button geklickt wurde
            if button_rect.collidepoint(event.pos):
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                x2, y2 = locate_place()
                new_industrial_unit = Industrial_unit(x2,y2)
                industrial_units.append(new_industrial_unit)
        elif event.type == pygame.MOUSEBUTTONUP:
            # Beenden des Ziehens aller Häuser und Villen
            for industrial_unit in industrial_units:
                industrial_unit.dragging = False
            for factory in factories:
                factory.dragging = False

            # Überprüfen auf Zusammenführung der Häuser
            for industrial_unit in industrial_units:
                for tester in industrial_units:
                    if tester != industrial_unit:
                        if industrial_unit.rect.colliderect(tester):
                            new_Factory = Factory(tester.rect.x, tester.rect.y)
                            factories.append(new_Factory)
                            industrial_units.remove(industrial_unit)
                            industrial_units.remove(tester)

        elif event.type == pygame.MOUSEMOTION:
            # Häuser und Villen verschieben, wenn sie gezogen werden
            for industrial_unit in industrial_units:
                if industrial_unit.dragging:
                    industrial_unit.rect.x += event.rel[0]
                    industrial_unit.rect.y += event.rel[1]
            for factory in factories:
                if factory.dragging:
                    factory.rect.x += event.rel[0]
                    factory.rect.y += event.rel[1]

    # Hintergrund färben
    window.fill(GREEN)

    # Zusätzliche Häuser zeichnen
    for industrial_unit in industrial_units:
        industrial_unit.draw(window)

    # Villen zeichnen
    for factory in factories:
        factory.draw(window)

    # Button zeichnen
    pygame.draw.rect(window, BLACK, button_rect)
    window.blit(button_text, button_rect)

    # Fenster aktualisieren
    pygame.display.update()

# Pygame beenden
pygame.quit()