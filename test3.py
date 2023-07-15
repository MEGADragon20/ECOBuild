import pygame
import os

# Initialisierung von Pygame
pygame.init()

# Fenstergröße
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)

# Farben
GREEN = (181, 230, 29)
WHITE = (255, 255, 255)

# Bildpfad
HOUSE_IMAGE_PATH = "house.png"

# Fenster erstellen
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Drag and Drop")

# Hausbild laden
house_image = pygame.image.load(HOUSE_IMAGE_PATH)

class House:
    def __init__(self, x, y):
        self.rect = house_image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dragging = False

    def draw(self, surface):
        surface.blit(house_image, self.rect)

# Start-Haus erstellen
start_house = House(WIDTH // 2 - house_image.get_width() // 2, HEIGHT // 2 - house_image.get_height() // 2)

# Liste zum Speichern der zusätzlichen Häuser
additional_houses = []

# Button erstellen
button_font = pygame.font.Font(None, 36)
button_text = button_font.render("Weiteres Haus", True, WHITE)
button_rect = button_text.get_rect()
button_rect.center = (WIDTH // 2, HEIGHT - 50)

# Hauptschleife
running = True
while running:
    # Ereignisse überprüfen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Prüfen, ob das Mausereignis innerhalb des Start-Hauses stattfindet
            if start_house.rect.collidepoint(event.pos):
                start_house.dragging = True
            # Prüfen, ob das Mausereignis innerhalb eines zusätzlichen Hauses stattfindet
            for house in additional_houses:
                if house.rect.collidepoint(event.pos):
                    house.dragging = True
            # Prüfen, ob der Button geklickt wurde
            if button_rect.collidepoint(event.pos):
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                new_house = House(x, y)
                additional_houses.append(new_house)
        elif event.type == pygame.MOUSEBUTTONUP:
            # Beenden des Ziehens aller Häuser
            start_house.dragging = False
            for house in additional_houses:
                house.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            # Häuser verschieben, wenn sie gezogen werden
            if start_house.dragging:
                start_house.rect.x += event.rel[0]
                start_house.rect.y += event.rel[1]
            for house in additional_houses:
                if house.dragging:
                    house.rect.x += event.rel[0]
                    house.rect.y += event.rel[1]

    # Hintergrund löschen
    window.fill(GREEN)

    # Start-Haus zeichnen
    start_house.draw(window)

    # Zusätzliche Häuser zeichnen
    for house in additional_houses:
        house.draw(window)

    # Button zeichnen
    pygame.draw.rect(window, WHITE, button_rect)
    window.blit(button_text, button_rect)

    # Fenster aktualisieren
    pygame.display.update()

# Pygame beenden
pygame.quit()