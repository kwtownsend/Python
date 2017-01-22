"""
Game By Kndall Townsend
CWID: 894121409
Based off the game Binding of Isaac
"""
import pygame, random, os, enemyclass, playerclass, powerupclass, barrierclass, bulletclass
from pygame.locals import *



# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIME = (0, 255, 0)
red = (200,0,0)
PINK = (255, 102, 255)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
white = (255, 255, 255)

# --- Create the window


# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 450
screen = pygame.display.set_mode([screen_width, screen_height])
font1 = pygame.font.Font(os.path.join("Times_New_Roman_Normal.ttf"),24)




clock = pygame.time.Clock()


def message_display(text):
    largeText = pygame.font.Font(os.path.join("Times_New_Roman_Normal.ttf"),115)

    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((screen_width/2),(screen_height/2))
    screen.blit(TextSurf, TextRect)
 
    pygame.display.update()
 
    time.sleep(2)
 
    game_loop()
    
def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    textSurf, textRect = text_objects(msg, font1)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)
    
def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(white)
        largeText = pygame.font.SysFont("Times_New_Roman_Normal.ttf",72)
        TextSurf, TextRect = text_objects("Death by Square", largeText)
        TextRect.center = ((screen_width/2+30),(screen_height/2-100))
        author = font1.render("By: Kendall Townsend",True,(0,0,0))        

        screen.blit(author, (250, 300))        
        screen.blit(TextSurf, TextRect)

        button("Start",150,200,100,50,green,bright_green,game_loop)
        button("Quit",500,200,100,50,red,bright_red,quitgame)
        button("Instructions", 300, 200, 150, 50, green, bright_green, instructions_page)

        pygame.display.update()
        clock.tick(15)

def instructions_page():
    intro = False
    instructions = True

    while instructions:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        instructions = font1.render("How to Play:",True,(0,0,0))        
        instructions1 = font1.render("Use arrow keys to move, and W, A, S, D to shoot projectile.",True,(0,0,0))
        instructions2 = font1.render("Hold down spacebar for continuous fire.",True,(0,0,0))        
        instructions3 = font1.render("The goal of the game is to eliminate all enemy squares.",True,(0,0,0))
        instructions4 = font1.render("Enemy squares drop green powerups that increase your speed.",True,(0,0,0))
        instructions5 = font1.render("Enemy squares drop pink powerups that increase your rate of fire.",True,(0,0,0))
        instructions6 = font1.render("Clear all enemy to go to next level..",True,(0,0,0))
        
        
        screen.fill(white)

        screen.blit(instructions, (15, 0))        
        screen.blit(instructions1, (15, 30))
        screen.blit(instructions2, (15, 60))
        screen.blit(instructions3, (15, 90))
        screen.blit(instructions4, (15, 120))
        screen.blit(instructions5, (15, 150))
        screen.blit(instructions6, (15, 180))


        button("Back", 500, 300, 100, 50, green, bright_green, game_intro)

        pygame.display.update()
        clock.tick(15)


def quitgame():
    pygame.display.quit()


 
# --- Sprite lists


def game_loop():

    #modifiable variables that can't be in a class
    score = 0  
    enemyshootdelay = 1000
    speed = 1
    level = 1    
    gameover = False
    timepassed = pygame.time.get_ticks()
    playerpassed = pygame.time.get_ticks()
    
    
    # This is a list of every sprite. All blocks and the player block as well.
    all_sprites_list = pygame.sprite.Group()
     
    # List of each block in the game
    block_list = pygame.sprite.Group()
    barrier_list = pygame.sprite.Group()
    player_list = pygame.sprite.Group()


    #list of powerups
    powerup_speed_list = pygame.sprite.Group()
    powerup_rateoffire_list = pygame.sprite.Group()
    
    # List of each bullet
    bullet_list = pygame.sprite.Group()
    enemy_bullet_list = pygame.sprite.Group()


    # --- Create the sprites
     
    for i in range(level):
        # This represents a block
        block = enemyclass.Block(BLUE)
        # Set a random location for the block
        block.rect.x = random.randint(100,600)
        block.rect.y = random.randint(100,300)
     
        # Add the block to the list of objects
        block_list.add(block)
        all_sprites_list.add(block)


    #random barriers horizontal to encourage movement of ai
    incrementy = 50
    for i in range(13):
        # This represents a block
        barrier = barrierclass.HorizontalBarrier(BLACK)
        # Set a random location for the block
        incrementy += random.randint(30, 75)
        if incrementy < 325:
            barrier.rect.x = 0
            barrier.rect.y = incrementy
            # Add the block to the list of objects
            barrier_list.add(barrier)
            all_sprites_list.add(barrier)
            
    incrementy = 50
    for i in range(13):
        # This represents a block
        barrier = barrierclass.HorizontalBarrier(BLACK)
        # Set a random location for the block
        incrementy += random.randint(30, 75)
        if incrementy < 325:
            barrier.rect.x = 650
            barrier.rect.y = incrementy
            # Add the block to the list of objects
            barrier_list.add(barrier)
            all_sprites_list.add(barrier)

        
    #random barriers vertical to encourage movement of ai
    incrementx = 50
    for i in range(13):
        # This represents a block
        barrier = barrierclass.VerticalBarrier(BLACK)
        # Set a random location for the block
        incrementx += random.randint(30, 75)
        if incrementx < 625: 
            barrier.rect.x = incrementx
            barrier.rect.y = 0     
            # Add the block to the list of objects
            barrier_list.add(barrier)
            all_sprites_list.add(barrier)

    incrementx = 50    
    for i in range(13):
        # This represents a block
        barrier = barrierclass.VerticalBarrier(BLACK)
        # Set a random location for the block
        incrementx += random.randint(30, 75)        
        if incrementx < 625:
            barrier.rect.x = incrementx
            barrier.rect.y = screen_height - 100
            # Add the block to the list of objects
            barrier_list.add(barrier)
            all_sprites_list.add(barrier)
        
    #create middle borders
    barrierx = 200
    barriery = 200
    # This represents a block
    barrier = barrierclass.CenterHorizontalBarrier(BLACK)
    # Set a random location for the block
    barrier.rect.x = barrierx
    barrier.rect.y = barriery
    # Add the block to the list of objects
    barrier_list.add(barrier)
    all_sprites_list.add(barrier)

    barrierx = 350
    barriery = 100
    # This represents a block
    barrier = barrierclass.CenterVerticalBarrier(BLACK)
    # Set a random location for the block
    barrier.rect.x = barrierx
    barrier.rect.y = barriery
    # Add the block to the list of objects
    barrier_list.add(barrier)
    all_sprites_list.add(barrier)


    #create borders
    barrierx = 0
    barriery = 0
    # This represents a block
    barrier = barrierclass.LeftRightBorder(BLACK)
    # Set a random location for the block
    barrier.rect.x = barrierx
    barrier.rect.y = barriery
    # Add the block to the list of objects
    barrier_list.add(barrier)
    all_sprites_list.add(barrier)
        
    barrierx = 700
    barriery = 0
    # This represents a block
    barrier = barrierclass.LeftRightBorder(BLACK)
    # Set a random location for the block
    barrier.rect.x = barrierx
    barrier.rect.y = barriery
    # Add the block to the list of objects
    barrier_list.add(barrier)
    all_sprites_list.add(barrier)

    barrierx = 0
    barriery = 0
    # This represents a block
    barrier = barrierclass.TopBotBorder(BLACK)
    # Set a random location for the block
    barrier.rect.x = barrierx
    barrier.rect.y = barriery
    # Add the block to the list of objects
    barrier_list.add(barrier)
    all_sprites_list.add(barrier)

    barrierx = 0
    barriery = 400
    # This represents a block
    barrier = barrierclass.TopBotBorder(BLACK)
    # Set a random location for the block
    barrier.rect.x = barrierx
    barrier.rect.y = barriery
    # Add the block to the list of objects
    barrier_list.add(barrier)
    all_sprites_list.add(barrier)

    # Create a red player block
    player = playerclass.Player()
    all_sprites_list.add(player)
    player_list.add(player)
     
    # Loop until the user clicks the close button.
    done = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
     
    player.rect.y = 370
    player.rect.x = 50

    spacebar = False
    
    # -------- Main Program Loop -----------
    while not done:



                    
        # --- Game logic
        
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 done = True        
            elif(done == False):
                playkey = pygame.key.get_pressed()
                if playkey[pygame.K_w]:
                    player.upshoot = True
                    player.downshoot = False
                    player.leftshoot = False
                    player.rightshoot = False

                elif playkey[pygame.K_s]:
                    player.downshoot = True
                    player.upshoot = False
                    player.leftshoot = False
                    player.rightshoot = False
                    
                elif playkey[pygame.K_a]:
                    player.leftshoot = True
                    player.downshoot = False
                    player.upshoot = False
                    player.rightshoot = False
                    
                elif playkey[pygame.K_d]:
                    player.rightshoot = True
                    player.downshoot = False
                    player.leftshoot = False
                    player.upshoot = False
                if event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        spacebar = True
                if event.type == pygame.KEYUP:
                    if event.key == K_SPACE:
                        spacebar = False
                        
               #fire when you click on w, a, s, d
                now = pygame.time.get_ticks()   
                if(now - playerpassed > player.shootdelay and gameover == False):
                    playerpassed = pygame.time.get_ticks()
                    starttime = pygame.time.get_ticks()                   
                    if player.upshoot == True:
                        # Fire a bullet if the user clicks the mouse button
                        bullet = bulletclass.BulletUp()
                        # Set the bullet so it is where the player is
                        bullet.rect.x = player.rect.x+8
                        bullet.rect.y = player.rect.y+8
                        # Add the bullet to the lists
                        all_sprites_list.add(bullet)
                        bullet_list.add(bullet)
                    if player.downshoot == True:
                        # Fire a bullet if the user clicks the mouse button
                        bullet = bulletclass.BulletDown()
                        # Set the bullet so it is where the player is
                        bullet.rect.x = player.rect.x+8
                        bullet.rect.y = player.rect.y+8
                        # Add the bullet to the lists
                        all_sprites_list.add(bullet)
                        bullet_list.add(bullet)
                    if player.leftshoot == True:
                        # Fire a bullet if the user clicks the mouse button
                        bullet = bulletclass.BulletLeft()
                        # Set the bullet so it is where the player is
                        bullet.rect.x = player.rect.x+8
                        bullet.rect.y = player.rect.y+8
                        # Add the bullet to the lists
                        all_sprites_list.add(bullet)
                        bullet_list.add(bullet)
                    if player.rightshoot == True:
                        # Fire a bullet if the user clicks the mouse button
                        bullet = bulletclass.BulletRight()
                        # Set the bullet so it is where the player is
                        bullet.rect.x = player.rect.x+8
                        bullet.rect.y = player.rect.y+8
                        # Add the bullet to the lists
                        all_sprites_list.add(bullet)
                        bullet_list.add(bullet)
                    
        #turn on continuous fire when holding spacebar            
        now = pygame.time.get_ticks()   
        if(now - playerpassed > player.shootdelay and gameover == False):
            playerpassed = pygame.time.get_ticks()
            starttime = pygame.time.get_ticks()                   
            if player.upshoot == True and spacebar == True:
                # Fire a bullet if the user clicks the mouse button
                bullet = bulletclass.BulletUp()
                # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x+8
                bullet.rect.y = player.rect.y+8
                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
            if player.downshoot == True and spacebar == True:
                # Fire a bullet if the user clicks the mouse button
                bullet = bulletclass.BulletDown()
                # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x+8
                bullet.rect.y = player.rect.y+8
                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
            if player.leftshoot == True and spacebar == True:
                # Fire a bullet if the user clicks the mouse button
                bullet = bulletclass.BulletLeft()
                # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x+8
                bullet.rect.y = player.rect.y+8
                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
            if player.rightshoot == True and spacebar == True:
                # Fire a bullet if the user clicks the mouse button
                bullet = bulletclass.BulletRight()
                # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x+8
                bullet.rect.y = player.rect.y+8
                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet) 
                        
        #enemy bullet rng
        now = pygame.time.get_ticks()
        if (now - timepassed > enemyshootdelay) and level >=5:
            timepassed = pygame.time.get_ticks()
            for block in block_list:
                rngshot = random.randint(0,3)
                if rngshot == 0:
                    bullet = bulletclass.EnemyBulletRight()
                elif rngshot == 1:
                    bullet = bulletclass.EnemyBulletLeft()
                elif rngshot == 2:
                    bullet = bulletclass.EnemyBulletUp()
                elif rngshot == 3:
                    bullet = bulletclass.EnemyBulletDown()    

                # Set the bullet so it is where the player is
                bullet.rect.x = block.rect.x+8
                bullet.rect.y = block.rect.y+8
                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                enemy_bullet_list.add(bullet)                

        #WHAT HAPPENS WHEN LEVEL IS CLEARED
        if not block_list:
            print("List is empty")
            level += 1
            for i in range(level):
                # This represents a block
                block = enemyclass.Block(BLUE)
                # Set a random location for the block
                block.rect.x = random.randint(100,600)
                block.rect.y = random.randint(100,300)

                if block.speedmultiplier < 3 and level % 5 == 0:
                    block.speedmultiplier += 1
                    print("enemy got faster")
                # Add the block to the list of objects
                block_list.add(block)
                all_sprites_list.add(block)

            player.rect.y = 370
            player.rect.x = 50

            #remove all bullets
            for bullet in bullet_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
            for bullet in enemy_bullet_list:
                enemy_bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)




                    
        # Call the update() method on all the sprites
        all_sprites_list.update()
     
        # Calculate mechanics for each bullet
        for bullet in bullet_list:
            # See if it hit a block
            block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
     
            # For each block hit, remove the bullet and add to the score
            for block in block_hit_list:
                #10% chance to drop powerup
                powerupdrop = random.randint(0,9)
                if powerupdrop <= 0:
                    #create powerup
                    powerup = powerupclass.Powerup(PINK)
                    powerup.rect.x = block.rect.x
                    powerup.rect.y = block.rect.y
                    powerup_rateoffire_list.add(powerup)
                    all_sprites_list.add(powerup)


                powerupdrop = random.randint(0,9)
                if powerupdrop <= 1:
                    #create powerup
                    powerup = powerupclass.Powerup(LIME)
                    powerup.rect.x = block.rect.x
                    powerup.rect.y = block.rect.y
                    powerup_speed_list.add(powerup)
                    all_sprites_list.add(powerup)

                    
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                block_list.remove(block)
                all_sprites_list.remove(block)
                score += 1
                print(score)
                
        
        # Calculate mechanics for each enemy bullet and if it kills player
        for bullet in enemy_bullet_list:
            # See if it hit a block
            player_hit_list = pygame.sprite.spritecollide(bullet, player_list, True)
            for player in player_hit_list:
                # when play gets hit
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                print("game over")
                gameover = True

                # Remove the bullet if it flies up off the screen
                if bullet.rect.y < -10:
                    bullet_list.remove(bullet)
                    all_sprites_list.remove(bullet)


        #Kill player if they are hit by enemy block
        for player in player_list:
            player_hit_list = pygame.sprite.spritecollide(block, player_list, True)
            for player in player_hit_list:
                player_list.remove(player)
                all_sprites_list.remove(player)
                gameover = True

                
                
        #if bullet hit barrier remove them
        for barrier in barrier_list:
            # See if it hit a barrier
            bullet_hit_list = pygame.sprite.spritecollide(barrier, bullet_list, True)
     
            # For each barrier hit, remove the bullet
            for bullet in bullet_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)

        #if enemy bullets hit barrier remove them
        for barrier in barrier_list:
            # See if it hit a barrier
            bullet_hit_list = pygame.sprite.spritecollide(barrier, enemy_bullet_list, True)
     
            # For each barrier hit, remove the bullet
            for bullet in bullet_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)

                
        #AI for blocks that has collision detection and goes in random directions
        # See if it hit a block               
        for block in block_list:
            block.rect.x += block.x_speed * block.speedmultiplier
            barriers_hit = pygame.sprite.spritecollide(block, barrier_list, False)
            for barrier in barriers_hit:
                if block.x_speed > 0:
                    block.rect.right = barrier.rect.left
                    temp = random.randint(0,2)
                    if temp == 0:
                        block.x_speed = 0
                        block.y_speed = 1 * block.speedmultiplier
                    if temp == 1:
                        block.x_speed = -1 * block.speedmultiplier
                        block.y_speed = 0
                    else:
                        block.x_speed = 0
                        block.y_speed = -1 * block.speedmultiplier
                else:
                    block.rect.left = barrier.rect.right
                    temp = random.randint(0,2)
                    if temp == 0:
                        block.x_speed = 0
                        block.y_speed = 1 * block.speedmultiplier
                    if temp == 1:
                        block.x_speed = 1 * block.speedmultiplier
                        block.y_speed = 0    
                    else:
                        block.x_speed = 0
                        block.y_speed = -1 * block.speedmultiplier
                        
            block.rect.y += block.y_speed * block.speedmultiplier
            barriers_hit = pygame.sprite.spritecollide(block, barrier_list, False)
            for barrier in barriers_hit:
                if block.y_speed > 0:
                    block.rect.bottom = barrier.rect.top
                    temp = random.randint(0,2)
                    if temp == 0:
                        block.x_speed = 1 * block.speedmultiplier
                        block.y_speed = 0
                    if temp == 1:
                        block.x_speed = 0
                        block.y_speed = -1 * block.speedmultiplier
                    else:
                        block.x_speed = -1 * block.speedmultiplier
                        block.y_speed = 0
                else:
                    block.rect.top = barrier.rect.bottom
                    temp = random.randint(0,2)
                    if temp == 0:
                        block.x_speed = 1 * block.speedmultiplier
                        block.y_speed = 0
                    if temp == 1:
                        block.x_speed = 0
                        block.y_speed = 1 * block.speedmultiplier
                    else:
                        block.x_speed = -1 * block.speedmultiplier
                        block.y_speed = 0            
                
                    

        # Move the player if an arrow key is pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.x_speed = -1 * player.speed
            player.y_speed = 0
        if key[pygame.K_RIGHT]:
            player.x_speed = 1 * player.speed
            player.y_speed = 0
        if key[pygame.K_UP]:
            player.y_speed = -1 * player.speed
            player.x_speed = 0
        if key[pygame.K_DOWN]:
            player.y_speed = 1 * player.speed
            player.x_speed = 0


        # Move each axis separately. Note that this checks for collisions both times.
        if player.x_speed != 0:
            # Move the rect
            player.rect.x += player.x_speed
            player.rect.y += 0
            player_collision = pygame.sprite.spritecollide(player, barrier_list, False)
            # If you collide with a wall, move out based on velocity
            for barrier in player_collision:
                if player.x_speed > 0: # Moving right; Hit the left side of the wall
                    player.rect.right = barrier.rect.left
                    player.x_speed = 0
                if player.x_speed < 0: # Moving left; Hit the right side of the wall
                    player.rect.left = barrier.rect.right
                    player.x_speed = 0
          
        if player.y_speed != 0:
            # If you collide with a wall, move out based on velocity
            player.rect.x += 0
            player.rect.y += player.y_speed
            player_collision = pygame.sprite.spritecollide(player, barrier_list, False)
            for barrier in player_collision:
                if player.y_speed > 0: # Moving down; Hit the top side of the wall
                    player.rect.bottom = barrier.rect.top
                    player.y_speed = 0
                if player.y_speed < 0: # Moving up; Hit the bottom side of the wall
                    player.rect.top = barrier.rect.bottom
                    player.y_speed = 0


            
        
        # See if the player block has collided with powerups.
        for powerup in powerup_speed_list:
            powerups_hit_list = pygame.sprite.spritecollide(player, powerup_speed_list, True)
            for powerup in powerups_hit_list:
                powerup_speed_list.remove(powerup)
                all_sprites_list.remove(powerup)
                #increase player speed cap at 15
                if player.speed <= 5:
                    player.speed += 1

        for powerup in powerup_rateoffire_list:
            powerups_hit_list = pygame.sprite.spritecollide(player, powerup_rateoffire_list, True)
            for powerup in powerups_hit_list:
                powerup_rateoffire_list.remove(powerup)
                all_sprites_list.remove(powerup)
                #increase player speed cap at 15
                if player.shootdelay > 500:
                    player.shootdelay = player.shootdelay - 250
                if player.shootdelay <= 500 and player.shootdelay > 250:
                    player.shootdelay = player.shootdelay - 50
                if player.shootdelay <= 250 and player.shootdelay > 50:
                    player.shootdelay = player.shootdelay - 25
                if player.shootdelay <= 50:
                    player.shootdelay = player.shootdelay / 2

                    
        # Clear the screen
        screen.fill(WHITE)
     
        # Draw all the spites
        all_sprites_list.draw(screen)

        #draw all displays
        displaylevel = font1.render("Level %d" %level,True,(0,0,0))
        screen.blit(displaylevel, (25, 400))

        displayscore = font1.render("Score: %d" %score,True,(0,0,0))
        screen.blit(displayscore, (135, 400))
        
        if player.speed < 5:
            displayspeed = font1.render("Speed: %d" %player.speed,True,(0,0,0))
        else:
            displayspeed = font1.render("Speed: MAX",True,(0,0,0))

        screen.blit(displayspeed, (245, 400))
        
       
        displayrateoffire = font1.render("Rate of Fire: %d ms" %player.shootdelay,True,(0,0,0))

        screen.blit(displayrateoffire, (355, 400))
        

        button("Quit",600,400,100,49,red,bright_red,quitgame)
        if gameover == True:
            button("Restart?",(screen_width/2 - 50),(screen_height/2- 50),100,49,red,bright_red,game_loop)
        
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 20 frames per second
        clock.tick(60)
game_intro()
game_loop()
pygame.quit()
