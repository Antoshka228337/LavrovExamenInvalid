from tkinter import Tk, CENTER, Label, Button, Entry #Импортируемые библиотеки
from tkinter import messagebox
import cProfile


window = Tk()
window.title('Авторизация')
window.geometry('450x230')
window.resizable(False, False)
font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}


def clicked():
    username = username_entry.get()
    password = password_entry.get()
    messagebox.showinfo('Заголовок', '{username}, {password}'.format(
       username=username, password=password))


main_label = Label(window, text='Авторизация', font=font_header,
                   justify=CENTER, **header_padding)
main_label.pack()

username_label = Label(window, text='Имя пользователя',
                       font=label_font, **base_padding)
username_label.pack()

username_entry = Entry(window, bg='#B5DEFA', fg='#444', font=font_entry)
username_entry.pack()

password_label = Label(window, text='Пароль', font=label_font, **base_padding)
password_label.pack()

password_entry = Entry(window, bg='#B5DEFA', fg='#444', font=font_entry)
password_entry.pack()

send_btn = Button(window, text='Войти', command=clicked)
send_btn.pack(**base_padding)

window.mainloop()
cProfile.run('window.mainloop()')
