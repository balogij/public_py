import pygame
import random
import math

# --- Beállítások ---
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
NUM_BODIES = 8 # Több test
G = 0.67        # Gravitációs állandó
TIME_STEP = 0.05 # Időlépés (dt)
BACKGROUND_COLOR = (10, 10, 30)
COLLISION_ELASTICITY = 0.9 # Rugalmassági együttható ütközéskor (0-1 között)
                         # 1 = teljesen rugalmas, 0 = teljesen rugalmatlan (összetapadnak)
                         # Jelenleg nem használjuk, mert egyesítjük őket, de hasznos lehet másfajta ütközésnél

# --- Test (Body) Osztály ---
class Body:
    def __init__(self, x, y, mass, color, radius):
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(random.uniform(-3, 3), random.uniform(-3, 3))
        self.mass = mass
        self.color = color
        self.radius = radius
        self.alive = True # Jelzi, hogy a test létezik-e még

    def draw(self, screen):
        if self.alive:
            pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), int(self.radius))

    def apply_force(self, force):
        if self.alive:
            acceleration = force / self.mass
            self.velocity += acceleration * TIME_STEP

    def update_position(self):
        if self.alive:
            self.position += self.velocity * TIME_STEP

            # Falra ütközés (egyszerű visszapattanás) - opcionális
            if self.position.x - self.radius < 0 or self.position.x + self.radius > SCREEN_WIDTH:
                self.velocity.x *= -1 * COLLISION_ELASTICITY
                self.position.x = max(self.radius, min(SCREEN_WIDTH - self.radius, self.position.x)) # Pozíció korrekció
            if self.position.y - self.radius < 0 or self.position.y + self.radius > SCREEN_HEIGHT:
                self.velocity.y *= -1 * COLLISION_ELASTICITY
                self.position.y = max(self.radius, min(SCREEN_HEIGHT - self.radius, self.position.y)) # Pozíció korrekció


# --- Fő Szimulációs Logika ---

def calculate_gravity(body1, body2):
    if not body1.alive or not body2.alive:
        return pygame.math.Vector2(0, 0)

    direction = body2.position - body1.position
    distance_sq = direction.length_squared()

    # Minimalis távolság, hogy elkerüljük az 0-val való osztást és a túl erős vonzást
    # Az ütközés detektálás miatt ezt még kisebbre vehetjük, vagy kikapcsolhatjuk,
    # de a nagyon közeli testeknél instabil lehet a szimuláció.
    # Jelenleg a rádiuszok összegének négyzetére korlátozzuk, hogy a túl közeli erők ne "robbanjanak" fel
    min_dist_sq = (body1.radius + body2.radius) ** 2
    if distance_sq < min_dist_sq: 
        distance_sq = min_dist_sq 

    force_magnitude = G * body1.mass * body2.mass / distance_sq

    force_vector = direction.normalize() * force_magnitude

    return force_vector

def check_collisions(bodies):
    for i in range(len(bodies)):
        if not bodies[i].alive:
            continue
        for j in range(i + 1, len(bodies)): # Csak egyszer ellenőrizzük a párokat
            if not bodies[j].alive:
                continue

            body1 = bodies[i]
            body2 = bodies[j]

            # Távolság kiszámítása a középpontok között
            distance = body1.position.distance_to(body2.position)

            # Ha a távolság kisebb, mint a sugarak összege, akkor ütközés van
            if distance < (body1.radius + body2.radius):
                # Ütközés kezelése: a kisebbik test beolvad a nagyobbikba
                if body1.mass >= body2.mass:
                    absorber = body1
                    absorbed = body2
                else:
                    absorber = body2
                    absorbed = body1

                # Lendület megmaradás: (m1*v1 + m2*v2) / (m1 + m2)
                new_velocity = (absorber.velocity * absorber.mass + absorbed.velocity * absorbed.mass) / (absorber.mass + absorbed.mass)

                absorber.velocity = new_velocity
                absorber.mass += absorbed.mass
                absorber.radius = int(math.sqrt(absorber.mass)) # Frissíti a sugarat az új tömeg alapján
                absorber.color = ((absorber.color[0] + absorbed.color[0]) // 2, 
                                  (absorber.color[1] + absorbed.color[1]) // 2, 
                                  (absorber.color[2] + absorbed.color[2]) // 2) # Átlagolja a színeket

                absorbed.alive = False # A beolvadt testet "megjelöljük" halottnak
                # Opcionálisan: beállíthatjuk a absorbed pozícióját valahova a képernyőn kívülre is


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("2D Gravitációs Szimuláció (N-Body) Ütközéssel")
    clock = pygame.time.Clock()

    # --- Testek inicializálása ---
    bodies = []

    for i in range(NUM_BODIES):
        mass = random.uniform(10, 50)
        radius = int(math.sqrt(mass)) 

        x = random.randint(100, SCREEN_WIDTH - 100)
        y = random.randint(100, SCREEN_HEIGHT - 100)

        color_val = 50 + int(mass * 4) 
        color = (color_val, color_val, 255 - color_val)

        bodies.append(Body(x, y, mass, color, radius))

    # --- Fő játékhurok ---
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 1. Erők kiszámítása
        active_bodies = [body for body in bodies if body.alive]
        for i in range(len(active_bodies)):
            total_force = pygame.math.Vector2(0, 0)
            for j in range(len(active_bodies)):
                if i != j: 
                    force = calculate_gravity(active_bodies[i], active_bodies[j])
                    total_force += force

            active_bodies[i].apply_force(total_force)

        # 2. Ütközések ellenőrzése és kezelése
        check_collisions(active_bodies)

        # 3. Pozíciók frissítése
        for body in active_bodies:
            body.update_position()

        # 4. Rajzolás
        screen.fill(BACKGROUND_COLOR)
        for body in active_bodies:
            body.draw(screen)

        pygame.display.flip()

        clock.tick(60) 

    pygame.quit()

if __name__ == '__main__':
    main()