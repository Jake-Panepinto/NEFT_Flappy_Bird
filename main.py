from sys import exit
import pygame
import config
import components
import population

pygame.init()
clock = pygame.time.Clock()
population = population.Population(100)

def generate_pipes():
    config.pipes.append(components.Pipes(config.win_width))

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def main():
    pipe_spawn_time = 10

    while True:
        quit_game()

        config.window.fill((0, 0, 0))  # Fill the window with black
        
        # Spawn Ground
        config.ground.draw(config.window)

        # Spawn Pipes
        if pipe_spawn_time <= 0:
            generate_pipes()
            pipe_spawn_time = 200
        pipe_spawn_time -= 1

        for p in config.pipes:
            p.draw(config.window)
            p.update()
            if p.off_screen:
                config.pipes.remove(p)
                config.pipes[0].draw(config.window)

        if not population.extinct():
            population.update_live_players()

        else:
            pass

        clock.tick(60)
        pygame.display.flip()

main()