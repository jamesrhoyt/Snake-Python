# Import Statements
import pygame
import time
import random

# Initialize Modules
pygame.init()

# Set up the game window
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Snake (Python)')

# Initialize the Color variables
colors = [
    (255,255,255), # White
    (255,0,0),     # Red
    (255,130,0),   # Orange
    (255,233,0),   # Yellow
    (120,190,33),  # Lime Green
    (0,255,0),     # Green
    (0,181,226),   # Light Blue
    (0,0,255),     # Blue
    (155,38,182),  # Violet
    (151,153,155)] # Gray
current_color = 0 # The current index of the selected color
black = (0,0,0)

# Initialize the Timer, Speed, and Size variables
clock = pygame.time.Clock()
snake_speed = 12
snake_block = dis_height / 30

# Set whether or not to automatically restart on Game Over during Autoplay
looping = False

# Set whether or not to display the "Loop" and "Hide" Prompts during Autoplay
displayLoopText = True

# Set up the game messages
font_style = pygame.font.SysFont('Impact', int(dis_height / 12.5))
finalscore_text = "SCORE: "
reset_text = "PRESS 'R' TO RESET"
quit_text = "[ESC] QUIT"
colors_text = "1-0: CHANGE COLORS"
autoplay_text = "[P] AUTOPLAY"
bored_text = "[P] I'M BORED, PLAY FOR ME"
stop_text = "[P] STOP PLAYING FOR ME"
loop_text = "[L] LOOP"
hide_text = "[H] HIDE/SHOW"
looping_text = "[LOOPING]"
def message(msg,x,y):
    mesg = font_style.render(msg, True, colors[current_color])
    dis.blit(mesg, [x,y])

# Draw the Snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, colors[current_color], [x[0], x[1], snake_block, snake_block])

# Manage the loop to run and reset the game
def gameLoop():
    #Initialize the Game State Management variables
    game_over = False
    game_close = False

    # Initialize the Movement variables
    x1 = dis_width/2
    y1 = dis_height/2
    x1_change = 0
    y1_change = 0

    # Retrieve the global Color variable
    global current_color

    # Initialize the Snake and Score (Score is used to measure Snake length)
    snake_List = []
    score = 0

    # Randomize food placement
    foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
    food_placed = True

    while not game_over:
        # Handle the Game Over/Restart state
        while game_close==True:
            # Draw the current game state
            dis.fill(black)
            pygame.draw.rect(dis, colors[current_color], [foodx,foody,snake_block,snake_block])
            draw_snake(snake_block, snake_List)
            message(str(score), dis_width - font_style.size(str(score))[0] - 4, 4)
            # Print the Game Over messages
            message(finalscore_text+str(score),(dis_width/2)-(font_style.size(finalscore_text+str(score))[0]/2), (dis_height/4))
            message(reset_text, (dis_width/2)-(font_style.size(reset_text)[0]/2), (dis_height/4) + font_style.size(reset_text)[1] + 16)
            message(quit_text, dis_width - font_style.size(quit_text)[0] - 8, dis_height - font_style.size(quit_text)[1] - 8)
            message(colors_text, 8, 8)
            message(bored_text, 8, dis_height - font_style.size(bored_text)[1] - 8)
            pygame.display.update()
            for event in pygame.event.get():
                # Quit if the "Close" Button is pressed
                if event.type==pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type==pygame.KEYDOWN:
                    # R: Reset the game
                    if event.key==pygame.K_r:
                        gameLoop()
                    # P: Start playing the game automatically
                    if event.key==pygame.K_p:
                        gameLoopAuto()
                    # Esc: Quit the game
                    if event.key==pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    # 1-0: Change the display Color
                    if event.key==pygame.K_0 or event.key==pygame.K_KP0:
                        current_color = 0
                    if event.key==pygame.K_1 or event.key==pygame.K_KP1:
                        current_color = 1
                    if event.key==pygame.K_2 or event.key==pygame.K_KP2:
                        current_color = 2
                    if event.key==pygame.K_3 or event.key==pygame.K_KP3:
                        current_color = 3
                    if event.key==pygame.K_4 or event.key==pygame.K_KP4:
                        current_color = 4
                    if event.key==pygame.K_5 or event.key==pygame.K_KP5:
                        current_color = 5
                    if event.key==pygame.K_6 or event.key==pygame.K_KP6:
                        current_color = 6
                    if event.key==pygame.K_7 or event.key==pygame.K_KP7:
                        current_color = 7
                    if event.key==pygame.K_8 or event.key==pygame.K_KP8:
                        current_color = 8
                    if event.key==pygame.K_9 or event.key==pygame.K_KP9:
                        current_color = 9
                        
        for event in pygame.event.get():
            # Quit if the "Close" Button is pressed
            if event.type==pygame.QUIT:
                game_over = True
            # Change the Snake's direction when the Arrows are pressed.
            if event.type==pygame.KEYDOWN:
                # Left/A:
                if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                    # If "Right" is the current direction, don't allow backwards movement
                    if x1_change != snake_block:
                        x1_change = -snake_block
                        y1_change = 0
                # Right/D:
                elif event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                    # If "Left" is the current direction, don't allow backwards movement
                    if x1_change != -snake_block:
                        x1_change = snake_block
                        y1_change = 0
                # Up/W:
                elif event.key==pygame.K_UP or event.key==pygame.K_w:
                    # If "Down" is the current direction, don't allow backwards movement
                    if y1_change != snake_block:
                        x1_change = 0
                        y1_change = -snake_block
                # Down/S:
                elif event.key==pygame.K_DOWN or event.key==pygame.K_s:
                    # If "Up" is the current direction, don't allow backwards movement
                    if y1_change != -snake_block:
                        x1_change = 0
                        y1_change = snake_block
                # 1-0: Change the display Color
                if event.key==pygame.K_0 or event.key==pygame.K_KP0:
                    current_color = 0
                if event.key==pygame.K_1 or event.key==pygame.K_KP1:
                    current_color = 1
                if event.key==pygame.K_2 or event.key==pygame.K_KP2:
                    current_color = 2
                if event.key==pygame.K_3 or event.key==pygame.K_KP3:
                    current_color = 3
                if event.key==pygame.K_4 or event.key==pygame.K_KP4:
                    current_color = 4
                if event.key==pygame.K_5 or event.key==pygame.K_KP5:
                    current_color = 5
                if event.key==pygame.K_6 or event.key==pygame.K_KP6:
                    current_color = 6
                if event.key==pygame.K_7 or event.key==pygame.K_KP7:
                    current_color = 7
                if event.key==pygame.K_8 or event.key==pygame.K_KP8:
                    current_color = 8
                if event.key==pygame.K_9 or event.key==pygame.K_KP9:
                    current_color = 9
                # P: Enable Autoplay (only available before starting)
                if event.key==pygame.K_p and x1_change==0 and y1_change==0:
                    gameLoopAuto()
        # If the Snake hits a wall, Game Over.
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        # Update the Snake's position
        x1 += x1_change
        y1 += y1_change
        # Refresh the Window
        dis.fill(black)
        # Draw the Food
        pygame.draw.rect(dis, colors[current_color], [foodx,foody,snake_block,snake_block])
        # Add another block to the Snake
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        # Keep the Snake the appropriate length by removing the first element
        # The Snake is essentially drawn backward, relative to its array order and perceived movement direction
        if(len(snake_List) > score + 1):
            del snake_List[0]
        # If the Head of the Snake has collided with its Body anywhere, Game Over.
        for x in snake_List[:-1]:
            if x==snake_Head:
                game_close = True
        # Draw the Snake
        draw_snake(snake_block, snake_List)
        # Draw the Score
        message(str(score), dis_width - font_style.size(str(score))[0] - 4, 4)
        # Draw the Autoplay Prompt (if the game hasn't started yet).
        if x1_change==0 and y1_change==0:
            message(autoplay_text, 8, dis_height - font_style.size(autoplay_text)[1] - 8)
        # Update the Window
        pygame.display.update()
        #If the Snake collides with the Food, increase the Score and reset the Food
        if x1==foodx and y1==foody:
            score += 1
            foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            # Make sure the Food is not under any part of the Snake body.
            food_placed = False
            while not food_placed:
                food_placed = True
                for x in snake_List:
                    if x == [foodx, foody]:
                        food_placed = False
                        # print("Replacing Food...") # Use this to test how often the Food has to be moved.
                        foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
                        foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

        # Refresh "snake_speed" times per second (currently 12)
        clock.tick(snake_speed)

    # Uninitialize Everything
    pygame.quit()
    quit()

# Determine what Direction the Snake should move in at every step.
def chooseDirection(x1, y1, x1_change, y1_change, foodx, foody, snake_List):
    # First, determine which adjacent spaces are blocked by the Snake's body.
    up_blocked = False
    down_blocked = False
    left_blocked = False
    right_blocked = False
    # Iterate through the Snake's body and trip any "adjacent-square" flags.
    for body in snake_List[:-1]:
        if body==[x1,y1 - snake_block]:
            up_blocked = True
        elif body==[x1,y1 + snake_block]:
            down_blocked = True
        elif body==[x1 - snake_block,y1]:
            left_blocked = True
        elif body==[x1 + snake_block,y1]:
            right_blocked = True
    # Also trip any "adjacent-square" flags if the Snake head is against an edge of the play field.
    if y1 == 0:
        up_blocked = True
    if y1 == dis_height - snake_block:
        down_blocked = True
    if x1 == 0:
        left_blocked = True
    if x1 == dis_width - snake_block:
        right_blocked = True
    # Second, see if moving into this square will get us closer to the Food.
    up_closer = False
    down_closer = False
    left_closer = False
    right_closer = False
    # There's no need to "sqrt" the distances - if the squared value is less than, the value itself would be as well.
    # Check if "Up" will move us closer.
    if ((x1-foodx)**2+((y1-snake_block)-foody)**2) < ((x1-foodx)**2)+((y1-foody)**2):
        up_closer = True
    # Check if "Down" will move us closer.
    if ((x1-foodx)**2+((y1+snake_block)-foody)**2) < ((x1-foodx)**2)+((y1-foody)**2):
        down_closer = True
    # Check if "Left" will move us closer.
    if (((x1-snake_block)-foodx)**2+(y1-foody)**2) < ((x1-foodx)**2)+((y1-foody)**2):
        left_closer = True
    # Check if "Right" will move us closer.
    if (((x1+snake_block)-foodx)**2+(y1-foody)**2) < ((x1-foodx)**2)+((y1-foody)**2):
        right_closer = True
    # Check if "Up" is not blocked and will move us closer.
    if not up_blocked and up_closer:
        # If the Snake is already moving Up, or hasn't moved at all yet, return "Up".
        if y1_change == -snake_block or (x1_change==0 and y1_change==0):
            return (0,-snake_block)
        # Determine whether or not moving closer to the Food will inadvertantly trap the Snake.
        else:
            for i in range(1, 7):
                for x in snake_List[:-1]:
                    # If a blockage is closer toward "Up", return either "Left", "Right", or "Down".
                    if [x1, y1 - (snake_block * i)] == x:
                        # If already heading Left and Left isn't blocked, go Left.
                        if x1_change == -snake_block and not left_blocked:
                            return (-snake_block, 0)
                        # If already heading Right and Right isn't blocked, go Right.
                        elif x1_change == snake_block and not right_blocked:
                            return (snake_block, 0)
                        # Otherwise, if Down isn't blocked, return "Down".
                        elif not down_blocked:
                            return (0,snake_block)
            # If not, return Up.
            return (0,-snake_block)
    # Check if "Down" is not blocked and will move us closer.
    if not down_blocked and down_closer:
        # If the Snake is already moving Down, or hasn't moved at all yet, return "Down".
        if y1_change == snake_block or (x1_change==0 and y1_change==0):
            return (0,snake_block)
        # Determine whether or not moving closer to the Food will inadvertantly trap the Snake.
        else:
            for i in range(1, 7):
                for x in snake_List[:-1]:
                    # If a blockage is closer toward "Down", return either "Left", "Right", or "Up".
                    if [x1, y1 + (snake_block * i)] == x:
                        # If already heading Left and Left isn't blocked, go Left.
                        if x1_change == -snake_block and not left_blocked:
                            return (-snake_block, 0)
                        # If already heading Right and Right isn't blocked, go Right.
                        elif x1_change == snake_block and not right_blocked:
                            return (snake_block, 0)
                        # Otherwise, return "Up".
                        elif not up_blocked:
                            return (0,-snake_block)
            # If not, return Down.
            return (0,snake_block)
    # Check if "Left" is not blocked and will move us closer.
    if not left_blocked and left_closer:
        # If the Snake is already moving Left, or hasn't moved at all yet, return "Left".
        if x1_change == -snake_block or (x1_change==0 and y1_change==0):
            return (-snake_block,0)
        # Determine whether or not moving closer to the Food will inadvertantly trap the Snake.
        else:
            for i in range(1, 7):
                for x in snake_List[:-1]:
                    # If a blockage is closer toward "Left", return either "Up", "Down", or "Right".
                    if [x1 - (snake_block * i), y1] == x:
                        # If already heading Up and Up isn't blocked, go Up.
                        if y1_change == -snake_block and not up_blocked:
                            return (0,-snake_block)
                        # If already heading Down and Down isn't blocked, go Down.
                        elif y1_change == snake_block and not down_blocked:
                            return (0, snake_block)
                        # Otherwise, return "Right".
                        elif not right_blocked:
                            return (snake_block,0)
            # If not, return Left.
            return (-snake_block,0)
    # Check if "Right" is not blocked and will move us closer.
    if not right_blocked and right_closer:
        # If the Snake is already moving Right, or hasn't moved at all yet, return "Right".
        if x1_change == snake_block or (x1_change==0 and y1_change==0):
            return (snake_block,0)
        # Determine whether or not moving closer to the Food will inadvertantly trap the Snake.
        else:
            for i in range(1, 7):
                for x in snake_List[:-1]:
                    # If a blockage is closer toward "Right", return either "Up", "Down", or "Left".
                    if [x1 + (snake_block * i), y1] == x:
                        # If already heading Up and Up isn't blocked, go Up.
                        if y1_change == -snake_block and not up_blocked:
                            return (0,-snake_block)
                        # If already heading Down and Down isn't blocked, go Down.
                        elif y1_change == snake_block and not down_blocked:
                            return (0, snake_block)
                        # Otherwise, return "Left".
                        elif not left_blocked:
                            return (-snake_block,0)
            # If not, return Right.
            return (snake_block,0)
    # If multiple directions will move us closer (and aren't blocked), choose the first one in the list
    if up_closer and not up_blocked:
        return (0,-snake_block)
    elif down_closer and not down_blocked:
        return (0,snake_block)
    elif left_closer and not left_blocked:
        return (-snake_block,0)
    elif right_closer and not right_blocked:
        return (snake_block,0)
    # If *no* direction will move us closer, turn the Snake in a direction that will enable it to move closer next turn.
    else:
        # If the Snake is currently moving Up or Down, determine whether turning Left or Right would be safer.
        if y1_change != 0:
            for i in range(1, int(dis_width/snake_block)):
                for x in snake_List[:-1]:
                    if [x1 - (snake_block * i), y1] == x: # or (x1-(snake_block * i) < 0):
                        return (snake_block,0)
                    if [x1 + (snake_block * i), y1] == x: # or (x1+(snake_block * i) > dis_width):
                        return (-snake_block,0)
            return (-snake_block,0)
        # If the Snake is currently moving Left or Right, determine whether turning Up or Down would be safer.
        elif x1_change != 0:
            for i in range(1, int(dis_height/snake_block)):
                for x in snake_List[:-1]:
                    if [x1, y1 - (snake_block * i)] == x: # or (y1-(snake_block * i) < 0):
                        return (0,snake_block)
                    if [x1, y1 + (snake_block * i)] == x: # or (x1-(snake_block * i) > dis_height):
                        return (0,-snake_block)
            return (0,-snake_block)
        # If the Snake cannot move in any direction, simply have it move forward and get a Game Over.
        elif up_blocked and down_blocked and left_blocked and right_blocked:
            return (x1_change,y1_change)

# Manage the loop to run the Game automatically
def gameLoopAuto():
    #Initialize the Game State Management variables
    game_over = False
    game_close = False

    # Initialize the Movement Variables
    x1 = dis_width/2
    y1 = dis_height/2
    x1_change = 0
    y1_change = 0

    # Retrieve the global Color variable
    global current_color

    # Initialize the Snake and Score (Score is used to measure Snake length)
    snake_List = []
    score = 0

    # Randomize Food placement
    foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
    food_placed = True

    # Set whether or not to automatically restart on Game Over
    global looping

    # Set whether or not to display the "Loop" and "Hide" Prompts
    global displayLoopText

    while not game_over:
        # Handle the Game Over/Restart state
        while game_close==True:
            # If the Game is meant to reset automatically, do so.
            if looping==True:
                gameLoopAuto()
            else:
                # Draw the current Game state
                dis.fill(black)
                pygame.draw.rect(dis, colors[current_color], [foodx,foody,snake_block,snake_block])
                draw_snake(snake_block, snake_List)
                message(str(score), dis_width - font_style.size(str(score))[0] - 4, 4)
                # Print the Game Over messages
                message(finalscore_text+str(score),(dis_width/2)-(font_style.size(finalscore_text+str(score))[0]/2), (dis_height/4))
                message(reset_text, (dis_width/2)-(font_style.size(reset_text)[0]/2), (dis_height/4) + font_style.size(reset_text)[1] + 16)
                message(quit_text, dis_width - font_style.size(quit_text)[0] - 8, dis_height - font_style.size(quit_text)[1] - 8)
                message(colors_text, 8, 8)
                message(stop_text, 8, dis_height - font_style.size(bored_text)[1] - 8)
                pygame.display.update()
                for event in pygame.event.get():
                # Quit if the "Close" Button is pressed
                    if event.type==pygame.QUIT:
                        game_over = True
                        game_close = False
                    if event.type==pygame.KEYDOWN:
                        # R: Reset the Game
                        if event.key==pygame.K_r:
                            gameLoopAuto()
                        # P: Stop playing the Game automatically
                        if event.key==pygame.K_p:
                            gameLoop()
                        # Esc: Quit the Game
                        if event.key==pygame.K_ESCAPE:
                            game_over = True
                            game_close = False
                        # 1-0: Change the display Color
                        if event.key==pygame.K_0 or event.key==pygame.K_KP0:
                            current_color = 0
                        if event.key==pygame.K_1 or event.key==pygame.K_KP1:
                            current_color = 1
                        if event.key==pygame.K_2 or event.key==pygame.K_KP2:
                            current_color = 2
                        if event.key==pygame.K_3 or event.key==pygame.K_KP3:
                            current_color = 3
                        if event.key==pygame.K_4 or event.key==pygame.K_KP4:
                            current_color = 4
                        if event.key==pygame.K_5 or event.key==pygame.K_KP5:
                            current_color = 5
                        if event.key==pygame.K_6 or event.key==pygame.K_KP6:
                            current_color = 6
                        if event.key==pygame.K_7 or event.key==pygame.K_KP7:
                            current_color = 7
                        if event.key==pygame.K_8 or event.key==pygame.K_KP8:
                            current_color = 8
                        if event.key==pygame.K_9 or event.key==pygame.K_KP9:
                            current_color = 9

        #Check for user input during Autoplay
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over = True
            if event.type==pygame.KEYDOWN:
                # ESC: Close the Game
                if event.key==pygame.K_ESCAPE:
                    game_over = True
                # L: Toggle the Autoplay looping
                if event.key==pygame.K_l:
                    looping = not looping
                # H: Toggle displaying text mid-game
                if event.key==pygame.K_h:
                    displayLoopText = not displayLoopText
                # 1-0: Change the display Color
                if event.key==pygame.K_0 or event.key==pygame.K_KP0:
                    current_color = 0
                if event.key==pygame.K_1 or event.key==pygame.K_KP1:
                    current_color = 1
                if event.key==pygame.K_2 or event.key==pygame.K_KP2:
                    current_color = 2
                if event.key==pygame.K_3 or event.key==pygame.K_KP3:
                    current_color = 3
                if event.key==pygame.K_4 or event.key==pygame.K_KP4:
                    current_color = 4
                if event.key==pygame.K_5 or event.key==pygame.K_KP5:
                    current_color = 5
                if event.key==pygame.K_6 or event.key==pygame.K_KP6:
                    current_color = 6
                if event.key==pygame.K_7 or event.key==pygame.K_KP7:
                    current_color = 7
                if event.key==pygame.K_8 or event.key==pygame.K_KP8:
                    current_color = 8
                if event.key==pygame.K_9 or event.key==pygame.K_KP9:
                    current_color = 9
        # If the Snake hits a wall, Game Over.
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        # Determine what direction to move the Snake in.
        (x1_change,y1_change) = chooseDirection(x1,y1,x1_change,y1_change,foodx,foody,snake_List)
        x1 += x1_change
        y1 += y1_change
        # Refresh the Window
        dis.fill(black)
        # Draw the Food
        pygame.draw.rect(dis, colors[current_color], [foodx,foody,snake_block,snake_block])
        # Add another block to the Snake
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        # Keep the Snake the appropriate length by removing the first element
        # The Snake is essentially drawn backward, relative to its array order and perceived movement direction
        if(len(snake_List) > score + 1):
            del snake_List[0]
        # If the Head of the Snake has collided with its Body anywhere, Game Over.
        for x in snake_List[:-1]:
            if x==snake_Head:
                game_close = True
        # Draw the Snake
        draw_snake(snake_block, snake_List)
        # Draw the Score
        message(str(score), dis_width - font_style.size(str(score))[0] - 4, 4)
        # If not being hidden, draw the "Loop" and "Hide" Prompts
        if displayLoopText==True:
            message(loop_text, 8, dis_height - font_style.size(loop_text)[1] - 8)
            message(hide_text, 24 + font_style.size(loop_text)[0], dis_height - font_style.size(hide_text)[1] - 8)
            # If looping, draw the notification Message
            if looping==True:
                message(looping_text, dis_width - font_style.size(looping_text)[0] - 8, dis_height - font_style.size(looping_text)[1] - 8)
        # Update the Window
        pygame.display.update()
        #If the Snake collides with the Food, increase the Score and Reset the Food
        if x1==foodx and y1==foody:
            score += 1
            foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            # Make sure the Food is not under any part of the Snake body.
            food_placed = False
            while not food_placed:
                food_placed = True
                for x in snake_List:
                    if x == [foodx, foody]:
                        food_placed = False
                        # print("Replacing Food...") # Use this to test how often the Food has to be moved.
                        foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
                        foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
        # Refresh "snake_speed" times per second (currently 12)
        clock.tick(snake_speed)

    # Uninitialize Everything
    pygame.quit()
    quit()

# Start running the Game
gameLoop()