########################################################

# Bounce 1.0 Copyright (C) RVJ Callanan 2012
#
# This is FREE software, licensed under the GNU GPLv3
# See: <http://www.gnu.org/licenses/>.
#
########################################################

########################################################
# IMPORTS
########################################################

import pygame

########################################################
# FUNCTIONS
########################################################

def BallRect():

    # Returns rect corresponding to the ball's current
    # state with values rounded to the nearest integer

    b_pos = round(cur_px), round(cur_py)
    
    return pygame.Rect(b_pos, b_size)

########################################################

def InitParams():

    # Initialise tunable parameters. 
    # This is where you experiment!
    # These are crude representations.
    # Units reflect screen time/space.

     global gravity         # adjusted for screen units 
     global throw_vel       # initial horizontal velocity
     global bounce_factor   # simulates energy loss
     global bounce_min      # prevent endless bouncing
     global roll_factor     # simulates friction
     
     gravity        = 2.0
     throw_vel      = 1.5
     bounce_factor  = 0.75
     bounce_min     = 0.5
     roll_factor    = 0.98

########################################################

def ResetBall():
    
    # Returns ball to ready/start position

    global cur_pos, cur_px, cur_py
    global cur_vel, cur_vx, cur_vy
    global cur_acc, cur_ax, cur_ay
    global cur_vol
    global cur_rec

    InitParams()

    # some state variables are redundant for now
    # can be used later to simulate air resistance
    # ball has slight left-to-right momentum (cur_vx)
    # gravity is key parameter in vertical direction (cur_ay)

    cur_pos = cur_px, cur_py = 20.0, 10.0       # position
    cur_vel = cur_vx, cur_vy = throw_vel, 0.0   # velocity
    cur_acc = cur_ax, cur_ay = 0.0, gravity     # acceleration
    cur_vol = 0.0                               # sound
    cur_rec = BallRect()                        # rectangular area

########################################################

def StartUp():

    global screen, s_size, s_width, s_height
    global ball, b_size, b_width, b_height
    global max_py, max_vy
    global sound
    global fps, tick, clock
    global cur_pos, cur_px, cur_py
    global cur_vel, cur_vx, cur_vy
    global cur_acc, cur_ax, cur_ay
    global cur_vol
    global cur_rec

    InitParams()

    # Initialise screen

    pygame.init()

    pygame.display.set_caption("Bounce Simulator 1.0")
    s_size = s_width, s_height = 400, 400
    screen = pygame.display.set_mode(s_size)

    # Initialise ball image

    ball = pygame.image.load('ball.png').convert_alpha()
    b_size = b_width, b_height = ball.get_size()

    # Initialise max values

    max_py = float(s_height - b_height)
    max_vy = 0

    # Re-initialise sound system with only
    # bare buffer size to reduce sound lag

    pygame.mixer.quit()
    pygame.mixer.init(buffer=8)

    # Initialise sound samples
    
    sound = pygame.mixer.Sound("bounce.wav")

    # Setup frame rate and throttle clock

    fps = 50                        # Frames Per Second
    tick = 1000/fps                 # Frame clock tick period in mS
    clock = pygame.time.Clock()     # Maintains frame time accuracy

    ResetBall()

    # Respond only to QUIT events

    pygame.event.set_allowed(pygame.QUIT)
    pygame.event.clear

########################################################

def ShutDown():

    pygame.quit()

########################################################

def MainLoop():

    global cur_pos, cur_px, cur_py
    
    while True:

        # Give Pygame a chance to respond to system events
        # such as window minimise, maximise and drag

        pygame.event.pump()

        # Always check if user is trying to close window
        # It's irritating when responsiveness is slow
       
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
             break

        # With events handled, poll keyboard

        keys = pygame.key.get_pressed()

        # If ball is completely at rest, do nothing
        # until user hits space bar to re-drop ball

        if cur_py == max_py and cur_vy == 0.0:
            pygame.display.set_caption("Hit SPACE to drop ball again")
            if keys[pygame.K_SPACE]:
                pygame.display.set_caption("Bouncing...")
                screen.fill((0,0,0))
                pygame.display.update()
                ResetBall()
  
        # Calculate ball dynamics for current frame
        # using our simple physics engine

        PhysicsEngine()

        # Update ball sound first as there is a slight
        # lag before sound is heard. If sounds from
        # previous bounces are still playing, more than
        # one sound channel will become active. This
        # means that lingering "echos" from previous
        # bounces will still be heard as the sound for
        # a new bounce is generated. This is realistic
        # when bounces start coming closer together and
        # the ball gradually "dribbles" to a halt.
        
        if cur_vol > 0:
            if cur_vol != prv_vol:
                sound.set_volume(cur_vol)
                sound.play()

        # Create dirty rects list for partial display updates
        # Do not update display if ball position is unchanged

        if cur_rec == prv_rec:
            dirty = []
        else:
            dirty = [prv_rec, cur_rec]

        # Repaint screen area around previous ball position
        # And then re-position ball at new screen position
        # This is more efficient than repainting whole screen

        if len(dirty) > 0:
            screen.fill((0,0,0), prv_rec)    
            screen.blit(ball, cur_rec)

        # Now update screen image to the actual display.
        # For efficiency, only update "dirty" screen areas
        # i.e. areas previously and currently occupied by ball. 
        # Before updating display, throttle main loop using
        # the special Pygame clock.tick() function. This slows
        # down the program to maintain an accurate frame rate.
        # It also frees up the CPU for other processes. If your
        # program does not behave like a good citizen, the OS
        # will slow it down anyway, but in unpredictable ways.
        # The smoothest animation is achieved by performing
        # display update right after clock.tick() returns
        
        clock.tick(fps)
        if len(dirty) > 0:
            pygame.display.update(dirty)

    #endwhile
    
########################################################

def PhysicsEngine():

    global cur_pos, cur_px, cur_py
    global prv_pos, prv_px, prv_py
    
    global cur_vel, cur_vx, cur_vy
    global prv_vel, prv_vx, prv_vy
    
    global cur_acc, cur_ax, cur_ay
    global prv_acc, prv_ax, prv_ay
    
    global cur_vol
    global prv_vol
    
    global cur_rec
    global prv_rec

    global max_py, max_vy

    # Copy current to previous state variables

    prv_pos = prv_px, prv_py = cur_pos
    prv_vel = prv_vx, prv_vy = cur_vel     
    prv_acc = prv_ax, prv_ay = cur_acc
    prv_vol = cur_vol
    prv_rec = cur_rec

    # Assume no sound unless bounce detected

    cur_vol = 0.0

    # Calculate velocity

    cur_vy = prv_vy + cur_ay
    max_vy = max(max_vy,cur_vy)
            
    # Calculate position

    cur_px = prv_px + cur_vx
    cur_py = prv_py + cur_vy

    # Detect and handle bounce

    if cur_py > max_py:

        # Bounce volume depends on velocity

        cur_vol = cur_vy / max_vy

        # Bounce reverses position and velocity

        dif_py = cur_py - max_py
        cur_py = max_py - bounce_factor * dif_py
        cur_vy = - bounce_factor * cur_vy

    # At some point, bring ball to complete vertical rest
    # Otherwise it ends with residual bounce oscillation

    if abs(max_py - cur_py) < bounce_min and abs(cur_py - prv_py) < bounce_min:
        
        cur_py = max_py
        cur_vy = 0.0
        cur_ay = 0.0

        # With ball rolling horizontally, add friction
        # which eventually overcomes residual momentum

        cur_vx = cur_vx * roll_factor  

        if cur_vx < 0.01:
            cur_vx = 0.0
            cur_ax = 0.0
        #endif

    #endif
        
    # Update remaining variables for current state

    cur_pos = cur_px, cur_py
    cur_vel = cur_vx, cur_vy
    cur_acc = cur_ax, cur_ay
    cur_rec = BallRect()

########################################################
# START OF PROGRAM
########################################################

StartUp()
MainLoop()
ShutDown()

########################################################
# END OF PROGRAM
########################################################
        
    
