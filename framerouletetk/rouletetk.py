from tkinter import Frame
from tkinter import Tk
from typing import Callable
from typing import Union

#Class Roulete that manages the frames
class Roulete(Frame):
    def __init__(self,parent:Tk):
        super().__init__(parent)
        self.__frame_roulete:dict[str, Callable[[Frame], Frame]] = {} #Saves callable obj that recieves and return the obj Frame
        self.__current_f:Frame = NotImplemented #Aux var for saves current frame obj
    
    #Insert the drame at the frame dictionary
    def insert(self,tag_name:str="",frame: Union[Callable[[Frame], Frame], Frame]= None)-> None:
        self.__frame_roulete[tag_name]= (lambda f: frame) if isinstance(frame,Frame) else frame
    
    #Set the frame that is to going to appear first
    def main_frame(self,tag_name:str="")-> None:
        self.__instance_frame(tag_name=tag_name)
    
    #Select the frame and spawns it destroying the previous one
    def turn_towars_at(self,tag_name:str="")-> None:
        
        if self.__current_f:
           self.__current_f.destroy() #Destroys the last frame if exist

        self.__instance_frame(tag_name=tag_name) #Instance the frame according to the name
    
    #Intern function that instance the frame ancording the name
    def __instance_frame(self,tag_name:str)-> None:
        if self.__frame_roulete!= {}:
           frame:Callable[[Frame], Frame] = self.__frame_roulete[tag_name] #Create a Callable obj tha recieves a Frame obj
           create_frame = frame(self)
           self.__current_f = create_frame #Saves the frame obj into __current variable
           self.__current_f.pack(fill="both", expand=True) #Instance __current


