import tkinter 
import tkinter.messagebox as mbox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTPAuthenticationError, SMTPDataError, SMTPException, SMTPHeloError, SMTPNotSupportedError, SMTPRecipientsRefused, SMTPSenderRefused
import webbrowser


def send(window,sender,password,receiver,subject,message):
    
    format = MIMEMultipart()
    format['From'] = sender.get()
    format['To'] = receiver.get()
    format['Subject'] = subject.get()
    format.attach(MIMEText(message,'plain'))
    try:
        session = smtplib.SMTP('smtp.gmail.com',587)
        session.starttls()
        session.login(sender.get(),password.get())
        final_mail = format.as_string()
    except SMTPHeloError:
        tkinter.messagebox.showinfo(title = 'Alert', message = 'The server did not reply properly') 
    except SMTPAuthenticationError:
        tkinter.messagebox.showinfo(title = 'Alert', message = 'The server did not accept the username/ password combination.') 
    except SMTPNotSupportedError:
        tkinter.messagebox.showinfo(title = 'Alert', message = 'The AUTH command is not supported by the server.') 
    except SMTPException:
        tkinter.messagebox.showinfo(title = 'Alert', message = 'No suitable authentication method was found.')
    try:
        reply = session.sendmail(sender.get(),receiver.get(),final_mail)
        session.quit()
        tkinter.messagebox.showinfo(title = 'Alert', message = 'Mail Delivered to {} successfully.'.format(receiver.get()))
    except SMTPHeloError:
        tkinter.messagebox.showinfo(title = 'Alert', message = 'The server did not reply properly') 
    except SMTPRecipientsRefused:
        tkinter.messagebox.showinfo(title = 'Alert', message = 'The server rejected ALL recipients (no mail was sent).')
    except SMTPSenderRefused:
        tkinter.messagebox.showinfo(title = 'Alert', message = 'The server did not accept the from_addr.') 
    except SMTPDataError:
        tkinter.messagebox.showinfo(title = 'Alert', message = 'The server replied with an unexpected error code')
    except SMTPNotSupportedError:
        tkinter.messagebox.showinfo(title = 'Alert', message = 'The mail_options parameter includes SMTPUTF8 but the SMTPUTF8 extension is not supported by the server.')

    sender.set('')
    password.set('')
    receiver.set('')
    subject.set('')
    message.delete('1.0',"end")



window = tkinter.Tk()
window.title('Email Sender')
window.geometry('500x600')
m = '''If you are using this application for the first time. Please enable Less Secure apps by logging into your Gmail account.Please Follow the below New User link to do the same.
Ignore if already a user.'''
# https://www.google.com/settings/security/lesssecureapps

tkinter.messagebox.showinfo(title='Description', message = m)
sender = tkinter.StringVar()
password = tkinter.StringVar()
receiver = tkinter.StringVar()
subject = tkinter.StringVar()


Heading = tkinter.Label(text = 'Email Made Easy ...!',bg="purple",fg="white",font=("consolas", 18))
Heading.grid(row = 0, column = 1,pady =10)

Empty_sapce_1 = tkinter.Label()
Empty_sapce_1.grid(row = 1)
label_sender = tkinter.Label(text = 'Sender mail id', bg = "white", fg = "green")
label_sender.grid(row = 2,column = 0,padx = 10)
entry_sender = tkinter.Entry(window,textvariable =sender,width = 40 )
entry_sender.grid(row = 2, column =  1)


Empty_sapce_5 = tkinter.Label()
Empty_sapce_5.grid(row = 3)
label_sender_pass = tkinter.Label(text = 'Sender Password', bg = "white", fg = "green")
label_sender_pass.grid(row = 4,column = 0,padx = 10)
entry_pass = tkinter.Entry(window,textvariable =password, width = 40,show='*')
entry_pass.grid(row = 4, column =  1)



Empty_sapce_2 = tkinter.Label()
Empty_sapce_2.grid(row = 5)
label_recv = tkinter.Label(text = 'Receiver email id', bg = "white", fg = "green")
label_recv.grid(row = 6,column = 0,padx = 10)
entry_recv = tkinter.Entry(window,textvariable =receiver,width = 40)
entry_recv.grid(row = 6, column =  1)



Empty_sapce_3 = tkinter.Label()
Empty_sapce_3.grid(row = 7)
label_sub = tkinter.Label(text = 'Subject', bg = "white", fg = "green")
label_sub.grid(row = 8,column = 0,padx = 10)
sub_text = tkinter.Entry(window,textvariable =subject, width= 40)
sub_text.grid(row = 8, column =  1)



Empty_sapce_4 = tkinter.Label()
Empty_sapce_4.grid(row = 9)
label_mess = tkinter.Label(text = 'Message', bg = "white", fg = "green")
label_mess.grid(row = 10,column = 0,padx = 10)
mess = tkinter.Text(height = 10, width = 30)
message = mess.get("1.0","end")
mess.grid(row = 10, column = 1)

Empty_sapce_6 = tkinter.Label()
Empty_sapce_6.grid(row = 11)
send_Btn = tkinter.Button(text = 'Send',fg = 'blue', command = lambda: send(window,sender,password,receiver,subject,message))
send_Btn.grid(row = 12,column = 1)

link1 = tkinter.Label( text="New User", fg="blue", cursor="hand2",bg='yellow',font = ('verdana',15))
link1.grid(row = 13,column=0)
link1.bind("<Button-1>", lambda e: webbrowser.open_new('https://www.google.com/settings/security/lesssecureapps'))


window.mainloop()