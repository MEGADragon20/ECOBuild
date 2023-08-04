import pygame
import os
import random as r
import time

# Funktionen
def load_image(path):
    return pygame.image.load(path)

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

def test_dragging(list_building_type, event):
    for i in list_building_type:
        if i.rect.collidepoint(event.pos):
            i.dragging = True
            break

def stop_dragging(list_building_type):
    for i in list_building_type:
        i.dragging = False

def merge(list_to_merge, new_element_class, new_element_list, class_h, class_w):
    for i in list_to_merge:
        for j in list_to_merge:
            if j != i:
                if i.rect.colliderect(j):
                    new_building = new_element_class(j.rect.x, j.rect.y, new_element_class, class_h, class_w)
                    new_element_list.append(new_building)
                    buildings.append(new_building)
                    if i in list_to_merge:
                        list_to_merge.remove(i)
                        buildings.remove(i)
                    if j in list_to_merge:
                        list_to_merge.remove(j)
                        buildings.remove(j)

def drag(list, event):
     for i in list:
        if i.dragging:
            i.rect.x += event.rel[0]
            i.rect.y += event.rel[1]

def draw_buildings(liste, space):
    render_list_reihenfolge = sort_for_height(liste)
    for i in render_list_reihenfolge:
        i.draw(space)


def sort_for_height(liste):
    if len(liste) <= 1:
        return liste
    pivot = liste[-1].rect.y + liste[-1].height
    less_than_pivot = []
    equal_to_pivot = []
    greater_than_pivot = []
    for element in liste:
        if (element.rect.y + element.height) < pivot:
            less_than_pivot.append(element)
        elif (element.rect.y + element.height) == pivot:
            equal_to_pivot.append(element)
        else:
            greater_than_pivot.append(element)
    sorted_less = sort_for_height(less_than_pivot)
    sorted_greater = sort_for_height(greater_than_pivot)
    return sorted_less + equal_to_pivot + sorted_greater

def paint_street():
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    a = Street(x,y)
    streets.append(a)

        

def earn(houses, villas, mansions, manors, industrial_units, factories):
    return len(houses) * 20 + len(villas) * 60 + len(mansions) * 150 + len(manors) * 350 + len(industrial_units) * 100 + len(factories) * 220 + len(industrial_plants) * 500

def count_habs(houses, villas, mansions, manors):
    return len(houses) * 1 + len(villas) * 2 + len(mansions) * 4 + len(manors) * 8

# leeren platz finden
def locate_place():
    a = r.randint(80, 944)
    b = r.randint(80, 630)
    for house in houses:
        if a == house.rect.x and b == house.rect.y or a == house.rect.x +64 and b == house.rect.y +64:
            return locate_place()
    return a, b


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

STREET_IMAGE_PATH = "pictures/street.png"

#Bildgrößen 
HOUSE_WIDTH = 84
HOUSE_HEIGHT = 76
VILLA_WIDTH = 108
VILLA_HEIGHT = 76
MANSION_WIDTH = 108
MANSION_HEIGHT = 110
MANOR_WIDTH = 144
MANOR_HEIGHT = 110
INDUSTRIAL_UNIT_WIDTH = 116
INDUSTRIAL_UNIT_HEIGHT = 84
FACTORY_WIDTH = 120
FACTORY_HEIGHT = 68
INDUSTRIAL_PLANT_WIDTH = 128
INDUSTRIAL_PLANT_HEIGHT = 128
GARDEN_WIDTH = 34
GARDEN_HEIGHT = 18
PARK_WIDTH = 70
PARK_HEIGHT = 34
FOREST_WIDTH = 48 
FOREST_HEIGHT = 34

# Start Variablen
coins = 80
habs = 0

buildings = []
houses = []
villas = []
mansions = []
manors = []
industrial_units = []
factories = []
industrial_plants = []
gardens = []
parks = []
forests = []

streets = []

# Klassen
class House:
    def __init__(self, x, y, klasse, height, width):
        self.rect = load_image(HOUSE_IMAGE_PATH).get_rect()
        self.rect.x = x
        self.rect.y = y
        self.klasse = klasse
        self.height = height
        self.width = width
        self.dragging = False

    def draw(self, surface):
        surface.blit(load_image(HOUSE_IMAGE_PATH), self.rect)

class Villa:
    def __init__(self, x, y, klasse, height, width):
        self.rect = load_image(VILLA_IMAGE_PATH).get_rect()
        self.rect.x = x
        self.rect.y = y
        self.klasse = klasse
        self.height = height
        self.width = width
        self.dragging = False

    def draw(self, surface):
        surface.blit(load_image(VILLA_IMAGE_PATH), self.rect)

class Mansion:
    def __init__(self, x, y, klasse, height, width):
        self.rect = load_image(MANSION_IMAGE_PATH).get_rect()
        self.rect.x = x
        self.rect.y = y
        self.klasse = klasse
        self.height = height
        self.width = width
        self.dragging = False

    def draw(self, surface):
        surface.blit(load_image(MANSION_IMAGE_PATH), self.rect)

class Manor:
    def __init__(self, x, y, klasse, height, width):
        self.rect = load_image(MANOR_IMAGE_PATH).get_rect()
        self.rect.x = x
        self.rect.y = y
        self.klasse = klasse
        self.height = height
        self.width = width
        self.dragging = False

    def draw(self, surface):
        surface.blit(load_image(MANOR_IMAGE_PATH), self.rect)

class Industrial_unit:
    def __init__(self, x, y, klasse, height, width):
        self.rect = load_image(INDUSTRIAL_UNIT_IMAGE_PATH).get_rect()
        self.rect.x = x
        self.rect.y = y
        self.klasse = klasse
        self.height = height
        self.width = width
        self.dragging = False

    def draw(self, surface):
        surface.blit(load_image(INDUSTRIAL_UNIT_IMAGE_PATH), self.rect)

class Factory:
    def __init__(self, x, y, klasse, height, width):
        self.rect = load_image(FACTORY_IMAGE_PATH).get_rect()
        self.rect.x = x
        self.rect.y = y
        self.klasse = klasse
        self.height = height
        self.width = width
        self.dragging = False

    def draw(self, surface):
        surface.blit(load_image(FACTORY_IMAGE_PATH), self.rect)
    
class Industrial_Plant:
    def __init__(self, x, y, klasse, height, width):
        self.rect = load_image(INDUSTRIAL_PLANT_IMAGE_PATH).get_rect()
        self.rect.x = x
        self.rect.y = y
        self.klasse = klasse
        self.height = height
        self.width = width
        self.dragging = False

    def draw(self, surface):
        surface.blit(load_image(INDUSTRIAL_PLANT_IMAGE_PATH), self.rect)

class Garden:
    def __init__(self, x, y, klasse, height, width):
        self.rect = load_image(GARDEN_IMAGE_PATH).get_rect()
        self.rect.x = x
        self.rect.y = y
        self.klasse = klasse
        self.height = height
        self.width = width
        self.dragging = False

    def draw(self, surface):
        surface.blit(load_image(GARDEN_IMAGE_PATH), self.rect)

class Park:
    def __init__(self, x, y, klasse, height, width):
        self.rect = load_image(PARK_IMAGE_PATH).get_rect()
        self.rect.x = x
        self.rect.y = y
        self.klasse = klasse
        self.height = height
        self.width = width
        self.dragging = False

    def draw(self, surface):
        surface.blit(load_image(PARK_IMAGE_PATH), self.rect)

class Forest:
    def __init__(self, x, y, klasse, height, width):
        self.rect = load_image(FOREST_IMAGE_PATH).get_rect()
        self.rect.x = x
        self.rect.y = y
        self.klasse = klasse
        self.height = height
        self.width = width
        self.dragging = False

    def draw(self, surface):
        surface.blit(load_image(FOREST_IMAGE_PATH), self.rect)

class Street:
    def __init__(self, x, y):
        self.rect = load_image(FOREST_IMAGE_PATH).get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dragging = False

    def draw(self, surface):
        surface.blit(load_image(STREET_IMAGE_PATH), self.rect)

# Fenster erstellen
bg = pygame.image.load("background.png")
window = pygame.display.set_mode(WINDOW_SIZE)
is_fullscreen = False
pygame.display.set_caption("ECOBuild")
pygame.init()
pygame.time.set_timer(618, 60000)

# INIT
# Start-Häuser erstellen
start_house1 = House(WIDTH // 2 - load_image(HOUSE_IMAGE_PATH).get_width() - 30, HEIGHT // 2 - load_image(HOUSE_IMAGE_PATH).get_height() + 20, House, HOUSE_HEIGHT, HOUSE_WIDTH)
start_house2 = House(WIDTH // 2, HEIGHT // 2 - load_image(HOUSE_IMAGE_PATH).get_height(), House, HOUSE_HEIGHT, HOUSE_WIDTH)

houses.append(start_house1)
houses.append(start_house2)
buildings.append(start_house1)
buildings.append(start_house2)

# init -> none everything
messageboxtext = None
street_draw = False
street_erase = False
street_drawing = True
street_erasing = True

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

# HAUPTSCHLEIFE
running = True
while running:
    habs = count_habs(houses, villas, mansions, manors)
    # Ereignisse prüfen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            test_dragging(buildings, event)
            if button_house_rect.collidepoint(event.pos):
                if coins >= 80:
                    coins -= 80
                    x2, y2 = locate_place()
                    new_house = House(x2,y2, House, HOUSE_HEIGHT, HOUSE_WIDTH)
                    houses.append(new_house)
                    buildings.append(new_house)
                else:
                    messageboxtext = "Du brauchst 80 Münzen, um ein Haus zu kaufen"
            # Prüfen, ob der Fabrik kaufen Button geklickt wurde
            if button_factory_rect.collidepoint(event.pos):
                if coins >= 200 and len(gardens) + len(parks) * 2 + len(forests) * 4>= len(industrial_units) + len(factories) and habs > len(industrial_units) * 1 + len(factories) * 2 + len(industrial_plants) * 4:
                    coins -=200
                    x2, y2 = locate_place()
                    new_industrial_unit = Industrial_unit(x2,y2, Industrial_unit, INDUSTRIAL_UNIT_HEIGHT, INDUSTRIAL_UNIT_WIDTH)
                    industrial_units.append(new_industrial_unit)
                    buildings.append(new_industrial_unit)
                else:
                    messageboxtext = "Du brauchst 200 Münzen, Parks und genug Einwohner, um eine Fabrik zu kaufen"
                
            # Prüfen, ob der Park kaufen Button geklickt wurde
            if button_park_rect.collidepoint(event.pos):
                if coins >= 150:
                    coins -= 150
                    x2, y2 = locate_place()
                    new_garden = Garden(x2,y2, Garden, GARDEN_HEIGHT, GARDEN_WIDTH)
                    gardens.append(new_garden)
                    buildings.append(new_garden)
                else:
                    messageboxtext = "Du brauchst 150 Münzen, um ein Park zu kaufen"
            if street_draw:
                street_drawing = True
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
            elif event.key == pygame.K_ESCAPE:
                    if is_fullscreen:
                        pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
                        is_fulscreen = False
            elif event.key == pygame.K_s:
                if street_draw:
                    street_draw = False
                else:
                    street_draw = True
            elif event.key == pygame.K_d:
                if street_erase:
                    street_erase = False
                else:
                    street_erase = True
            elif event.key == pygame.K_q:
                running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            stop_dragging(buildings)
            merge(houses, Villa, villas, VILLA_HEIGHT, VILLA_WIDTH)
            merge(villas, Mansion, mansions, MANSION_HEIGHT, MANSION_WIDTH)
            merge(mansions, Manor, manors, MANOR_HEIGHT, MANOR_WIDTH)
            merge(industrial_units, Factory, factories, FACTORY_HEIGHT, FACTORY_WIDTH)
            merge(factories, Industrial_Plant, industrial_plants, INDUSTRIAL_PLANT_HEIGHT, INDUSTRIAL_PLANT_WIDTH)
            merge(gardens, Park, parks, PARK_HEIGHT, PARK_WIDTH)
            merge(parks, Forest, forests, FOREST_HEIGHT, FOREST_WIDTH)
        elif event.type == pygame.MOUSEMOTION:
            drag(buildings, event)
        elif event.type == 618:
            coins += earn(houses, villas, mansions, manors, industrial_units, factories)
            messageboxtext = None
    if street_draw:
        paint_street()
    
    window.blit(bg, (0,0))

    for street in streets:
        street.draw(window)

    draw_buildings(buildings, window)

    # Haus Button zeichnen
    if coins >= 80:
        pygame.draw.rect(window, BLACK, button_house_rect,0,5)
    else:
        pygame.draw.rect(window, GREY, button_house_rect,0,5)
    window.blit(button_house_text, button_house_rect)

    # Fabrik Button zeichnen
    if coins >= 200 and len(gardens) + len(parks)*2 + len(forests) * 4>= len(industrial_units) + len(factories) + len(industrial_plants):
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
