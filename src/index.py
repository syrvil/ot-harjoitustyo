from tkinter import Tk
from ui.image_app import ImageApp


def main():
    window = Tk()
    window.title("Image Tagging App")
    ImageApp(window).start()
    window.mainloop()


if __name__ == "__main__":
    main()
