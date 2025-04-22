import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Create the groups
    all_sprites = pygame.sprite.Group()  # New group for all sprites
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    collidable = pygame.sprite.Group()   # New group for objects that can collide
    
    # Set the containers for the Player class
    # Player is in all_sprites, updatable, drawable, and collidable
    Player.containers = (all_sprites, updatable, drawable, collidable)
    
    # Create the player in the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    running = True
    while running:
        # Check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update delta time first
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds
        
        # Update all updatable objects
        updatable.update(dt)
        
        # Example of collision detection (if you had other collidable objects)
        # This would check if player collides with any other collidable object
        # collisions = pygame.sprite.spritecollide(player, collidable, False)
        # for collision in collisions:
        #     if collision != player:  # Don't collide with yourself!
        #         handle_collision(player, collision)
        
        # Fill the screen with black
        screen.fill("black")
        
        # Draw all drawable objects
        for entity in drawable:
            entity.draw(screen)
        
        # Alternative way to draw all sprites (if they use the standard Sprite draw method)
        # all_sprites.
        
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
