function spawnFood () {
    fx = randint(0, 4)
    fy = randint(0, 4)
}
input.onButtonPressed(Button.A, function () {
    if (vx != 0) {
        vx = 0 - vx
    }
    temp = vx
    vx = vy
    vy = temp
})
function drawFood () {
    led.plotBrightness(fx, fy, 25)
}
function moveSnake () {
    basic.clearScreen()
    for (let value of segments) {
        led.plot(value % 5, Math.idiv(value, 5))
    }
    segments.push((segments[length - 1] + vx + 5) % 5 + 5 * (vy + Math.idiv(segments[length - 1], 5) + 5) % 25)
    if (segments[length] == fx + 5 * fy) {
        spawnFood()
        length += 1
    } else {
        segments.shift()
    }
    if (isColliding()) {
        gameOver = true
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.PowerDown), music.PlaybackMode.UntilDone)
    }
}
input.onButtonPressed(Button.B, function () {
    if (vy != 0) {
        vy = 0 - vy
    }
    temp = vx
    vx = vy
    vy = temp
})
function isColliding () {
    for (let segment of segments.slice(0, -1)) {
        if (segment == segments[length - 1]) {
            return true
        }
    }
    return false
}
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    gameOver = !(gameOver)
})
function reset () {
    length = 3
    vy = 1
    segments = [0, 5, 10]
    spawnFood()
}
let temp = 0
let vx = 0
let vy = 0
let length = 0
let fy = 0
let fx = 0
let gameOver = false
let segments: number[] = []
gameOver = true
fx = -1
fy = -1
length = 3
vy = 1
segments = [0, 5, 10]
spawnFood()
basic.forever(function () {
    if (!(gameOver)) {
        moveSnake()
        drawFood()
    } else {
        basic.showIcon(IconNames.SmallHeart)
        basic.showIcon(IconNames.Heart)
    }
    basic.pause(500)
})
