
from pynput import keyboard

# 1. Define the log file
log = "log.txt" 

def on_press(key):
    """
    Handles key press events.
    Logs characters directly, and logs the name of special keys.
    """
    try:
        # sajel kol char 
        char_to_log = key.char 
        
    
    except AttributeError:
        
        # shift/ctrl/space lezem methode o5ra 5ater yetsajlou sous forme key.shit key.ctrl
        char_to_log = f'[{str(key).split(".")[-1].upper()}]'
    
    # check key li 5theh
    print(f'Logged: {char_to_log}')
    
    # save fel txt "a" hiya fonctins append
    with open(log, "a") as f:
        f.write(char_to_log)
        
    # exit
    if key == keyboard.Key.esc:
        print("\n--- Listener stopped (Escape key pressed). ---")
        return False # ywa9ef listener

#mm

print("--- Simple Keyboard Monitor ---")
print("Monitoring inputs. Press 'Esc' to stop.")
print(f"Logs are saved to: {log}\n")

# Start the listener and wait for it to stop
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

print("© 2025 Abdelaziz Ounissi")