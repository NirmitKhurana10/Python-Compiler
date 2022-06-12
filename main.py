import subprocess
from tkinter import*
from tkinter import messagebox, filedialog


class Vs_code:
    def __init__(self, root):
        self.root = root
        self.root.title("Bits N Bytes")
        self.root.geometry("1350x700+0+0")

        self.path_name = ''

        self.colortheme = StringVar()
        self.colortheme.set('Light (default)')

        self.font_size = 11

        # ========= SHORTCUTS ===========
        self.root.bind('<Control-plus>',self.font_size_increment)
        self.root.bind('<Control-minus>',self.font_size_decrement)
        self.root.bind('<Control-n>',self.new_file)
        self.root.bind('<Control-s>',self.save_file)
        self.root.bind('<Control-Shift-S>',self.save_as_file)
        self.root.bind('<Control-o>',self.open_file)
        self.root.bind('<Control-F4>',self.exit_func)
        self.root.bind('<Control-F5>',self.run)




        
        # ========= MENU ICONS ===========

        self.file_icon = PhotoImage(file='icons/File.png')
        self.open_icon = PhotoImage(file='icons/open.png')
        self.save_icon = PhotoImage(file='icons/save.png')
        self.save_as_icon = PhotoImage(file='icons/save_as.png')
        self.exit_icon = PhotoImage(file='icons/exit.png')

        self.light_default_icon = PhotoImage(file='icons/light.png')
        self.dark_icon = PhotoImage(file='icons/dark.png')
        self.red_icon = PhotoImage(file='icons/red.png')
        self.monokai_icon = PhotoImage(file='icons/monokai.png')
        self.night_blue_icon = PhotoImage(file='icons/nightblue.png')

        # ========= MENU FOR COMPILER ===========

        Mymenu = Menu(self.root)

        Filemenu = Menu(Mymenu, tearoff=False)
        Filemenu.add_command(label='New File', image=self.file_icon,
                             compound=LEFT, accelerator='Ctrl + N', command=self.new_file)
        Filemenu.add_command(label='Open File ', image=self.open_icon,
                             compound=LEFT, accelerator='Ctrl + O', command=self.open_file)
        Filemenu.add_command(label='Save', image=self.save_icon,
                             compound=LEFT, accelerator='Ctrl + S', command=self.save_file)
        Filemenu.add_command(label='Save As..', image=self.save_as_icon, compound=LEFT,
                             accelerator='Ctrl + Shift_L + S', command=self.save_as_file)
        Filemenu.add_separator()
        Filemenu.add_command(label='Exit', image=self.exit_icon,
                             compound=LEFT, accelerator='Ctrl + F4', command=self.exit_func)

        Viewmenu = Menu(Mymenu, tearoff=False)
        Viewmenu.add_radiobutton(label='Light (default)', value='Light (default)',
                                 variable=self.colortheme, image=self.light_default_icon, compound=LEFT, command=self.color_change)
        Viewmenu.add_radiobutton(label='Monokai', value='Monokai',
                                 variable=self.colortheme, image=self.monokai_icon, compound=LEFT, command=self.color_change)
        Viewmenu.add_radiobutton(
            label='Dark', value='Dark', variable=self.colortheme, image=self.dark_icon, compound=LEFT, command=self.color_change)
        Viewmenu.add_radiobutton(
            label='Red', value='Red', variable=self.colortheme, image=self.red_icon, compound=LEFT, command=self.color_change)
        Viewmenu.add_radiobutton(label='Night Blue', value='Night Blue',
                                 variable=self.colortheme, image=self.night_blue_icon, compound=LEFT, command=self.color_change)

        Mymenu.add_cascade(label='File', menu=Filemenu)
        Mymenu.add_cascade(label='View', menu=Viewmenu)
        Mymenu.add_command(label='Clear', command=self.clear_all)
        Mymenu.add_separator()
        Mymenu.add_command(label='Run (Ctrl + F5)',command = self.run)

        self.root.config(menu=Mymenu)

        # ========= MENU END HERE ===========

        # ========= INPUT FRAME ===========

        InputFrame = Frame(self.root, bg="white")
        InputFrame.place(x=0, y=0, relwidth=1, height=500)

        scrolly = Scrollbar(InputFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)
        self.txt_in_inputframe = Text(InputFrame, bg="white", font=(
            'consolas', self.font_size), yscrollcommand=scrolly.set)
        self.txt_in_inputframe.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_in_inputframe.yview)

        # ========= OUTPUT FRAME ===========


        outputFrame = Frame(self.root, bg="white")
        outputFrame.place(x=0, y=500, relwidth=1, height=200)
        scrolly = Scrollbar(outputFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)
        self.txt_in_outputframe = Text(outputFrame, bg="white", font=(
            'consolas', 12), yscrollcommand=scrolly.set)
        self.txt_in_outputframe.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_in_outputframe.yview)

        # ========= ALL FUNCTIONS ===========

    def save_as_file(self,event=None):
        path = filedialog.asksaveasfilename(
            filetypes=[('Python Files', '*py')], defaultextension=('.py'))
        if path != '':
            self.path_name = path
            fp = open(self.path_name, 'w')
            fp.write(self.txt_in_inputframe.get('1.0', END))
            fp.close()

    def open_file(self,event=None):
        path = filedialog.askopenfilename(
            filetypes=[('Python Files', '*py')], defaultextension=('.py'))
        if path != '':
            self.path_name = path
            fp = open(self.path_name, 'r')
            data = fp.read()
            self.txt_in_inputframe.delete('1.0', END)
            self.txt_in_inputframe.insert('1.0', data)
            fp.close()

    def save_file(self,event=None):
        if self.path_name == "":
            self.save_as_file()
        else:
            fp = open(self.path_name, 'w')
            fp.write(self.txt_in_inputframe.get('1.0', END))
            fp.close()

    def new_file(self,event=None):
        self.path_name = ''
        self.txt_in_inputframe.delete('1.0', END)
        self.txt_in_outputframe.delete('1.0', END)

    def exit_func(self,event=None):
        self.root.destroy()


    def color_change(self):
        if self.colortheme.get() == 'Light (default)':
            self.txt_in_outputframe.config(bg='#ffffff', fg='#000000')
            self.txt_in_inputframe.config(bg='#ffffff', fg='#000000')

        if self.colortheme.get() == 'Monokai':
            self.txt_in_outputframe.config(bg='#1a1a2e', fg='#F8F8F2')
            self.txt_in_inputframe.config(bg='#1a1a2e', fg='#F8F8F2')

        if self.colortheme.get() == 'Dark':
            self.txt_in_outputframe.config(bg='#2d2d2d', fg='#06FF00')
            self.txt_in_inputframe.config(bg='#2d2d2d', fg='#06ff00')

        if self.colortheme.get() == 'Red':
            self.txt_in_outputframe.config(bg='#f05454', fg='#2d2d2d')
            self.txt_in_inputframe.config(bg='#f05454', fg='#2d2d2d')

        if self.colortheme.get() == 'Night Blue':
            self.txt_in_outputframe.config(bg='#04293A', fg='#FEC260')
            self.txt_in_inputframe.config(bg='#04293A', fg='#FEC260')

    def clear_all(self): 
        self.txt_in_inputframe.delete('1.0', END)
        self.txt_in_outputframe.delete('1.0', END)


    def run(self,event=None):
        if self.path_name == '':
            messagebox.showerror('Error', 'Please save the file to execute the code')
        else:
            command = f'python {self.path_name}'
            run_file=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=TRUE)
            output,error=run_file.communicate()
            self.txt_in_outputframe.delete('1.0',END)
            self.txt_in_outputframe.insert('1.0',output)
            self.txt_in_outputframe.insert('1.0',error)


    def font_size_increment(self,event=None):
        self.font_size += 1
        self.txt_in_inputframe.config(font=('consolas',self.font_size))

    def font_size_decrement(self,event=None):
        self.font_size -= 1
        self.txt_in_inputframe.config(font=('consolas',self.font_size))


root = Tk()
obj = Vs_code(root)
root.mainloop()
