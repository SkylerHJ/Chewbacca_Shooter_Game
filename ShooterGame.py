import pygame
from pygame.locals import *
from Player import *
from Laser import *
from Block import *
import random as rand

#screen setup
pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
pygame.key.set_repeat(100,100)

#creation of sprites and sprite groups
sprite_list = pygame.sprite.Group()
player = Player(20, 20)
sprite_list.add(player)
lasers = pygame.sprite.Group()
blocks = pygame.sprite.Group()

#creating of score keeper, fonts, and timer variables
score = 0
ariel_70 = pygame.font.SysFont('Ariel', 70)
ariel_20 = pygame.font.SysFont('Ariel', 20)
counter = 120
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event , 1000)
timer = ariel_20.render(str(counter), 1, (0, 0, 0))

#creation of block/enemy objects
for i in range(10):
        x = rand.randint(830, 1000)
        y = rand.randint(0, 570)
        block = Block(x, y)
        sprite_list.add(block)
        blocks.add(block)
    
end = True
while end:
#fill screen with white and display of direction for the game
    screen.fill((255, 255, 255))
    directions = ariel_20.render('Use the [UP] and [DOWN] keys to move and the [SPACEBAR] to shoot', 1, (0, 0, 0))
    screen.blit(directions, (200, 570))
    clock.tick(60)
    
#movement of all laser objects
    for l in lasers:
        l.rect.x += 2

#movement of all block objects and position reset when they move off screen
    for b in blocks:
        if b.rect.x <= -30:
            b.rect.x = rand.randint(830, 1000)
            b.rect.y = rand.randint(0, 570)
        b.rect.x -= 2
#key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type==KEYDOWN and event.key==K_ESCAPE):
            end = False
            pygame.quit()
        #movement of player sprite
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                player.move_down()
            if event.key == K_UP:
                player.move_up()
        #creation of laser object when [SPACEBAR] is pressed
            if event.key == pygame.K_SPACE:
                laser = Laser(player.get_x() + 70, player.get_y() + 27)
                lasers.add(laser)
                sprite_list.add(laser)
        #display of game timer
        if event.type == timer_event:
            counter -= 1
            timer = ariel_20.render('Timer: ' + str(counter), 1, (0, 0, 0))
            if counter == 0 and score < 50:
                end = False
                lose = ariel_70.render('You Lose', 1, (0, 0, 255))
                screen.blit(lose, (290, 250))
        screen.blit(timer, (720, 5))

#collision between block and laser sprites
    points = pygame.sprite.groupcollide(lasers, blocks, True, True)
    #will create new block after old one has been 'destroyed' and add 5 points to score
    for point in points:
        x = rand.randint(830, 1000)
        y = rand.randint(0, 570)
        block = Block(x, y)
        sprite_list.add(block)
        blocks.add(block)
        score += 5
#print of score on screen
    scoring = ariel_20.render('Score: ' + str(score), 1, (0, 0, 0))
    screen.blit(scoring, (720, 20))

#player and block sprite collision will show 'game over'
    if pygame.sprite.spritecollideany(player, blocks):
        end = False
        text = ariel_70.render('Game Over', 1, (0, 0, 255))
        screen.blit(text, (290, 250))

#if score is 50 or above displays 'you win'
    if score >= 50:
        end = False
        win = ariel_70.render('You Win', 1, (0, 0, 255))
        screen.blit(win, (290, 250))

#update of sprites and screen
    sprite_list.update()
    sprite_list.draw(screen)
    lasers.update()
    lasers.draw(screen)
    blocks.update()
    blocks.draw(screen)
    pygame.display.update()
