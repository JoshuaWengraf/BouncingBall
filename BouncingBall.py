import pygame
import os

lightblue = (0, 255, 255)  
lightgrey = (128,128,128)

image_path = os.path.dirname(__file__) # Where the .py file is located

timeLimit = 15000 # time in milliseconds

def main():
    pygame.init()      

    y = 500
    v = 0 # initial speed
    g = 0.00015 # gravitational constant
    t = 0      

    screen = pygame.display.set_mode((640,480))
    smileyface = pygame.image.load(os.path.join(image_path, 'ball.png')) # The image folder pathball.png')
    
    ctr = 0
    playing = True
    while playing:
        event = pygame.event.poll()    
        if event.type == pygame.QUIT:  
            break                   

        v = v - g*t
        y = y + v*t - g*t*t/2
        
        y_corrected = 480 - y
        if y < 400:
            v = v*-1
    
        screen.fill(lightblue)
        screen.blit(smileyface, (140, int(y_corrected)))

        width = 0.8 * y + 100
        
        pygame.draw.ellipse(screen, lightgrey, (200,400,int(width),20))
        t = t + 0.01

        framesPerSecond = 50
        timeBetweenFrames = 1000/framesPerSecond # (in milliseconds)
        timeElapsed = pygame.time.get_ticks() # (in milliseconds)
        if timeElapsed % timeBetweenFrames == 0:
            pygame.image.save(screen, os.path.join(image_path, 'BouncingBall' + str(ctr) + '.png'))
            print(ctr)
            ctr = ctr + 1

        if timeElapsed > timeLimit:
            pygame.quit()
            break

        pygame.display.flip()

main()
