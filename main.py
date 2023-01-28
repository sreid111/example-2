x = 0

def on_forever():
    global x
    x = x + 1
    basic.show_number(x)
    basic.pause(1000)
basic.forever(on_forever)
