from tkinter import simpledialog, messagebox, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    sanswer1 = simpledialog.askstring('','s?')
    if sanswer1=='s':
        messagebox.showinfo('', 's')
        sanswer2 = simpledialog.askstring('', 't?')
        if sanswer2 == 't':
            messagebox.showinfo('', 'st')
            sanswer3 = simpledialog.askstring('', 'y?')
            if sanswer3 == 'y':
                messagebox.showinfo('', 'story')
            else:
                messagebox.showinfo('', 'wrong')
        else:
            messagebox.showinfo('', 'wrong')
    else:
        messagebox.showinfo('', 'wrong')
            # TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
