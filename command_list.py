import webbrowser
import os


def execute_command(texto):
    if "open youtube" in texto:
        webbrowser.open("https://www.youtube.com")
        return True
    elif "open spotify" in texto:
        webbrowser.open("https://open.spotify.com")
        return True
    elif "open calculator" in texto:
        os.system("calc" if os.name == "nt" else "gnome-calculator")
        return True
    return False
