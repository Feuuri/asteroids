import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
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
        
        # Update the player state
        player.update(dt)
        
        # Fill the screen with black
        screen.fill("black")
        
        # Draw the player (after updating)
        player.draw(screen)
        
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
