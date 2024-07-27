from pynput import keyboard

# Teclas de movimiento en CS2
left_key = keyboard.KeyCode.from_char('a')
right_key = keyboard.KeyCode.from_char('d')

# Crear una instancia del controlador de teclado
controller = keyboard.Controller()

# Variables globales para el estado de las teclas
isAPressed = False
isDPressed = False

def on_press(key):
    press_counter_key(key)

def on_release(key):
    global isAPressed, isDPressed
    if key == left_key:
        isAPressed = False
    elif key == right_key:
        isDPressed = False
    print(f"Key soltada {key}")

def press_counter_key(key):
    global isAPressed, isDPressed
    if key == right_key:
        isDPressed = True
        if isAPressed:
            controller.release(left_key)
    elif key == left_key:
        isAPressed = True
        if isDPressed:
            controller.release(right_key)

# Configurar el listener del teclado
listener = keyboard.Listener(on_press=on_press, on_release=on_release)

# Iniciar el listener
listener.start()
listener.join()