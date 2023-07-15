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
active_house = None

# Laden des Hausbildes
house_image = pygame.image.load("house.png")
house_width, house_height = house_image.get_width(), house_image.get_height()

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
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                button_rect = pygame.Rect(10, 10, 100, 50)
                if button_rect.collidepoint(mouse_pos):
                    # Überprüfen, ob genug Münzen vorhanden sind
                    if coins >= 100:
                        coins -= 100
                        house_rect = pygame.Rect((width - house_width) // 2, (height - house_height) // 2, house_width, house_height)
                        houses.append(house_rect)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                active_house = None
        elif event.type == pygame.MOUSEMOTION:
            if active_house is not None:
                houses[active_house].x += event.rel[0]
                houses[active_house].y += event.rel[1]

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