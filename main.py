import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Set up the screen
    clock = pygame.time.Clock()  # Initialize the Clock for FPS management
    dt = 0  # Initialize delta time
    
    # Create the player in the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    running = True
    while running:
        # Check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Fill the screen with black
        screen.fill("black")
        
        # Draw the player
        player.draw(screen)
        
        # Update the display
        pygame.display.flip()
        
        # Tick the clock and update delta time
        dt = clock.tick(60) / 1000  # Limit FPS to 60 and calculate delta time in seconds

if __name__ == "__main__":
    main()
