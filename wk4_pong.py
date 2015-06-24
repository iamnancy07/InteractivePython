# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
frame_width = 600
frame_height = 400       
ball_radius = 20
ball_line_width = 1
pad_width = 8
pad_height = 80
half_pad_width = pad_width / 2
half_pad_height = pad_height / 2

text_font = 80
 


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_pos = [frame_width / 2, frame_height / 2] 

    ball_vel = [random.randrange(120, 240)/60, - random.randrange(60, 180)/60]
    
    if direction != 'right':
        ball_vel[0] = -ball_vel[0]
        
        
        

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    
    paddle1_pos = [half_pad_width, frame_height / 2]
    paddle2_pos = [frame_width - half_pad_width, frame_height / 2]
    
    paddle1_vel = 0
    paddle2_vel = 0
    
    spawn_ball('right')

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([frame_width / 2, 0],[frame_width / 2, frame_height], 1, "White")
    canvas.draw_line([pad_width, 0],[pad_width, frame_height], 1, "White")
    canvas.draw_line([frame_width - pad_width, 0],[frame_width - pad_width, frame_height], 1, "White")
        
    # update ball

    

            
    

    # draw ball
    
    canvas.draw_circle(ball_pos, ball_radius, ball_line_width, 'white', 'white')
  
    # update paddle's vertical position, keep paddle on the screen
    
    if paddle1_pos[1] + paddle1_vel >= half_pad_height and paddle1_pos[1] + paddle1_vel <= frame_height - half_pad_height:
        
        paddle1_pos[1] += paddle1_vel
    
    else:
        paddle1_vel = 0
        
    if paddle2_pos[1] + paddle2_vel >= half_pad_height and paddle2_pos[1] + paddle2_vel <= frame_height - half_pad_height:
      
        paddle2_pos[1] += paddle2_vel
    else:
        paddle2_vel = 0
 
    # draw paddles
    
    canvas.draw_polygon([[0, paddle1_pos[1] - half_pad_height], [pad_width, paddle1_pos[1] - half_pad_height], [pad_width, paddle1_pos[1] + half_pad_height],[0, paddle1_pos[1] + half_pad_height]], 1, 'red','red')
    canvas.draw_polygon([[frame_width - pad_width, paddle2_pos[1] - half_pad_height], [frame_width, paddle2_pos[1] - half_pad_height], [frame_width, paddle2_pos[1] + half_pad_height],[frame_width - pad_width, paddle2_pos[1] + half_pad_height]], 1, 'red','red')
    
    # determine whether paddle and ball collide    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[1] == ball_radius or ball_pos[1] == frame_height - ball_radius:
        
        ball_vel[1] = -ball_vel[1]
        
    if ball_pos[0] <= pad_width + ball_radius:
    
        if ball_pos[1] >= paddle1_pos[1] - half_pad_height and ball_pos[1] <= paddle1_pos[1] + half_pad_height:
        
            ball_vel[0] = -ball_vel[0]*1.1
        else: 
            score2 += 1
            spawn_ball('right')
          
    if ball_pos[0] >= frame_width - (pad_width + ball_radius):
        
        if ball_pos[1] >= paddle2_pos[1] - half_pad_height and ball_pos[1] <= paddle2_pos[1] + half_pad_height:
        
            ball_vel[0] = -ball_vel[0]*1.1    
    
        else:
            score1 += 1
            spawn_ball('left')
    
    score = str(score1) + ' / ' + str(score2)    

    # draw scores
    canvas.draw_text(score, [frame_width / 2 - text_font, text_font + 10], text_font, 'green')
       
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    acc = 1 
    
    if key == simplegui.KEY_MAP['down']:
        
        if paddle2_vel <0:
            
            paddle2_vel = 0
            paddle2_vel += acc
        else:
            paddle2_vel += acc
    
    if key == simplegui.KEY_MAP['s']:
        
        if paddle1_vel <0:
            
            paddle1_vel = 0
            paddle1_vel += acc
        else:
            paddle1_vel += acc
    
   
def keyup(key):
    global paddle1_vel, paddle2_vel

    acc = 1 

    if key == simplegui.KEY_MAP['up']:
        
        if paddle2_vel >0:
            
            paddle2_vel = 0
            paddle2_vel -= acc
        else:
            paddle2_vel -= acc
    
    if key == simplegui.KEY_MAP['w']:
        
        if paddle1_vel >0:
            
            paddle1_vel = 0
            paddle1_vel -= acc
        else:
            paddle1_vel -= acc
    
def reset_handler(): 
        
    new_game()
    
# create frame
frame = simplegui.create_frame("Pong", frame_width, frame_height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Reset', reset_handler, 100)


# start frame
new_game()
frame.start()
