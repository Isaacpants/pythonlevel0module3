from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    window = Tk()
    window.withdraw()
    answer = simpledialog.askstring(title = 'kk', prompt = "Are you happy?")
    if answer == 'yes':
        messagebox.showinfo('',"e")
    pass
