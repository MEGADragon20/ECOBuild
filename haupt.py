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
HOUSE_IMAGE_PATH = "house.png"
VILLA_IMAGE_PATH = "villa.png"

# Fenster erstellen
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Drag and Drop")

# Hausbilder laden
house_image = pygame.image.load(HOUSE_IMAGE_PATH)
villa_image = pygame.image.load(VILLA_IMAGE_PATH)

class House:
    def __init__(self, x, y):
        self.rect = house_image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dragging = False

    def draw(self, surface):
        surface.blit(house_image, self.rect)

class Villa:
    def __init__(self, x, y):
        self.rect = villa_image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dragging = False

    def draw(self, surface):
        surface.blit(villa_image, self.rect)

# Start-Häuser erstellen
start_house1 = House(WIDTH // 2 - house_image.get_width() - 30, HEIGHT // 2 - house_image.get_height() + 20)
start_house2 = House(WIDTH // 2, HEIGHT // 2 - house_image.get_height())

# Liste zum Speichern der zusätzlichen Häuser und Villen
houses = [start_house1, start_house2]
villas = []

# Button erstellen
button_font = pygame.font.Font(None, 36)
button_text = button_font.render("Weiteres Haus", True, WHITE)
button_rect = button_text.get_rect()
button_rect.center = (WIDTH // 2, HEIGHT - 50)

def locate_place():
    a = r.randint(64, 960)
    b = r.randint(64, 702)
    for house in houses:
        if a == house.rect.x and b == house.rect.y or a == house.rect.x +64 and b == house.rect.y +64:
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
            for house in houses:
                if house.rect.collidepoint(event.pos):
                    house.dragging = True
                    break
            # Prüfen, ob das Mausereignis innerhalb einer Villa stattfindet
            for villa in villas:
                if villa.rect.collidepoint(event.pos):
                    villa.dragging = True
                    break
            # Prüfen, ob der Button geklickt wurde
            if button_rect.collidepoint(event.pos):
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                x2, y2 = locate_place()
                new_house = House(x2,y2)
                houses.append(new_house)
        elif event.type == pygame.MOUSEBUTTONUP:
            # Beenden des Ziehens aller Häuser und Villen
            for house in houses:
                house.dragging = False
            for villa in villas:
                villa.dragging = False

            # Überprüfen auf Zusammenführung der Häuser
            for house in houses:
                for tester in houses:
                    if tester != house:
                        if house.rect.colliderect(tester):
                            new_villa = Villa(tester.rect.x, tester.rect.y)
                            villas.append(new_villa)
                            houses.remove(house)
                            houses.remove(tester)

        elif event.type == pygame.MOUSEMOTION:
            # Häuser und Villen verschieben, wenn sie gezogen werden
            for house in houses:
                if house.dragging:
                    house.rect.x += event.rel[0]
                    house.rect.y += event.rel[1]
            for villa in villas:
                if villa.dragging:
                    villa.rect.x += event.rel[0]
                    villa.rect.y += event.rel[1]

    # Hintergrund färben
    window.fill(GREEN)

    # Zusätzliche Häuser zeichnen
    for house in houses:
        house.draw(window)

    # Villen zeichnen
    for villa in villas:
        villa.draw(window)

    # Button zeichnen
    pygame.draw.rect(window, BLACK, button_rect)
    window.blit(button_text, button_rect)

    # Fenster aktualisieren
    pygame.display.update()

# Pygame beenden
pygame.quit()