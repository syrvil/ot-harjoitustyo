from tkinter import Tk, messagebox
from ui.image_app import ImageApp


def main():
    window = Tk()
    window.title("Image Tagging App")
    app = ImageApp(window)

    def on_close():
        result = messagebox.askyesnocancel(
            "Save Changes", "Do you want to save configation file changes?")
        if result is None:
            return
        if result:
            print("kutsutaan ImageApp.save_changes()")
            app.save_conf_changes()
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_close)
    window.mainloop()


if __name__ == "__main__":
    main()
