import pygame

# Initialisierung
pygame.init()

# Bildschirmgröße
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Schriftart
font = pygame.font.Font(None, 36)

# Spielvariablen
coins = 200
houses = []
selected_house = None
offset_x = 0
offset_y = 0

# Laden des Hausbildes
house_image = pygame.image.load("house.png")

# Funktion, um Text auf dem Bildschirm anzuzeigen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

# Hauptspiel-Schleife
running = True
clock = pygame.time.Clock()

while running:
    # Hintergrund zeichnen
    screen.fill(WHITE)

    # Ereignisse überprüfen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Überprüfen, ob der Knopf gedrückt wurde
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                button_rect = pygame.Rect(10, 10, 100, 50)
                if button_rect.collidepoint(mouse_pos):
                    # Überprüfen, ob genug Münzen vorhanden sind
                    if coins >= 100:
                        coins -= 100
                        houses.append(pygame.Rect(mouse_pos[0], mouse_pos[1], 50, 50))
            # Überprüfen, ob ein Haus angeklickt wurde
            elif event.button == 3:
                mouse_pos = pygame.mouse.get_pos()
                for house in houses:
                    if house.collidepoint(mouse_pos):
                        if selected_house == house:
                            selected_house = None
                        else:
                            selected_house = house
                            offset_x = mouse_pos[0] - house.x
                            offset_y = mouse_pos[1] - house.y
        elif event.type == pygame.MOUSEMOTION:
            # Überprüfen, ob ein Haus ausgewählt ist und die Maus bewegt wird
            if selected_house is not None:
                mouse_pos = pygame.mouse.get_pos()
                selected_house.x = mouse_pos[0] - offset_x
                selected_house.y = mouse_pos[1] - offset_y

    # Tasteneingabe überprüfen
    keys = pygame.key.get_pressed()
    if selected_house is not None:
        if keys[pygame.K_LEFT]:
            selected_house.x -= 5
        elif keys[pygame.K_RIGHT]:
            selected_house.x += 5
        elif keys[pygame.K_UP]:
            selected_house.y -= 5
        elif keys[pygame.K_DOWN]:
            selected_house.y += 5

    # Knopf zeichnen
    pygame.draw.rect(screen, BLACK, (10, 10, 100, 50))
    draw_text("Haus kaufen", font, WHITE, 15, 20)

    # Anzeige für das Geld zeichnen
    draw_text("Münzen: {}".format(coins), font, BLACK, 10, 70)

    # Häuser zeichnen
    for house in houses:
        screen.blit(house_image, house)
        if house == selected_house:
            pygame.draw.rect(screen, BLUE, house, 3)

    # Aktualisierung des Bildschirms
    pygame.display.flip()
    clock.tick(60)

pygame.quit()