import pygame
import sys
import math

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (135, 206, 235)  # Light Blue
TREE_COLOR = (139, 69, 19)  # Brown
LEAF_COLOR = (0, 128, 0)  # Green
INITIAL_TREE_HEIGHT = 150
SCALE_FACTOR_INCREMENT = 0.05  # Adjust the scaling speed

# --- Helper Functions ---

def draw_tree(screen, x, y, height, scale):
    """Draws a simple tree with leaves.

    Args:
        screen: The Pygame screen.
        x: The x-coordinate of the base of the tree.
        y: The y-coordinate of the base of the tree.
        height: The base height of the tree trunk.
        scale: The scaling factor.
    """

    scaled_height = height * scale

    # Trunk
    trunk_width = 10 * scale  # Scale the trunk width
    pygame.draw.rect(screen, TREE_COLOR, (x - trunk_width / 2, y - scaled_height, trunk_width, scaled_height))

    # Crown (Simple, stylized)
    crown_width = 50 * scale  # Scale the crown width
    crown_height = 40 * scale # Scale the crown height
    pygame.draw.polygon(screen, LEAF_COLOR, [
        (x, y - scaled_height - crown_height),  # Top
        (x - crown_width / 2, y - scaled_height), # Left base
        (x + crown_width / 2, y - scaled_height), # Right base
    ])



# --- Main Program ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Resizable Tree with Arrow Keys")
    clock = pygame.time.Clock()

    # --- Game Variables ---
    tree_x = SCREEN_WIDTH // 2  # Center the tree horizontally
    tree_y = SCREEN_HEIGHT - 50  # Position the base near the bottom
    tree_scale = 1.0  # Initial scale factor

    # --- Game Loop ---
    running = True
    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #Allow escape to quit
                    running = False


        # --- Input Handling (Scale the tree) ---
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            tree_scale += SCALE_FACTOR_INCREMENT
        if keys[pygame.K_DOWN]:
            tree_scale -= SCALE_FACTOR_INCREMENT
            if tree_scale < 0.1:  # Keep the tree from disappearing
                tree_scale = 0.1


        # --- Update (No specific updates in this simple example) ---


        # --- Drawing ---
        screen.fill(BACKGROUND_COLOR)  # Clear the screen

        draw_tree(screen, tree_x, tree_y, INITIAL_TREE_HEIGHT, tree_scale)


        pygame.display.flip()  # Update the display

        clock.tick(60)  # Limit frame rate to 60 FPS

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()