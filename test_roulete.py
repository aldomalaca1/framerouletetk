from framerouletetk.rouletetk import Roulete
from tkinter import Frame,Tk,Label
from tkinter import Button

class FrameOne(Frame):
    def __init__(self, parent:Frame):
        super().__init__(parent)
        Label(self, text="Este es el Frame Uno").pack()
        Button(self, name="button test", text="button text").pack()

class FrameTwo(Frame):
    def __init__(self, parent:Frame):
        super().__init__(parent)
        Label(self, text="Este es el Frame Dos").pack(padx=20, pady=20)


def main()->None:
   root = Tk()
   rt = Roulete(parent=root)
   rt.pack(fill="both", expand=True)

   frameThree = Frame(rt)
   lb = Label(frameThree, text="Frame tres")
   lb.pack()
   lb.config(background="blue")
   bt = Button(frameThree)
   bt.pack()
   bt.config(text="button")

   rt.insert(tag_name="0", frame=FrameOne)  
   rt.insert(tag_name="1", frame=FrameTwo)
   rt.insert(tag_name="2", frame=frameThree)
    
   rt.main_frame("1")
   #rt.turn_towars_at("0")
   
   root.after(2000, lambda: rt.turn_towars_at("0"))
   root.after(4000, lambda: rt.turn_towars_at("1"))
   root.after(4000, lambda: rt.turn_towars_at("2"))
   
   root.mainloop()

if __name__ == "__main__":
    main()