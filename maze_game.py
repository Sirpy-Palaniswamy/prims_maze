import pygame
from random import shuffle, randint
import random
import time

cell_size = 3 
maze_length = 600
maze_height = 600

black = (0, 0, 0)
white = (245, 245, 245)
red = (255, 0, 0)
blue = (0, 0, 255)

passage_list = []
potential_passage_list = []
impossible_passage = []
random_cell = []
done = False

pygame.init()
pygame.display.set_caption("Get to the red square!")
screen = pygame.display.set_mode((600, 600))
pygame.display.flip()

def one_connection(cell_x, cell_y):
    count = 0

    if [cell_x + cell_size, cell_y] in passage_list:
        count += 1
    if [cell_x - cell_size, cell_y] in passage_list:
        count += 1
    if [cell_x, cell_y + cell_size] in passage_list:
        count += 1
    if [cell_x, cell_y - cell_size] in passage_list:
        count += 1

    if count <= 1:
        return True
    else:
        return False


def valid_cell(cell_x, cell_y):
    if [cell_x, cell_y] in potential_passage_list:
        impossible_passage.append([cell_x, cell_y])
    elif [cell_x, cell_y] in impossible_passage:
        impossible_passage.append([cell_x, cell_y])
    elif cell_x < 0 or cell_x >= maze_length - cell_size or cell_y < 0 or cell_y >= maze_height - cell_size:
        impossible_passage.append([cell_x, cell_y])
    elif not one_connection(cell_x, cell_y):
        impossible_passage.append([cell_x, cell_y])
    elif (([cell_x + cell_size, cell_y + cell_size] in passage_list and [cell_x + cell_size, cell_y] not in
           passage_list and [cell_x, cell_y + cell_size] not in passage_list) or
          ([cell_x + cell_size, cell_y - cell_size] in passage_list and [cell_x + cell_size, cell_y] not in
           passage_list and [cell_x, cell_y - cell_size] not in passage_list) or
          ([cell_x - cell_size, cell_y + cell_size] in passage_list and [cell_x - cell_size, cell_y] not in
           passage_list and [cell_x, cell_y + cell_size] not in passage_list) or
          ([cell_x - cell_size, cell_y - cell_size] in passage_list and [cell_x - cell_size, cell_y] not in
           passage_list and [cell_x, cell_y - cell_size] not in passage_list)):

        impossible_passage.append([cell_x, cell_y])
    elif [cell_x, cell_y] not in passage_list:
        return True


def maze_passage(cell_x, cell_y):
    block_passage_list = []
    potential_passage_list.remove([cell_x, cell_y])
    if valid_cell(cell_x, cell_y):
        pygame.draw.rect(screen, white, [cell_x, cell_y, cell_size, cell_size])
        pygame.display.update()

        passage_list.append([cell_x, cell_y])

        if valid_cell(cell_x + cell_size, cell_y):
            block_passage_list.append([cell_x + cell_size, cell_y])
        if valid_cell(cell_x - cell_size, cell_y):
            block_passage_list.append([cell_x - cell_size, cell_y])
        if valid_cell(cell_x, cell_y + cell_size):
            block_passage_list.append([cell_x, cell_y + cell_size])
        if valid_cell(cell_x, cell_y - cell_size):
            block_passage_list.append([cell_x, cell_y - cell_size])

        shuffle(block_passage_list)

        for j in block_passage_list:
            potential_passage_list.append(j)


start_cell = [randint(0, int(maze_height / cell_size))*cell_size, randint(0, int(maze_height / cell_size))*cell_size]
potential_passage_list.append([start_cell[0], start_cell[1]])

maze_init=True
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if [runner_x,runner_y-cell_size] in passage_list:
                    pygame.draw.rect(screen, white, [runner_x, runner_y, cell_size , cell_size ])
                    runner_y=runner_y-cell_size
                    pygame.draw.rect(screen, red, [runner_x, runner_y, cell_size , cell_size ])
                
                    if (runner_x==destination_x and runner_y==destination_y):
                        
                        new_loc=random.choice(passage_list)
                        destination_x=new_loc[1]
                        destination_y=new_loc[0]
                        pygame.draw.rect(screen, blue, [destination_x, destination_y, cell_size , cell_size ])
                        print("Game Completed")
                    pygame.display.update()
            elif event.key == pygame.K_DOWN:
                if [runner_x,runner_y+cell_size] in passage_list:
                    pygame.draw.rect(screen, white, [runner_x, runner_y, cell_size , cell_size ])
                    runner_y=runner_y+cell_size
                    pygame.draw.rect(screen, red, [runner_x, runner_y, cell_size , cell_size ])
          
                    if (runner_x==destination_x and runner_y==destination_y):
                        new_loc=random.choice(passage_list)
                        destination_x=new_loc[1]
                        destination_y=new_loc[0]
                        pygame.draw.rect(screen, blue, [destination_x, destination_y, cell_size , cell_size ])
                        print("Game Completed")
                    pygame.display.update()
            elif event.key == pygame.K_LEFT:
                if [runner_x-cell_size,runner_y] in passage_list:
                    pygame.draw.rect(screen, white, [runner_x, runner_y, cell_size , cell_size ])
                    runner_x=runner_x-cell_size
                    pygame.draw.rect(screen, red, [runner_x, runner_y, cell_size , cell_size ])
                    
                    if (runner_x==destination_x and runner_y==destination_y):
                        new_loc=random.choice(passage_list)
                        destination_x=new_loc[1]
                        destination_y=new_loc[0]
                        pygame.draw.rect(screen, blue, [destination_x, destination_y, cell_size , cell_size ])
                        print("Game Completed")
                    pygame.display.update()
            elif event.key == pygame.K_RIGHT:
                if [runner_x+cell_size,runner_y] in passage_list:
                    pygame.draw.rect(screen, white, [runner_x, runner_y, cell_size , cell_size ])
                    runner_x=runner_x+cell_size
                    pygame.draw.rect(screen, red, [runner_x, runner_y, cell_size , cell_size ])
                    
                    if (runner_x==destination_x and runner_y==destination_y):
                        new_loc=random.choice(passage_list)
                        destination_x=new_loc[1]
                        destination_y=new_loc[0]
                        pygame.draw.rect(screen, blue, [destination_x, destination_y, cell_size , cell_size ])
                        print("Game Completed")
                    pygame.display.update()
            else:

                pass

    for i in range(1, len(potential_passage_list) + 1):
        if randint(0, int(len(passage_list) / 50)) == 0:
            maze_passage(potential_passage_list[-i][0], potential_passage_list[-i][1])
            break

    if not potential_passage_list:
        passage_list.sort()
        
        if maze_init:
            runner_y=passage_list[0][0]
            runner_x=passage_list[0][1] 
            pygame.draw.rect(screen, red, [runner_y, runner_x, cell_size , cell_size ])
            print("Initiated")
            maze_init=False
            destination_y=passage_list[-1][0]
            destination_x=passage_list[-1][1]

            pygame.draw.rect(screen, blue, [destination_y, destination_x , cell_size , cell_size])
        
        pygame.display.update()