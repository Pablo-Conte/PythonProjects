from pynput import mouse
arq = open('PositionsAndClicks.txt')

def on_move(x, y):
    with open('PositionsAndClicks.txt', 'a') as arq:
        arq.write('Pointer moved to {0}\n'.format((x, y)))
        

def on_click(x, y, button, pressed):
    with open('PositionsAndClicks.txt', 'a') as arq:
        arq.write('Pressed at {0}\n'.format((x, y)))

with mouse.Listener(
        on_move=on_move,
        on_click=on_click) as listener:
    listener.join()

listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click)
listener.start()