# template for "Stopwatch: The Game"

import simplegui
# define global variables
tens_sec = 0
try_cnt = 0
success_cnt = 0 

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    """convert time in tenths of seconds
    into formated string
    """
    min = tens_sec / 600
    sec = (tens_sec % 600) / 10
    tens = (tens_sec % 600) % 10
    
    min_str = str(min)
    
    if sec == 0:
        sec_str = '00'
    elif sec < 10:
        sec_str = '0' + str(sec)
    else:
        sec_str = str(sec)
    
    tens_str = str(tens)
    
    result = min_str + ':' + sec_str + '.' + tens_str
    return result
    

    
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start_handler():
    timer.start()

def stop_handler():
    global try_cnt, success_cnt, tens_sec
    if timer.is_running():
        try_cnt  = try_cnt + 1
        if tens_sec % 10 == 0:
            success_cnt = success_cnt + 1
    
    timer.stop()
    

def reset_handler():
    global tens_sec, try_cnt, success_cnt
    tens_sec = 0
    try_cnt = 0
    success_cnt = 0
    timer.stop()


# define event handler for timer with 0.1 sec interval

def timer_handler():
    
    global tens_sec
    
    tens_sec = tens_sec + 1

    


# define draw handler

def display_result(canvas):
    canvas.draw_text(format(tens_sec), [80, 120], 60, 'Red')
    global try_cnt, success_cnt
    result = str(success_cnt) + '/' + str(try_cnt)
    canvas.draw_text(result, [240, 40], 40, 'Green')

    
# create frame

frame = simplegui.create_frame('Stop Watch', 300, 200)

# register event handlers


frame.set_draw_handler(display_result)
frame.add_button('Start',start_handler, 150)
frame.add_button('Stop', stop_handler, 150)
frame.add_button('Reset', reset_handler, 150)
timer = simplegui.create_timer(100, timer_handler)



# start frame

frame.start()
# Please remember to review the grading rubric
