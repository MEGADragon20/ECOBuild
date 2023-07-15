import pygame
import os
import random as r
import time

# Initialisierung von Pygame
pygame.init()

# Fenstergröße
WIDTH, HEIGHT = 1024, 768
WINDOW_SIZE = (WIDTH, HEIGHT)

# Farben
GREEN = (181, 230, 29)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
GREY = (100, 100, 100)

# Bildpfade
HOUSE_IMAGE_PATH = "house.png"
VILLA_IMAGE_PATH = "villa.png"
MANSION_IMAGE_PATH = "mansion.png"
INDUSTRIAL_UNIT_IMAGE_PATH = "Industrial_unit.png"
FACTORY_IMAGE_PATH = "Factory.png"
GARDEN_IMAGE_PATH = "garden.png"
PARK_IMAGE_PATH = "park.png"

#Geld
coins = 100

# Fenster erstellen
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("ECOBuild")

# Hausbilder laden
house_image = pygame.image.load(HOUSE_IMAGE_PATH)
villa_image = pygame.image.load(VILLA_IMAGE_PATH)
mansion_image = pygame.image.load(MANSION_IMAGE_PATH)

# Fabrikbilder laden
industrial_unit_image = pygame.image.load(INDUSTRIAL_UNIT_IMAGE_PATH)
Factory_image = pygame.image.load(FACTORY_IMAGE_PATH)

# Parkbilder laden
garden_image = pygame.image.load(GARDEN_IMAGE_PATH)
park_image = pygame.image.load(PARK_IMAGE_PATH)

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

class Mansion:
    def __init__(self, x, y):
        self.rect = mansion_image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dragging = False

    def draw(self, surface):
        surface.blit(mansion_image, self.rect)

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

class Garden:
    def __init__(self, x, y):
        self.rect = garden_image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dragging = False

    def draw(self, surface):
        surface.blit(garden_image, self.rect)

class Park:
    def __init__(self, x, y):
        self.rect = park_image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dragging = False

    def draw(self, surface):
        surface.blit(park_image, self.rect)

# Start-Häuser erstellen
start_house1 = House(WIDTH // 2 - house_image.get_width() - 30, HEIGHT // 2 - house_image.get_height() + 20)
start_house2 = House(WIDTH // 2, HEIGHT // 2 - house_image.get_height())

# Liste zum Speichern der zusätzlichen Häuser und Villen
houses = [start_house1, start_house2]
villas = []
mansions = []
industrial_units = []
factories = []
gardens = []
parks = []

# Button_Haus erstellen
button_house_font = pygame.font.Font(None, 36)
button_house_text = button_house_font.render("Haus", True, WHITE)
button_house_rect = button_house_text.get_rect()
button_house_rect.center = (WIDTH // 2 -100, HEIGHT - 50)

# Button_Fabrik erstellen
button_factory_font = pygame.font.Font(None, 36)
button_factory_text = button_factory_font.render("Fabrik", True, WHITE)
button_factory_rect = button_factory_text.get_rect()
button_factory_rect.center = (WIDTH // 2 +100, HEIGHT - 50)

# Button_Park erstellen
button_park_font = pygame.font.Font(None, 36)
button_park_text = button_park_font.render("Park", True, WHITE)
button_park_rect = button_park_text.get_rect()
button_park_rect.center = (WIDTH // 2, HEIGHT - 50)

# Leeren Platz finden 
def locate_place():
    a = r.randint(64, 960)
    b = r.randint(64, 702)
    for house in houses:
        if a == house.rect.x and b == house.rect.y or a == house.rect.x +64 and b == house.rect.y +64:
            return locate_place()
    return a, b

# Funktion, um Text auf dem Bildschirm anzuzeigen
def draw_text(text, font, color, x, y, surface):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

# Anzahl Geld pro minute
def earn(houses, villas, mansions, factories, industrial_units):
    return len(houses) * 50 + len(villas) * 75 + len(mansions) * 100 + len(factories) * 100 + len(industrial_units) * 150

# Zeit konfiguration
pygame.time.set_timer(618, 60000)

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
            # Prüfen, ob das Mausereignis innerhalb einer Mansion stattfindet
            for mansion in mansions:
                if mansion.rect.collidepoint(event.pos):
                    mansion.dragging = True
                    break
            # Prüfen, ob das Mausereignis innerhalb eines zusätzlichen IU stattfindet
            for industrial_unit in industrial_units:
                if industrial_unit.rect.collidepoint(event.pos):
                    industrial_unit.dragging = True
                    break
            # Prüfen, ob das Mausereignis innerhalb einer Fabrik stattfindet
            for factory in factories:
                if factory.rect.collidepoint(event.pos):
                    factory.dragging = True
                    break
            # Prüfen, ob das Mausereignis innerhalb eines zusätzlichen Gartens stattfindet
            for garden in gardens:
                if garden.rect.collidepoint(event.pos):
                    garden.dragging = True
                    break
            # Prüfen, ob das Mausereignis innerhalb einer park stattfindet
            for park in parks:
                if park.rect.collidepoint(event.pos):
                    park.dragging = True
                    break
            # Prüfen, ob der Haus kaufen Button geklickt wurde
            if button_house_rect.collidepoint(event.pos):
                if coins >= 100:
                    coins -= 100
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    x2, y2 = locate_place()
                    new_house = House(x2,y2)
                    houses.append(new_house)
            # Prüfen, ob der Fabrik kaufen Button geklickt wurde
            if button_factory_rect.collidepoint(event.pos):
                if coins >= 200:
                    coins -=200
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    x2, y2 = locate_place()
                    new_industrial_unit = Industrial_unit(x2,y2)
                    industrial_units.append(new_industrial_unit)
            # Prüfen, ob der Park kaufen Button geklickt wurde
            if button_park_rect.collidepoint(event.pos):
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                x2, y2 = locate_place()
                new_garden = Garden(x2,y2)
                gardens.append(new_garden)

        elif event.type == pygame.MOUSEBUTTONUP:
            # Beenden des Ziehens aller Gebäude
            for house in houses:
                house.dragging = False
            for villa in villas:
                villa.dragging = False
            for mansion in mansions:
                mansion.dragging = False
            for industrial_unit in industrial_units:
                industrial_unit.dragging = False
            for factory in factories:
                factory.dragging = False
            for garden in gardens:
                garden.dragging = False
            for park in parks:
                park.dragging = False

            # Überprüfen auf Zusammenführung der Häuser
            for house in houses:
                for tester in houses:
                    if tester != house:
                        if house.rect.colliderect(tester):
                            new_villa = Villa(tester.rect.x, tester.rect.y)
                            villas.append(new_villa)
                            houses.remove(house)
                            houses.remove(tester)
            # Überprüfen auf Zusammenführung der Fabriken
            for industrial_unit in industrial_units:
                for tester in industrial_units:
                    if tester != industrial_unit:
                        if industrial_unit.rect.colliderect(tester):
                            new_Factory = Factory(tester.rect.x, tester.rect.y)
                            factories.append(new_Factory)
                            industrial_units.remove(industrial_unit)
                            industrial_units.remove(tester)
            # Überprüfen auf Zusammenführung der Parks
            for garden in gardens:
                for tester in gardens:
                    if tester != garden:
                        if garden.rect.colliderect(tester):
                            new_park = Park(tester.rect.x, tester.rect.y)
                            parks.append(new_park)
                            gardens.remove(garden)
                            gardens.remove(tester)
            # Überprüfen auf Zusammenführung der Villen
            for villa in villas:
                for tester in villas:
                    if tester != villa:
                        if villa.rect.colliderect(tester):
                            new_mansion = Mansion(tester.rect.x, tester.rect.y)
                            mansions.append(new_mansion)
                            villas.remove(villa)
                            villas.remove(tester)

        elif event.type == pygame.MOUSEMOTION:
            # Gebäude verschieben, wenn sie gezogen werden
            for house in houses:
                if house.dragging:
                    house.rect.x += event.rel[0]
                    house.rect.y += event.rel[1]
            for villa in villas:
                if villa.dragging:
                    villa.rect.x += event.rel[0]
                    villa.rect.y += event.rel[1]
            for mansion in mansions:
                if mansion.dragging:
                    mansion.rect.x += event.rel[0]
                    mansion.rect.y += event.rel[1]
            for industrial_unit in industrial_units:
                if industrial_unit.dragging:
                    industrial_unit.rect.x += event.rel[0]
                    industrial_unit.rect.y += event.rel[1]
            for factory in factories:
                if factory.dragging:
                    factory.rect.x += event.rel[0]
                    factory.rect.y += event.rel[1]
            for garden in gardens:
                if garden.dragging:
                    garden.rect.x += event.rel[0]
                    garden.rect.y += event.rel[1]
            for park in parks:
                if park.dragging:
                    park.rect.x += event.rel[0]
                    park.rect.y += event.rel[1]

        elif event.type == 618:
            coins += earn(houses, villas, mansions, factories, industrial_units)

    # Hintergrund färben
    window.fill(GREEN)

    # Garten zeichnen
    for garden in gardens:
        garden.draw(window)
    
    # Park zeichnen
    for park in parks:
        park.draw(window)

    # Fabriken zeichnen
    for factory in factories:
        factory.draw(window)   

    # Mansion zeichnen
    for mansion in mansions:
        mansion.draw(window)
    
    # Villen zeichnen
    for villa in villas:
        villa.draw(window)

    # Zusätzliche IU zeichnen
    for industrial_unit in industrial_units:
        industrial_unit.draw(window)

    # Zusätzliche Häuser zeichnen
    for house in houses:
        house.draw(window)
    # Haus Button zeichnen
    if coins >= 100:
        pygame.draw.rect(window, BLACK, button_house_rect)
    else:
        pygame.draw.rect(window, GREY, button_house_rect)
    window.blit(button_house_text, button_house_rect)

    # Fabrik Button zeichnen
    if coins >= 200:
        pygame.draw.rect(window, BLACK, button_factory_rect)
    else:
        pygame.draw.rect(window, GREY, button_factory_rect)
    window.blit(button_factory_text, button_factory_rect)

    # Park Button zeichnen
    pygame.draw.rect(window, BLACK, button_park_rect)
    window.blit(button_park_text, button_park_rect)

    # Geldanzahl
    draw_text("Münzen: {}".format(coins),pygame.font.Font(None, 36) ,BLACK, 15, 20, window)
    
    # Fenster aktualisieren
    pygame.display.update()

# Pygame beenden
pygame.quit()