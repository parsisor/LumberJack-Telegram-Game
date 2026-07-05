from pynput import mouse

coords = []

def on_click(x, y, button, pressed):
    if pressed:
        coords.append((x, y))
        print(x, y)

listener = mouse.Listener(on_click=on_click)
listener.start()

listener.join()