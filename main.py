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
HOUSE_IMAGE_PATH = "pictures/house.png"
VILLA_IMAGE_PATH = "pictures/villa.png"
MANSION_IMAGE_PATH = "pictures/mansion.png"
MANOR_IMAGE_PATH = "pictures/manor.png"
INDUSTRIAL_UNIT_IMAGE_PATH = "pictures/industrial_unit.png"
FACTORY_IMAGE_PATH = "pictures/factory.png"
INDUSTRIAL_PLANT_IMAGE_PATH = "pictures/industrial_plant.png"
GARDEN_IMAGE_PATH = "pictures/garden.png"
PARK_IMAGE_PATH = "pictures/park.png"
FOREST_IMAGE_PATH = "pictures/forest.png"

# Start Variablen
coins = 80

habs = 0

# Fenster erstellen
bg = pygame.image.load("background.png")
window = pygame.display.set_mode(WINDOW_SIZE)
is_fullscreen = False
pygame.display.set_caption("ECOBuild")

# Hausbilder laden
house_image = pygame.image.load(HOUSE_IMAGE_PATH)
villa_image = pygame.image.load(VILLA_IMAGE_PATH)
mansion_image = pygame.image.load(MANSION_IMAGE_PATH)
manor_image = pygame.image.load(MANOR_IMAGE_PATH)

# Fabrikbilder laden
industrial_unit_image = pygame.image.load(INDUSTRIAL_UNIT_IMAGE_PATH)
Factory_image = pygame.image.load(FACTORY_IMAGE_PATH)
industrial_plant_image = pygame.image.load(INDUSTRIAL_PLANT_IMAGE_PATH)

# Parkbilder laden
garden_image = pygame.image.load(GARDEN_IMAGE_PATH)
park_image = pygame.image.load(PARK_IMAGE_PATH)
forest_image = pygame.image.load(FOREST_IMAGE_PATH)

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

class Manor:
    def __init__(self, x, y):
        self.rect = manor_image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dragging = False

    def draw(self, surface):
        surface.blit(manor_image, self.rect)

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
    
class Industrial_Plant:
    def __init__(self, x, y):
        self.rect = industrial_plant_image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dragging = False

    def draw(self, surface):
        surface.blit(industrial_plant_image, self.rect)


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

class Forest:
    def __init__(self, x, y):
        self.rect = forest_image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dragging = False

    def draw(self, surface):
        surface.blit(forest_image, self.rect)

# Start-Häuser erstellen
start_house1 = House(WIDTH // 2 - house_image.get_width() - 30, HEIGHT // 2 - house_image.get_height() + 20)
start_house2 = House(WIDTH // 2, HEIGHT // 2 - house_image.get_height())

# Liste zum Speichern der zusätzlichen Häuser und Villen
houses = [start_house1, start_house2]
villas = []
mansions = []
manors = []
industrial_units = []
factories = []
industrial_plants = []
gardens = []
parks = []
forests = []

# Error text
messageboxtext = None

# Button_Haus erstellen
button_house_font = pygame.font.SysFont('impact', 32)
button_house_text = button_house_font.render("  Haus", True, WHITE)
button_house_rect = pygame.Rect(120, 100, 87, 45)
button_house_rect.center = (WIDTH // 2 -100, HEIGHT - 50)

# Button_Fabrik erstellen
button_factory_font = pygame.font.SysFont('impact', 32)
button_factory_text = button_factory_font.render(" Fabrik", True, WHITE)
button_factory_rect = pygame.Rect(120, 100, 95, 45)
button_factory_rect.center = (WIDTH // 2 +100, HEIGHT - 50)

# Button_Park erstellen
button_park_font = pygame.font.SysFont('impact', 32)
button_park_text = button_park_font.render("   Park", True, WHITE)
button_park_rect = pygame.Rect(120, 100, 95, 45)
button_park_rect.center = (WIDTH // 2, HEIGHT - 50)

# Leeren Platz finden 
def locate_place():
    a = r.randint(80, 944)
    b = r.randint(80, 630)
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

def message_box(txt, font, space, surface):
    text_surface = font.render(txt, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (space, 16)
    surface.blit(text_surface, text_rect)

# Anzahl Geld pro minute
def earn(houses, villas, mansions, manors, industrial_units, factories):
    return len(houses) * 20 + len(villas) * 60 + len(mansions) * 150 + len(manors) * 350 + len(industrial_units) * 100 + len(factories) * 220 + len(industrial_plants) * 500

def count_habs(houses, villas, mansions, manors):
    return len(houses) * 2 + len(villas) * 3 + len(mansions) * 4 + len(manors) * 5

# Zeit konfiguration
pygame.time.set_timer(618, 60000)

# Hauptschleife
running = True
while running:
    habs = count_habs(houses, villas, mansions, manors)
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
            # Prüfen, ob das Mausereignis innerhalb einer Herrenhaus stattfindet
            for manor in manors:
                if manor.rect.collidepoint(event.pos):
                    manor.dragging = True
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
            # Prüfen, ob das Mausereignis innerhalb einer IP stattfindet
            for industrial_plant in industrial_plants:
                if industrial_plant.rect.collidepoint(event.pos):
                    industrial_plant.dragging = True
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
            for forest in forests:
                if forest.rect.collidepoint(event.pos):
                    forest.dragging = True
                    break
            # Prüfen, ob der Haus kaufen Button geklickt wurde
            if button_house_rect.collidepoint(event.pos):
                if coins >= 80:
                    coins -= 80
                    x2, y2 = locate_place()
                    new_house = House(x2,y2)
                    houses.append(new_house)
                else:
                    messageboxtext = "Du brauchst 80 Münzen, um ein Haus zu kaufen"
            # Prüfen, ob der Fabrik kaufen Button geklickt wurde
            if button_factory_rect.collidepoint(event.pos):
                if coins >= 200 and len(gardens) + len(parks) * 2 + len(forests) * 4>= len(industrial_units) + len(factories) and habs > len(industrial_units) * 1 + len(factories) * 2 + len(industrial_plants) * 4:
                    coins -=200
                    x2, y2 = locate_place()
                    new_industrial_unit = Industrial_unit(x2,y2)
                    industrial_units.append(new_industrial_unit)
                else:
                    messageboxtext = "Du brauchst 200 Münzen, Parks und genug Einwohner, um eine Fabrik zu kaufen"
                
            # Prüfen, ob der Park kaufen Button geklickt wurde
            if button_park_rect.collidepoint(event.pos):
                if coins >= 150:
                    coins -= 150
                    x2, y2 = locate_place()
                    new_garden = Garden(x2,y2)
                    gardens.append(new_garden)
                else:
                    messageboxtext = "Du brauchst 150 Münzen, um ein Park zu kaufen"

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                # Überprüfe den aktuellen Fenstermod us
                if is_fullscreen:
                    # Wenn Vollbildmodus aktiv ist, wechsle zu Fenstermodus
                    pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
                    is_fullscreen = False
                else:
                    # Wenn Fenstermodus aktiv ist, wechsle zu Vollbildmodus
                    pygame.display.set_mode(WINDOW_SIZE, pygame.FULLSCREEN)
                    is_fullscreen = True

        elif event.type == pygame.MOUSEBUTTONUP:
            # Beenden des Ziehens aller Gebäude
            for house in houses:
                house.dragging = False
            for villa in villas:
                villa.dragging = False
            for mansion in mansions:
                mansion.dragging = False
            for manor in manors:
                manor.dragging = False
            for industrial_unit in industrial_units:
                industrial_unit.dragging = False
            for factory in factories:
                factory.dragging = False
            for industrial_plant in industrial_plants:
                industrial_plant.dragging = False
            for garden in gardens:
                garden.dragging = False
            for park in parks:
                park.dragging = False
            for forest in forests:
                forest.dragging = False

            # Überprüfen auf Zusammenführung der Häuser (LVL 1 -> LVL 2)
            for house in houses:
                for tester in houses:
                    if tester != house:
                        if house.rect.colliderect(tester):
                            new_villa = Villa(tester.rect.x, tester.rect.y)
                            villas.append(new_villa)
                            if house in houses:
                                houses.remove(house)
                            if tester in houses:
                                houses.remove(tester)
            # Überprüfen auf Zusammenführung der IU (LVL 1 -> LVL 2)
            for industrial_unit in industrial_units:
                for tester in industrial_units:
                    if tester != industrial_unit:
                        if industrial_unit.rect.colliderect(tester):
                            new_factory = Factory(tester.rect.x, tester.rect.y)
                            factories.append(new_factory)
                            if industrial_unit in industrial_units:
                                industrial_units.remove(industrial_unit)
                            if tester in industrial_units:
                                industrial_units.remove(tester)
            # Überprüfen auf Zusammenführung der Gärten (LVL 1 -> LVL 2)
            for garden in gardens:
                for tester in gardens:
                    if tester != garden:
                        if garden.rect.colliderect(tester):
                            new_park = Park(tester.rect.x, tester.rect.y)
                            parks.append(new_park)
                            if garden in gardens:
                                gardens.remove(garden)
                            if tester in gardens:
                                gardens.remove(tester)
            # Überprüfen auf Zusammenführung der Villen (LVL 2 -> LVL 3)
            for villa in villas:
                for tester in villas:
                    if tester != villa:
                        if villa.rect.colliderect(tester):
                            new_mansion = Mansion(tester.rect.x, tester.rect.y)
                            mansions.append(new_mansion)
                            if villa in villas:
                                villas.remove(villa)
                            if tester in villas:
                                villas.remove(tester)
            # Überprüfen auf Zusammenführung der Fabriken (LVL 2 -> LVL 3)
            for factory in factories:
                for tester in factories:
                    if tester != factory:
                        if factory.rect.colliderect(tester):
                            new_industrial_plant = Industrial_Plant(tester.rect.x, tester.rect.y)
                            industrial_plants.append(new_industrial_plant)
                            if factory in factories:
                                factories.remove(factory)
                            if tester in factories:
                                factories.remove(tester)
            # Überprüfen auf Zusammenführung der Parks (LVL 2 -> LVL 3)
            for park in parks:
                for tester in parks:
                    if tester != park:
                        if park.rect.colliderect(tester):
                            new_forest = Forest(tester.rect.x, tester.rect.y)
                            forests.append(new_forest)
                            if park in parks:
                                parks.remove(park)
                            if tester in parks:
                                parks.remove(tester)
            # Überprüfen auf Zusammenführung der Mansionen (LVL 3 -> LVL 4)
            for mansion in mansions:
                for tester in mansions:
                    if tester != mansion:
                        if mansion.rect.colliderect(tester):
                            new_manor = Manor(tester.rect.x, tester.rect.y)
                            manors.append(new_manor)
                            if mansion in mansions:
                                mansions.remove(mansion)
                            if tester in mansions:
                                mansions.remove(tester)

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
            for manor in manors:
                if manor.dragging:
                    manor.rect.x += event.rel[0]
                    manor.rect.y += event.rel[1]
            for industrial_unit in industrial_units:
                if industrial_unit.dragging:
                    industrial_unit.rect.x += event.rel[0]
                    industrial_unit.rect.y += event.rel[1]
            for factory in factories:
                if factory.dragging:
                    factory.rect.x += event.rel[0]
                    factory.rect.y += event.rel[1]
            for industrial_plant in industrial_plants:
                if industrial_plant.dragging:
                    industrial_plant.rect.x += event.rel[0]
                    industrial_plant.rect.y += event.rel[1]
            for garden in gardens:
                if garden.dragging:
                    garden.rect.x += event.rel[0]
                    garden.rect.y += event.rel[1]
            for park in parks:
                if park.dragging:
                    park.rect.x += event.rel[0]
                    park.rect.y += event.rel[1]
            for forest in forests:
                if forest.dragging:
                    forest.rect.x += event.rel[0]
                    forest.rect.y += event.rel[1]     

        elif event.type == 618:
            coins += earn(houses, villas, mansions, manors, industrial_units, factories)
            messageboxtext = None
        
    window.blit(bg, (0,0))

    # IP zeichnen
    for industrial_plant in industrial_plants:
        industrial_plant.draw(window)

    # Fabriken zeichnen
    for factory in factories:
        factory.draw(window)  

    # Zusätzliche IU zeichnen
    for industrial_unit in industrial_units:
        industrial_unit.draw(window)

    # Herrenhäuser zeichnen
    for manor in manors:
        manor.draw(window)

    # Mansion zeichnen
    for mansion in mansions:
        mansion.draw(window)
    
    # Villen zeichnen
    for villa in villas:
        villa.draw(window)

    # Zusätzliche Häuser zeichnen
    for house in houses:
        house.draw(window)
    
    # Wald zeichen
    for forest in forests:
        forest.draw(window)

    # Park zeichnen
    for park in parks:
        park.draw(window) 

    # Garten zeichnen
    for garden in gardens:
        garden.draw(window)
    
     
      
    # Haus Button zeichnen
    if coins >= 80:
        pygame.draw.rect(window, BLACK, button_house_rect,0,5)
    else:
        pygame.draw.rect(window, GREY, button_house_rect,0,5)
    window.blit(button_house_text, button_house_rect)

    # Fabrik Button zeichnen
    if coins >= 200 and len(gardens) + len(parks)*2 + len(forests) * 4>= len(industrial_units) + len(factories)*2 + len(industrial_plants) * 4:
        pygame.draw.rect(window, BLACK, button_factory_rect, 0, 5)
    else:
        pygame.draw.rect(window, GREY, button_factory_rect,0,5)
    window.blit(button_factory_text, button_factory_rect)

    # Park Button zeichnen
    if coins >= 150:
        pygame.draw.rect(window, BLACK, button_park_rect, 0,5)
    else:
        pygame.draw.rect(window, GREY, button_park_rect, 0,5)
    window.blit(button_park_text, button_park_rect)

    # Anzahl Variablen
    draw_text("Münzen: {}".format(coins),pygame.font.Font(None, 36) ,BLACK, 15, 20, window)
    draw_text("Einwohner: {}".format(habs), pygame.font.Font(None, 36), BLACK,15, 60, window)
    
    if messageboxtext == "Du brauchst 200 Münzen, Parks und genug Einwohner, um eine Fabrik zu kaufen":
        message_box(messageboxtext, pygame.font.Font(None, 16), 300, window)

    elif messageboxtext is not None:
        message_box(messageboxtext, pygame.font.Font(None, 16), 400, window)


    # Fenster aktualisieren
    pygame.display.update()

# Pygame beenden
pygame.quit()