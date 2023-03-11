import customtkinter as ctk
import modules.screen_app as m_app

width_MessageFrame = 100
height_MessageFrame = 47

class MessageFrame(ctk.CTkFrame):
    def __init__(self, user_name, message_text, master, width, height, border_width, **kwargs):
        super().__init__(master= master, width= width, height= height, border_width= border_width, **kwargs)
        self.FONT_MESSAGE = ctk.CTkFont(family="Arial", size=12, weight="normal")
        self.FONT_USERNAME = ctk.CTkFont(family="Arial", size=15, weight="bold")
        self.MESSAGE_LABEL = self.message_label(message_text= message_text)
        self.USER_NAME_LABEL = self.username_label(username= user_name)
        
    
    def message_label(self, message_text):
        msg =  ctk.CTkLabel(master= self, text= message_text, font= self.FONT_MESSAGE)
        msg.place(x = 20, y = 20)
        return msg
        

    def username_label(self, username):
        user =  ctk.CTkLabel(master=self, text= username, font= self.FONT_USERNAME, text_color="orange")
        user.place(x= 35, y = 0)
        return user

message = MessageFrame(
    user_name= "User", 
    message_text= "Hello, user!", 
    master = m_app.main_app.FRAME4, 
    width= width_MessageFrame,
    height = height_MessageFrame,
    border_width= 0
)

message.place(x = 30, y = 405)