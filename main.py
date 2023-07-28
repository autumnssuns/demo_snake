def spawnFood():
    global fx, fy
    fx = randint(0, 4)
    fy = randint(0, 4)

def on_button_pressed_a():
    global vx, temp, vy
    if vx != 0:
        vx = 0 - vx
    temp = vx
    vx = vy
    vy = temp
input.on_button_pressed(Button.A, on_button_pressed_a)

def drawFood():
    led.plot_brightness(fx, fy, 125)
def moveSnake():
    global length
    basic.clear_screen()
    for value in segments:
        led.plot(value % 5, Math.idiv(value, 5))
    segments.append((segments[length - 1] + vx + 5) % 5 + 5 * (vy + Math.idiv(segments[length - 1], 5) + 5) % 25)
    if segments[length] == fx + 5 * fy:
        spawnFood()
        length += 1
    else:
        segments.shift()
    if isColliding():
        music.string_playable("", 120)
        gameOver = True

def on_button_pressed_b():
    global vy, temp, vx
    if vy != 0:
        vy = 0 - vy
    temp = vx
    vx = vy
    vy = temp
input.on_button_pressed(Button.B, on_button_pressed_b)

def isColliding():
    for segment in segments.slice(0, -1):
        if segment == segments[length - 1]:
            return True
    return False

def on_logo_pressed():
    global gameOver2
    gameOver2 = not (gameOver2)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def reset():
    global length, vy, segments
    length = 3
    vy = 1
    segments = [0, 5, 10]
    spawnFood()
temp = 0
vx = 0
vy = 0
length = 0
fy = 0
fx = 0
gameOver2 = False
segments: List[number] = []
gameOver2 = True
fx = -1
fy = -1
length = 3
vy = 1
segments = [0, 5, 10]
spawnFood()

def on_forever():
    if not (gameOver2):
        moveSnake()
        drawFood()
    else:
        basic.show_icon(IconNames.SMALL_HEART)
        basic.show_icon(IconNames.HEART)
    basic.pause(200)
basic.forever(on_forever)
