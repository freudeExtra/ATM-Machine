from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import tkinter.messagebox
import time

class atm:
    def __init__(self, app):
        self.app = app
        blank_space = " "
        self.app.title(110 * blank_space + "ATM System")
        self.app.geometry("790x760+280+0")
        self.app.resizable(False, False)
        self.app.configure(bg = 'gainsboro')
        self.app.iconbitmap('atmicon.ico')
        #===========================Frames==========================
        
        MainFrame = Frame(self.app, bd=20, width=780, height=700, relief=RIDGE)
        MainFrame.grid()
        
        m_BottomFrame = Frame(MainFrame, bd=7, width=734, height=300, relief=RIDGE)
        m_BottomFrame.grid(row=1, column=0, padx=12)
        m_UpperFrame = Frame(MainFrame,  bd=7, width=734, height=300, relief=RIDGE)
        m_UpperFrame.grid(row=0, column=0, padx=8)
        
        m_UpperFrameLeft = Frame(m_UpperFrame, bd=5, width=190, height=300, relief=RIDGE, )
        m_UpperFrameLeft.grid(row=1, column=0, padx=3)
        
        m_UpperFrameMid = Frame(m_UpperFrame, bd=5, width=200, height=300, relief=RIDGE)
        m_UpperFrameMid.grid(row=1, column=1, padx=3)
        
        m_UpperFrameRight = Frame(m_UpperFrame, bd=5, width=190, height=300, relief=RIDGE)
        m_UpperFrameRight.grid(row=1, column=2, padx=3)
        
         #===========Variables=========#
        self.balance = 10000
        self.pinNo = '1234'
        self.ui_amount = 0
        self.localtime = str(time.asctime(time.localtime(time.time())))
        
        #===========Text box=========#
        self.txtReceipt = Text(m_UpperFrameMid, height=9, width=21, bd=12, font=('arial', 18, 'bold'))
        self.txtReceipt.grid(row=1, column=0)
        
        #============input box ===============#
        self.input_box = Entry(m_UpperFrameMid, state=DISABLED, font=('arial', 18, 'bold'))
        
        #========== Side arrows ===============#    
        self.img_arrow_Left = ImageTk.PhotoImage(Image.open('button-icons/arrowL.png'))
        self.btnArrowL1 = Button(m_UpperFrameLeft, width=160, height=60, state=DISABLED, image=self.img_arrow_Left)
        self.btnArrowL2 = Button(m_UpperFrameLeft, width=160, height=60, state=DISABLED, image=self.img_arrow_Left)
        self.btnArrowL3 = Button(m_UpperFrameLeft, width=160, height=60, state=DISABLED, image=self.img_arrow_Left)
        self.btnArrowL4 = Button(m_UpperFrameLeft, width=160, height=60, state=DISABLED, image=self.img_arrow_Left)
            
        self.img_arrow_Right = ImageTk.PhotoImage(Image.open('button-icons/arrowR.png'))
        self.btnArrowR1 = Button(m_UpperFrameRight, width=160, height=60, state=DISABLED, image=self.img_arrow_Right)
        self.btnArrowR2 = Button(m_UpperFrameRight, width=160, height=60, state=DISABLED, image=self.img_arrow_Right)
        self.btnArrowR3 = Button(m_UpperFrameRight, width=160, height=60, state=DISABLED, image=self.img_arrow_Right)
        self.btnArrowR4 = Button(m_UpperFrameRight, width=160, height=60, state=DISABLED, image=self.img_arrow_Right)
            
            #======================PinNumberButton=======================
        self.img1 = ImageTk.PhotoImage(Image.open('button-icons/One.png'))
        self.btn1 = Button(m_BottomFrame, width=160, height=60, state=NORMAL, image=self.img1)
            
        self.img2 = ImageTk.PhotoImage(Image.open('button-icons/Two.png'))
        self.btn2 = Button(m_BottomFrame, width=160, height=60, state=NORMAL, image=self.img2)
            
        self.img3 = ImageTk.PhotoImage(Image.open('button-icons/Three.png'))
        self.btn3 = Button(m_BottomFrame, width=160, height=60, state=NORMAL, image=self.img3)
            
        self.imgCE = ImageTk.PhotoImage(Image.open('button-icons/Cancel.png'))
        self.btnCancel = Button(m_BottomFrame, width=160, height=60, state=NORMAL, command=self.cancel, image=self.imgCE)
            #======================
        self.img4 = ImageTk.PhotoImage(Image.open('button-icons/Four.png'))
        self.btn4 = Button(m_BottomFrame, width=160, height=60, state=NORMAL, image=self.img4)
            
        self.img5 = ImageTk.PhotoImage(Image.open('button-icons/Five.png'))
        self.btn5 = Button(m_BottomFrame, width=160, height=60, state=NORMAL, image=self.img5)
            
        self.img6 = ImageTk.PhotoImage(Image.open('button-icons/Six.png'))
        self.btn6 = Button(m_BottomFrame, width=160, height=60, state=NORMAL, image=self.img6)
            
        self.imgCL = ImageTk.PhotoImage(Image.open('button-icons/Clear.png'))
        self.btnClear = Button(m_BottomFrame, width=160, height=60, state=NORMAL, command=self.Clear, image=self.imgCL)
            #======================
        self.img7 = ImageTk.PhotoImage(Image.open('button-icons/Seven.png'))
        self.btn7 = Button(m_BottomFrame, width=160, height=60, state=NORMAL,  image=self.img7)
            
        self.img8 = ImageTk.PhotoImage(Image.open('button-icons/Eight.png'))
        self.btn8 = Button(m_BottomFrame, width=160, height=60, state=NORMAL,  image=self.img8)
            
        self.img9 = ImageTk.PhotoImage(Image.open('button-icons/Nine.png'))
        self.btn9 = Button(m_BottomFrame, width=160, height=60, state=NORMAL, image=self.img9)
            
        self.imgEnter = ImageTk.PhotoImage(Image.open('button-icons/Enter.png'))
        self.btnEnter = Button(m_BottomFrame, width=160, height=60, state=NORMAL,  command=self.login, image=self.imgEnter)
            #======================
        self.imgEM1 = ImageTk.PhotoImage(Image.open('button-icons/Empty.png'))
        self.btnEmpty1 = Button(m_BottomFrame, width=160, height=60, state=DISABLED,  image=self.imgEM1)
            
        self.img0 = ImageTk.PhotoImage(Image.open('button-icons/Zero.png'))
        self.btn0 = Button(m_BottomFrame, width=160, height=60, state=NORMAL, image=self.img0)
            
        self.imgEM2 = ImageTk.PhotoImage(Image.open('button-icons/Empty.png'))
        self.btnEmpty2 = Button(m_BottomFrame, width=160, height=60, state=DISABLED,  image=self.imgEM2)
            
        self.imgEM3 = ImageTk.PhotoImage(Image.open('button-icons/Empty.png'))
        self.btnEmpty3 = Button(m_BottomFrame, width=160, height=60, state=DISABLED,  image=self.imgEM3)
         #====================== OTHER WIDGETS=============
        
        self.gui()
        #===========================Functions=========================
    def gui(self):
        self.txtReceipt.delete(1.0, END)
        self.input_box.delete(0, END)
        self.exitPrompt = ImageTk.PhotoImage(Image.open('image-display/login.png')) 
        self.txtReceipt.image_create(END, image=self.exitPrompt)
        
        self.ui_amount = 0
        self.btnEnter.configure(command=self.login)
        self.input_box.configure(state=NORMAL)
        
        self.btnArrowL1.configure(state=DISABLED)
        self.btnArrowL2.configure(state=DISABLED)
        self.btnArrowL3.configure(state=DISABLED)   
        self.btnArrowL4.configure(state=DISABLED)
        self.btnArrowR1.configure(state=DISABLED)
        self.btnArrowR2.configure(state=DISABLED)
        self.btnArrowR3.configure(state=DISABLED)
        self.btnArrowR4.configure(state=DISABLED)
        
        self.numpad_inputbox()
        
        self.input_box.grid(row=2, column=0)
        
        self.btnArrowL1.grid(row=0, column=0, padx=2, pady=2)
        self.btnArrowL2.grid(row=1, column=0, padx=2, pady=2)
        self.btnArrowL3.grid(row=2, column=0, padx=2, pady=2)
        self.btnArrowL4.grid(row=3, column=0, padx=2, pady=2)
            
        self.btnArrowR1.grid(row=0, column=0, padx=2, pady=2)
        self.btnArrowR2.grid(row=1, column=0, padx=2, pady=2)
        self.btnArrowR3.grid(row=2, column=0, padx=2, pady=2)
        self.btnArrowR4.grid(row=3, column=0, padx=2, pady=2)
            
        self.btn1.grid(row=0, column=0, padx=6, pady=4)
        self.btn2.grid(row=0, column=1, padx=6, pady=4)
        self.btn3.grid(row=0, column=2, padx=6, pady=4)
        self.btn4.grid(row=1, column=0, padx=4, pady=4)
        self.btn5.grid(row=1, column=1, padx=6, pady=4)
        self.btn6.grid(row=1, column=2, padx=6, pady=4)
        self.btn7.grid(row=2, column=0, padx=4, pady=4)
        self.btn8.grid(row=2, column=1, padx=6, pady=4)
        self.btn9.grid(row=2, column=2, padx=6, pady=4)
        self.btn0.grid(row=3, column=1, padx=6, pady=4)
            
        self.btnCancel.grid(row=0, column=3, padx=4, pady=4)
        self.btnClear.grid(row=1, column=3, padx=4, pady=4)
        self.btnEnter.grid(row=2, column=3, padx=4, pady=4)
        self.btnEmpty1.grid(row=3, column=0, padx=4, pady=4)
        self.btnEmpty2.grid(row=3, column=2, padx=6, pady=4)
        self.btnEmpty3.grid(row=3, column=3, padx=4, pady=4)
        
    def login(self):
        pinNo = self.input_box.get()
        if (pinNo == self.pinNo):
            self.txtReceipt.delete(1.0, END)
            self.main_menu()
        else:
            self.txtReceipt.delete(1.0, END)
            self.input_box.delete(0,END)
            self.txtReceipt.insert(END, 'Invalid Pin Number' + "\n\n" )
    def main_menu(self):
        self.txtReceipt.delete(1.0, END)
        self.input_box.delete(0, END)
        self.input_box.configure(state=DISABLED)
        # Configure, Enable all side buttons
        self.btnArrowL1.configure(state=NORMAL, command=self.withdrawcash)
        self.btnArrowL2.configure(state=NORMAL, command=self.transfer)
        self.btnArrowL3.configure(state=DISABLED, command=self.cancel)
        self.btnArrowL4.configure(state=DISABLED, command=self.cancel)
        self.btnArrowR1.configure(state=NORMAL, command=self.deposit)
        self.btnArrowR2.configure(state=NORMAL, command=self.acc_balance)
        self.btnArrowR3.configure(state=NORMAL, command=self.pinchange)
        self.btnArrowR4.configure(state=DISABLED, command=self.cancel)
        # Insert Main Menu 
        self.text_file = open('const-text/mainMenu.txt', 'r')
        self.text = self.text_file.read()
        self.txtReceipt.insert(END, self.text)
        self.text_file.close()
    def exit_prompt(self):
        self.txtReceipt.delete(1.0, END)
        self.input_box.configure(state=DISABLED)
        self.exitPrompt = ImageTk.PhotoImage(Image.open('image-display/exitPrompt.png')) 
        self.txtReceipt.image_create(END, image=self.exitPrompt)
        self.app.after(5000, self.gui)
    def Clear(self):
        self.txtReceipt.delete(1.0, END)
        self.input_box.delete(0, END)
        self.gui()
    def cancel(self):
        Cancel = tkinter.messagebox.askyesno("ATM", "Confirm if you want to cancel")
        if Cancel > 0:
            self.txtReceipt.delete(1.0, END)
            self.exitPrompt = ImageTk.PhotoImage(Image.open('image-display/exitPrompt.png')) 
            self.txtReceipt.image_create(END, image=self.exitPrompt)
            
            self.app.after(5000, self.app.destroy)
            return 
        
    # === NUMPAD FUNCTIONS
    def numpad(self, num):
        self.txtReceipt.insert(END, str(num))
    def input_entrybox(self, num):
        in_num = self.input_box.get()
        self.input_box.delete(0, END)
        self.input_box.insert(0, str(in_num) + str(num))
    def numpad_inputbox(self):
        self.btn0.configure(command=lambda:self.input_entrybox(0))
        self.btn1.configure(command=lambda:self.input_entrybox(1))
        self.btn2.configure(command=lambda:self.input_entrybox(2))
        self.btn3.configure(command=lambda:self.input_entrybox(3))
        self.btn4.configure(command=lambda:self.input_entrybox(4))
        self.btn5.configure(command=lambda:self.input_entrybox(5))
        self.btn6.configure(command=lambda:self.input_entrybox(6))
        self.btn7.configure(command=lambda:self.input_entrybox(7))
        self.btn8.configure(command=lambda:self.input_entrybox(8))
        self.btn9.configure(command=lambda:self.input_entrybox(9))
    def numpad_textbox(self):
        self.btn0.configure(command=lambda:self.numpad(0))
        self.btn1.configure(command=lambda:self.numpad(1))
        self.btn2.configure(command=lambda:self.numpad(2))
        self.btn3.configure(command=lambda:self.numpad(3))
        self.btn4.configure(command=lambda:self.numpad(4))
        self.btn5.configure(command=lambda:self.numpad(5))
        self.btn6.configure(command=lambda:self.numpad(6))
        self.btn7.configure(command=lambda:self.numpad(7))
        self.btn8.configure(command=lambda:self.numpad(8))
        self.btn9.configure(command=lambda:self.numpad(9))
        
    # Main menu functions
    def acc_balance(self):
        self.txtReceipt.delete(1.0, END)
        self.txtReceipt.insert(END, 'Your current balance is \n')
        self.txtReceipt.insert(END, '\t ₽' + str(self.balance)+ '\n\n\n\n\n')
        self.img_backoption = ImageTk.PhotoImage(Image.open('image-display/backtomainmenu.png'))
        self.txtReceipt.image_create(END, image=self.img_backoption)
        
        self.btnArrowL1.configure(state=DISABLED)
        self.btnArrowL2.configure(state=DISABLED)
        self.btnArrowL3.configure(state=DISABLED)   
        self.btnArrowR1.configure(state=DISABLED)
        self.btnArrowR2.configure(state=DISABLED)
        self.btnArrowR3.configure(state=DISABLED)
        self.btnArrowL4.configure(state=NORMAL, command=self.main_menu)
        self.btnArrowR4.configure(state=NORMAL, command=self.exit_prompt)
    
    # === WITHDRAW FUNCTIONS
    def withdraw_receipt(self):        
        self.txtReceipt.delete(1.0, END)
        self.input_box.configure(state=DISABLED)
        self.btnArrowL1.configure(state=DISABLED)
        self.btnArrowL2.configure(state=DISABLED)
        self.btnArrowL3.configure(state=DISABLED)   
        self.btnArrowL4.configure(state=DISABLED)
        self.btnArrowR1.configure(state=DISABLED)
        self.btnArrowR2.configure(state=DISABLED)
        self.btnArrowR3.configure(state=DISABLED)
        self.btnArrowR4.configure(state=DISABLED)  
        
        self.txtReceipt.insert(END, ' ==  ATM MACHINE  ==\n\n')
        self.txtReceipt.insert(END, 'Time:' + self.localtime)
        self.txtReceipt.insert(END, '\nCard          **********2213\n')
        self.txtReceipt.insert(END, 'Record no.             9913\n')
        self.txtReceipt.insert(END, 'Withdrawal        ₱' + str(self.ui_amount) + '\n')
        self.txtReceipt.insert(END, 'New Acct Bal    ₱' + str(self.balance) + '\n\n')
        self.txtReceipt.insert(END, 'You transaction is \nbeing processed...')
        self.app.after(6000, self.exit_prompt)
    def withdraw_EnterBtn(self):
        self.ui_amount = int(self.input_box.get())
        self.input_box.delete(0, END)
        if self.ui_amount % 100 == 0:
            self.txtReceipt.delete(1.0, END)
            self.balance = self.balance - self.ui_amount
            self.confirmation = ImageTk.PhotoImage(Image.open('image-display/confirmation.png'))
            self.txtReceipt.image_create(END, image=self.confirmation)
            
            self.btnArrowL1.configure(state=DISABLED)
            self.btnArrowL2.configure(state=DISABLED)
            self.btnArrowL3.configure(state=DISABLED)   
            self.btnArrowL4.configure(state=DISABLED)
            self.btnArrowR1.configure(state=DISABLED)
            self.btnArrowR2.configure(state=NORMAL, command=self.withdraw_receipt)
            self.btnArrowR3.configure(state=NORMAL, command=self.exit_prompt) 
            self.btnArrowR4.configure(state=DISABLED)
        else:
            self.withdrawcash()
    def withdrawcash(self):
        self.txtReceipt.delete(1.0, END)
        # Menu - from Text File
        self.text_file = open('const-text/withdrawPrompt.txt', 'r')
        self.text = self.text_file.read()
         
        self.txtReceipt.insert(END, self.text)
        self.btnArrowL1.configure(state=DISABLED)
        self.btnArrowL2.configure(state=DISABLED)
        self.btnArrowL3.configure(state=DISABLED)   
        self.btnArrowL4.configure(state=DISABLED)
        self.btnArrowR1.configure(state=DISABLED)
        self.btnArrowR2.configure(state=DISABLED)
        self.btnArrowR3.configure(state=DISABLED)
        self.btnArrowR4.configure(state=DISABLED)
        
        self.text_file.close()
        # Configure numpad 
        self.input_box.configure(state=NORMAL)
        self.numpad_inputbox()
        self.btnEnter.configure(command=self.withdraw_EnterBtn)
    
    # ==== DEPOSIT FUNCTIONS
    def deposit_receipt(self):        
        self.txtReceipt.delete(1.0, END)
        self.input_box.configure(state=DISABLED)
        self.btnArrowL1.configure(state=DISABLED)
        self.btnArrowL2.configure(state=DISABLED)
        self.btnArrowL3.configure(state=DISABLED)   
        self.btnArrowL4.configure(state=DISABLED)
        self.btnArrowR1.configure(state=DISABLED)
        self.btnArrowR2.configure(state=DISABLED)
        self.btnArrowR3.configure(state=DISABLED)
        self.btnArrowR4.configure(state=DISABLED)  
        
        self.txtReceipt.insert(END, ' ==  ATM MACHINE  ==\n\n')
        self.txtReceipt.insert(END, 'Time:' + self.localtime)
        self.txtReceipt.insert(END, '\nCard          **********2213\n')
        self.txtReceipt.insert(END, 'Record no.             9913\n')
        self.txtReceipt.insert(END, 'Deposit        ₱' + str(self.ui_amount) + '\n')
        self.txtReceipt.insert(END, 'New Acct Bal    ₱' + str(self.balance) + '\n\n')        
        self.txtReceipt.insert(END, 'You transaction is \nbeing processed...')
        self.app.after(6000, self.exit_prompt)
    def deposit_EnterBtn(self):
        temp = int(self.input_box.get())
        
        self.input_box.delete(0, END)
        self.txtReceipt.delete(1.0, END)
        if temp % 100 == 0:
            self.txtReceipt.delete(1.0, END)
            self.ui_amount = self.ui_amount + temp
            self.balance = self.balance + self.ui_amount
            self.txtReceipt.insert(END, 'You have inserted:\n₱' + str(self.ui_amount))
            self.txtReceipt.insert(END, '\n\n\n\n\n               Add more bills')
            self.txtReceipt.insert(END, '\n\n                         Confirm') 
            self.btnArrowL1.configure(state=DISABLED)
            self.btnArrowL2.configure(state=DISABLED)
            self.btnArrowL3.configure(state=DISABLED)   
            self.btnArrowL4.configure(state=DISABLED)
            self.btnArrowR1.configure(state=DISABLED)
            self.btnArrowR2.configure(state=DISABLED) 
            self.btnArrowR3.configure(state=NORMAL, command=self.deposit)
            self.btnArrowR4.configure(state=NORMAL, command=self.deposit_receipt)
        else:
            self.deposit()
    def deposit(self):
        self.txtReceipt.delete(1.0, END)
        self.input_box.delete(0, END) 
        # Menu - from Text File
        self.text_file = open('const-text/depositPrompt.txt', 'r')
        self.text = self.text_file.read()
        
        self.btnArrowL1.configure(state=DISABLED)
        self.btnArrowL2.configure(state=DISABLED)
        self.btnArrowL3.configure(state=DISABLED)   
        self.btnArrowL4.configure(state=DISABLED)
        self.btnArrowR1.configure(state=DISABLED)
        self.btnArrowR2.configure(state=DISABLED)
        self.btnArrowR3.configure(state=DISABLED)
        self.btnArrowR4.configure(state=DISABLED)
        
        self.txtReceipt.insert(END, self.text)
        self.text_file.close()
        
        # Configure numpad 
        self.input_box.configure(state=NORMAL)
        self.numpad_inputbox()
        self.btnEnter.configure(command=self.deposit_EnterBtn)
        
        
    
    # ==== CHANGE PIN 
    def input_newPin(self):
        self.pinNo = self.input_box.get()
        self.txtReceipt.delete(1.0, END)
        self.input_box.delete(0, END)
        self.txtReceipt.insert(END, '\nSuccessfully Changed!\n\nPlease wait...')
        self.app.after(5000, self.exit_prompt)
    def confirm_pin(self):
        pinNo = self.input_box.get()
        if (pinNo == self.pinNo):
            self.input_box.delete(0, END)
            self.txtReceipt.insert(END, '\n\nInsert your new pin code')
            self.btnEnter.config(command=self.input_newPin)
        else:
            self.txtReceipt.delete(1.0, END)
            self.txtReceipt.insert(END, 'Invalid Pin Number  \n\nPress [ENTER] \nto continue')
            self.btnEnter.configure(command=self.pinchange)
    def pinchange(self):
        self.txtReceipt.delete(1.0, END)
        self.input_box.delete(0, END)
        
        self.btnArrowL1.configure(state=DISABLED)
        self.btnArrowL2.configure(state=DISABLED)
        self.btnArrowL3.configure(state=DISABLED)   
        self.btnArrowL4.configure(state=DISABLED)
        self.btnArrowR1.configure(state=DISABLED)
        self.btnArrowR2.configure(state=DISABLED) 
        self.btnArrowR3.configure(state=DISABLED)
        self.btnArrowR4.configure(state=DISABLED)
        
        self.input_box.configure(state=NORMAL)
        self.numpad_inputbox()
        self.btnEnter.configure(command=self.confirm_pin)
        
        self.txtReceipt.insert(END,'Enter your old pin code first')
        
    # === TRANSFER 
    def transfer_EnterBtn(self):
        transfer_amount = int(self.input_box.get())
        if transfer_amount > 0:
            self.txtReceipt.delete(1.0, END)
            self.input_box.delete(0, END)
            self.txtReceipt.insert(END,'Money inserted:   \n₱ ' + str(transfer_amount))
            self.txtReceipt.insert(END,'\n\nYour money is \nbeing transferred... ')
            self.app.after(6000,self.Clear)
        else: 
            self.txtReceipt.delete(1.0,END)
            self.txtReceipt.insert(END,'Please Enter valid\ninput...')
            self.app.after(4000,self.transfer)
        
    def transfer(self):
        self.txtReceipt.delete(1.0, END)
        self.input_box.delete(0, END)

        self.input_box.configure(state=NORMAL)
        self.numpad_inputbox()
        self.btnEnter.configure(command=self.transfer_EnterBtn)
        
        self.text_file = open('transferPrompt.txt', 'r')
        self.text = self.text_file.read()
        
        self.btnArrowL1.configure(state=DISABLED)
        self.btnArrowL2.configure(state=DISABLED)
        self.btnArrowL3.configure(state=DISABLED)   
        self.btnArrowL4.configure(state=DISABLED)
        self.btnArrowR1.configure(state=DISABLED)
        self.btnArrowR2.configure(state=DISABLED) 
        self.btnArrowR3.configure(state=DISABLED)
        self.btnArrowR4.configure(state=DISABLED)
        
        self.txtReceipt.insert(END, self.text)
        self.text_file.close()
        
    
# ============ MAIN    
if __name__=='__main__':
    root = Tk()
    program = atm(root)
    root.mainloop()