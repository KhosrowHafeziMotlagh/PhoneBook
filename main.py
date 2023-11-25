"""
Programmer : Khosrow Hafezi Motlagh
Program Name :Phonebook
Ver : 0.0.1
"""

import sys
import tkinter
from tkinter import *
from tkinter import messagebox
import db_connction as dbc
import positioning
import time

label_bg = "#00FF00"
label_fg = "black"
label_internal_padding = 5

btn_font = "arial"
btn_size_font = 18
btn_backgroand_color = "gray"

entry_font = "arial"
entry_lock_backgroand_color = "black"

entry_size_font = 18
entry_color_font = "#000099"
entry_border = 7
c_time = time.localtime()


def start():
    dbc.start_connction()
    start_form = Tk()

    contact_id = StringVar()
    contact_name = StringVar()
    contact_family = StringVar()
    contact_phone = StringVar()
    contact_email = StringVar()
    contact_telegramId = StringVar()

    contact_update_id = StringVar()
    contact_update_name = StringVar()
    contact_update_family = StringVar()
    contact_update_phone = StringVar()
    contact_update_email = StringVar()
    contact_update_telegramId = StringVar()

    contact_delete_id = StringVar()
    contact_delete_name = StringVar()
    contact_delete_family = StringVar()
    contact_delete_phone = StringVar()
    contact_delete_email = StringVar()
    contact_delete_telegramId = StringVar()

    contact_id.set(str(dbc.get_id()))

    start_form.title("PhoneBook 0.0.1")
    start_form.config(bg="#333333")

    lable_programmer = Label(start_form, text="By Khosrow Hafezi Motlagh", bg="black", fg="lime", bd=entry_border,
                             font=(entry_size_font)).grid(row=0, columnspan=6)

    lable_status = Label(start_form, text="Status", bg="black", fg="white", bd=entry_border,
                         font=(entry_size_font))
    lable_status.grid(row=0, column=5, sticky="e")

    label_contact_id = Label(start_form, text='ID:', bg=label_bg, fg=label_fg).grid(row=1, column=0, ipadx=15)
    entry_contact_id = Entry(start_form, bg="silver", fg=entry_color_font, textvariable=contact_id,
                             font=(entry_font, entry_size_font),
                             bd=entry_border).grid(row=1, column=1)

    label_contact_name = Label(start_form, text='Name:', bg=label_bg, fg=label_fg).grid(row=1, column=2,
                                                                                        ipadx=label_internal_padding)
    entry_contact_name = (Entry(start_form, textvariable=contact_name, bg="silver", fg=entry_color_font,
                                font=(entry_font, entry_size_font),
                                bd=entry_border))
    entry_contact_name.grid(row=1, column=3)

    label_contact_familyName = Label(start_form, text='*Family:', bg=label_bg, fg=label_fg).grid(row=1, column=4,
                                                                                                 ipadx=label_internal_padding)
    entry_contact_familyName = Entry(start_form, textvariable=contact_family, bg="silver", fg=entry_color_font,
                                     font=(entry_font, entry_size_font), bd=entry_border).grid(row=1, column=5)

    label_contact_phone = Label(start_form, text='*Phone:', bg=label_bg, fg=label_fg).grid(row=2, column=0, padx=5,
                                                                                           ipadx=label_internal_padding)
    entry_contact_phone = Entry(start_form, textvariable=contact_phone, bg="silver", fg=entry_color_font,
                                font=(entry_font, entry_size_font), bd=entry_border).grid(row=2,
                                                                                          column=1)

    label_contact_email = Label(start_form, text='Email:', bg=label_bg, fg=label_fg).grid(row=2, column=2,
                                                                                          ipadx=label_internal_padding)
    entry_contact_email = Entry(start_form, textvariable=contact_email, bg="silver", fg=entry_color_font,
                                font=(entry_font, entry_size_font),
                                bd=entry_border).grid(row=2, column=3)

    label_contact_telegramID = Label(start_form, text='Tg Id:', bg=label_bg, fg=label_fg).grid(row=2, column=4,
                                                                                               ipadx=label_internal_padding)
    entry_contact_telegramID = Entry(start_form, textvariable=contact_telegramId, bg="silver", fg=entry_color_font,
                                     font=(entry_font, entry_size_font),
                                     bd=entry_border).grid(row=2, column=5)

    btn_add = Button(start_form, text="Add New", bg=btn_backgroand_color, bd=entry_border,
                     highlightbackground="lime", highlightthickness=2,
                     command=lambda: insert()).grid(row=5, column=1)
    btn_update = Button(start_form, text=" Update ", bg=btn_backgroand_color, bd=entry_border,
                        highlightbackground="lime", highlightthickness=2,
                        command=lambda: update()).grid(row=5, column=2)
    btn_search = Button(start_form, text=" Search ", bg=btn_backgroand_color, bd=entry_border,
                        highlightbackground="lime", highlightthickness=2,
                        command=lambda: search()).grid(row=5, column=3,
                                                       pady=3)
    btn_delete = Button(start_form, text="  Delete  ", bg=btn_backgroand_color, bd=entry_border,
                        highlightbackground="lime", highlightthickness=2,
                        command=lambda: delete()).grid(row=5, column=4)
    btn_close = Button(start_form, text="Exit", bg="red", bd=entry_border,
                       highlightbackground="lime", highlightthickness=2, command=sys.exit).grid(row=5,
                                                                                                column=5)

    def clear_entry(contact_name, contact_family, contact_phone, contact_email, contact_telegramId):
        contact_name.set('')
        contact_family.set('')
        contact_phone.set('')
        contact_email.set('')
        contact_telegramId.set('')

    def insert():
        c_name = contact_name.get().strip()
        if len(contact_family.get().strip()) != 0:
            c_family = contact_family.get().strip()
            if len(contact_phone.get().strip()) != 0:
                try:
                    assert contact_phone.get().strip().isnumeric() == True
                except:
                    msg = messagebox.showerror("Error", "<Phone> must be Numeral")
                    return
                c_phone = contact_phone.get().strip()
                c_email = contact_email.get().strip()
                c_telegramId = contact_telegramId.get().strip()
                dbc.insert_new_contact(c_name, c_family, c_phone, c_email, c_telegramId)
                contact_id.set(str(dbc.get_id()))
                lable_status.config(fg="lime", text="Saved")
                clear_entry(contact_name, contact_family, contact_phone, contact_email, contact_telegramId)
                entry_contact_name.focus()
            else:
                msg = messagebox.showerror("Error", "<Phone> is empty")
                return
        else:
            msg = messagebox.showerror("Error", "<Family> is empty")
            return

    def search():

        if len(contact_family.get().strip()) == 0 and len(contact_phone.get().strip()) == 0:
            msg = messagebox.showerror("Error", "Please fill just the <Family> or just the <Phone>")
        else:
            serach_form = Tk()
            serach_form.title("Search Form")
            datas = dbc.select_all_database(contact_family.get().strip(), contact_phone.get().strip())
            header = ['Id', 'Name', 'Family', 'Phone', 'Email', 'Telegram ID']

            try:
                assert datas != '' and datas != None and len(datas) != 0
                datas.insert(0, header)
                i = 0
                for row in datas:
                    for j in range(len(row)):
                        e = Listbox(serach_form, fg='blue', bg="white", height=1)
                        e.grid(row=i, column=j)
                        e.insert(END, row[j])
                    i = i + 1
            except:
                label_noResult = Label(serach_form, text="No Result", fg='red', bg="white", font=(50)).grid(row=0,
                                                                                                            column=0)
            serach_form.mainloop()

    def update():
        update_form = Toplevel(start_form)
        update_form.title("Upadate Form")

        lable_update_status = Label(update_form, text="Status", bg="black", fg="white", bd=entry_border,
                                    font=(entry_size_font))
        lable_update_status.grid(row=0, column=5, sticky="e")

        label_contact_update_id = Label(update_form, text='ID:', bg=label_bg, fg=label_fg).grid(row=1, column=0,
                                                                                                ipadx=15)
        entry_contact_update_id = (Entry(update_form, bg="yellow", fg=entry_color_font, textvariable=contact_update_id,
                                         font=(entry_font, entry_size_font),
                                         bd=entry_border))
        entry_contact_update_id.grid(row=1, column=1)

        label_contact_update_name = Label(update_form, text='Name:', bg=label_bg, fg=label_fg).grid(row=1, column=2,
                                                                                                    ipadx=label_internal_padding)
        entry_contact_update_name = Entry(update_form, textvariable=contact_update_name, bg="silver",
                                          fg=entry_color_font, font=(entry_font, entry_size_font),
                                          bd=entry_border)
        entry_contact_update_name.grid(row=1, column=3)

        label_contact_update_familyName = Label(update_form, text='*Family:', bg=label_bg, fg=label_fg).grid(row=1,
                                                                                                             column=4,
                                                                                                             ipadx=label_internal_padding)
        entry_contact_update_familyName = Entry(update_form, textvariable=contact_update_family, bg="silver",
                                                fg=entry_color_font, font=(entry_font, entry_size_font),
                                                bd=entry_border)
        entry_contact_update_familyName.grid(row=1, column=5)

        label_contact_update_phone = Label(update_form, text='*Phone:', bg=label_bg, fg=label_fg).grid(row=2, column=0,
                                                                                                       padx=5,
                                                                                                       ipadx=label_internal_padding)
        entry_contact_update_phone = (
            Entry(update_form, textvariable=contact_update_phone, bg="silver", fg=entry_color_font,
                  font=(entry_font, entry_size_font), bd=entry_border))
        entry_contact_update_phone.grid(row=2, column=1)

        label_contact_update_email = Label(update_form, text='Email:', bg=label_bg, fg=label_fg).grid(row=2, column=2,
                                                                                                      ipadx=label_internal_padding)
        entry_contact_update_email = Entry(update_form, textvariable=contact_update_email, bg="silver",
                                           fg=entry_color_font, font=(entry_font, entry_size_font), bd=entry_border)
        entry_contact_update_email.grid(row=2, column=3)

        label_contact_update_telegramID = Label(update_form, text='Tg Id:', bg=label_bg, fg=label_fg).grid(row=2,
                                                                                                           column=4,
                                                                                                           ipadx=label_internal_padding)
        entry_contact_update_telegramID = Entry(update_form, textvariable=contact_update_telegramId, bg="silver",
                                                fg=entry_color_font, font=(entry_font, entry_size_font),
                                                bd=entry_border)
        entry_contact_update_telegramID.grid(row=2, column=5)

        btn_load = Button(update_form, text="Load ID", bg=btn_backgroand_color, bd=entry_border,
                          highlightbackground="lime", highlightthickness=2,
                          command=lambda: load()).grid(row=3, column=1)
        btn_update = Button(update_form, text=" Update ", bg=btn_backgroand_color, bd=entry_border,
                            command=lambda: update_contact_info())
        btn_update.grid(row=3, column=3)
        btn_close = (Button(update_form, text="Close", bg="red", bd=entry_border, command=update_form.destroy))
        btn_close.grid(row=3, column=5)

        btn_update.config(state=DISABLED)
        entry_contact_update_id.config(bg="#fffacd")
        entry_contact_update_name.config(state=DISABLED)
        entry_contact_update_familyName.config(state=DISABLED)
        entry_contact_update_email.config(state=DISABLED)
        entry_contact_update_telegramID.config(state=DISABLED)

        def load():
            try:
                int(contact_update_id.get().strip())
                datas = dbc.select_person_bye_id(int(contact_update_id.get().strip()))
                try:
                    assert datas != None
                    assert datas != ''
                    assert len(datas) != 0
                    contact_update_name.set(datas[1])
                    contact_update_family.set(datas[2])
                    contact_update_phone.set(datas[3])
                    contact_update_email.set(datas[4])
                    contact_update_telegramId.set(datas[5])

                except:
                    msg = messagebox.showerror("Error", "No item found")
                    return
                btn_update.config(state=NORMAL, highlightbackground="lime", highlightthickness=2)
                entry_contact_update_name.config(state=NORMAL, highlightbackground="lime", highlightthickness=2)
                entry_contact_update_familyName.config(state=NORMAL, highlightbackground="lime", highlightthickness=2)
                entry_contact_update_phone.config(state=NORMAL, highlightbackground="lime", highlightthickness=2)
                entry_contact_update_email.config(state=NORMAL, highlightbackground="lime", highlightthickness=2)
                entry_contact_update_telegramID.config(state=NORMAL, highlightbackground="lime", highlightthickness=2)
                lable_update_status.config(text="Loaded", fg="lime")

            except:
                msg = messagebox.showerror("Error", "Please fill the <ID> with Number")
                return

        def update_contact_info():
            dbc.update_contact(contact_update_id.get(), contact_update_name.get(), contact_update_family.get().strip(),
                               contact_update_phone.get().strip(), contact_update_email.get().strip(),
                               contact_update_telegramId.get().strip())
            lable_update_status.config(text="Updated", fg="lime")
            clear_entry(contact_update_name, contact_update_family, contact_update_phone,
                        contact_update_email, contact_update_telegramId)

            entry_contact_update_name.config(state=NORMAL, highlightbackground="gray", highlightthickness=2)
            entry_contact_update_familyName.config(state=NORMAL, highlightbackground="gray", highlightthickness=2)
            entry_contact_update_phone.config(state=NORMAL, highlightbackground="gray", highlightthickness=2)
            entry_contact_update_email.config(state=NORMAL, highlightbackground="gray", highlightthickness=2)
            entry_contact_update_telegramID.config(state=NORMAL, highlightbackground="gray", highlightthickness=2)
            btn_update.config(state=NORMAL, highlightbackground="gray", highlightthickness=2)

            btn_update.config(state=DISABLED)
            entry_contact_update_name.config(state=DISABLED)
            entry_contact_update_familyName.config(state=DISABLED)
            entry_contact_update_phone.config(state=DISABLED)
            entry_contact_update_email.config(state=DISABLED)

        update_form.mainloop()

    def delete():
        delete_form = Toplevel(start_form)
        delete_form.title("Delete Form")

        lable_delete_status = Label(delete_form, text="Status", bg="black", fg="white", bd=entry_border,
                                    font=(entry_size_font))
        lable_delete_status.grid(row=0, column=5, sticky="e")

        label_contact_delete_id = Label(delete_form, text='ID:', bg=label_bg, fg=label_fg).grid(row=1, column=0,
                                                                                                ipadx=15)
        entry_contact_delete_id = (Entry(delete_form, bg="silver", fg=entry_color_font, textvariable=contact_delete_id,
                                         font=(entry_font, entry_size_font),
                                         bd=entry_border))
        entry_contact_delete_id.grid(row=1, column=1)

        label_contact_delete_name = Label(delete_form, text='Name:', bg=label_bg, fg=label_fg).grid(row=1, column=2,
                                                                                                    ipadx=label_internal_padding)
        entry_contact_delete_name = (
            Entry(delete_form, textvariable=contact_delete_name, bg="silver", fg=entry_color_font,
                  font=(entry_font, entry_size_font),
                  bd=entry_border))
        entry_contact_delete_name.grid(row=1, column=3)

        label_contact_delete_familyName = Label(delete_form, text='*Family:', bg=label_bg, fg=label_fg).grid(row=1,
                                                                                                             column=4,
                                                                                                             ipadx=label_internal_padding)
        entry_contact_delete_familyName = (Entry(delete_form, textvariable=contact_delete_family, bg="silver",
                                                 fg=entry_color_font,
                                                 font=(entry_font, entry_size_font), bd=entry_border))
        entry_contact_delete_familyName.grid(row=1,
                                             column=5)

        label_contact_delete_phone = Label(delete_form, text='*Phone:', bg=label_bg, fg=label_fg).grid(row=2, column=0,
                                                                                                       padx=5,
                                                                                                       ipadx=label_internal_padding)
        entry_contact_delete_phone = (Entry(delete_form, textvariable=contact_delete_phone, bg="silver",
                                            fg=entry_color_font,
                                            font=(entry_font, entry_size_font), bd=entry_border))
        entry_contact_delete_phone.grid(row=2,
                                        column=1)

        label_contact_delete_email = Label(delete_form, text='Email:', bg=label_bg, fg=label_fg).grid(row=2, column=2,
                                                                                                      ipadx=label_internal_padding)
        entry_contact_delete_email = Entry(delete_form, textvariable=contact_delete_email, bg="silver",
                                           fg=entry_color_font,
                                           font=(entry_font, entry_size_font),
                                           bd=entry_border)
        entry_contact_delete_email.grid(row=2, column=3)

        label_contact_delete_telegramID = Label(delete_form, text='Tg Id:', bg=label_bg, fg=label_fg).grid(row=2,
                                                                                                           column=4,
                                                                                                           ipadx=label_internal_padding)
        entry_contact_delete_telegramID = Entry(delete_form, textvariable=contact_delete_telegramId, bg="silver",
                                                fg=entry_color_font, font=(entry_font, entry_size_font)
                                                , bd=entry_border)
        entry_contact_delete_telegramID.grid(row=2, column=5)

        btn_load = Button(delete_form, text="Load ID", bg=btn_backgroand_color, bd=entry_border,
                          command=lambda: load())
        btn_load.grid(row=3, column=1)
        btn_delete = (Button(delete_form, text=" Delete ", bg="gray", bd=entry_border,
                             command=lambda: delete_contact_info(), state=DISABLED))
        btn_delete.grid(row=3, column=3)
        btn_close = Button(delete_form, text="Close", bg="red", bd=entry_border, command=delete_form.destroy)
        btn_close.grid(row=3, column=5)

        btn_load.config(highlightbackground="lime", highlightthickness=2)
        entry_contact_delete_name.config(state=DISABLED)
        entry_contact_delete_familyName.config(state=DISABLED)
        entry_contact_delete_phone.config(state=DISABLED)
        entry_contact_delete_email.config(state=DISABLED)
        entry_contact_delete_telegramID.config(state=DISABLED)

        def load():
            try:
                int(contact_delete_id.get().strip())
                btn_delete.config(state=NORMAL)
            except:
                msg = messagebox.showerror("Error", "Please fill the <ID> with Number")
                return
            datas = dbc.select_person_bye_id(int(contact_delete_id.get().strip()))
            contact_delete_name.set(datas[1])
            contact_delete_family.set(datas[2])
            contact_delete_phone.set(datas[3])
            contact_delete_email.set(datas[4])
            contact_delete_telegramId.set(datas[5])
            btn_delete.config(state=NORMAL, highlightbackground="lime", highlightthickness=2)
            lable_delete_status.config(text="Loaded", fg="lime")

        def delete_contact_info():
            dbc.delete_contact(int(contact_delete_id.get()))
            lable_delete_status.config(text="Deleted", fg="lime")
            clear_entry(contact_delete_name, contact_delete_family, contact_delete_phone,
                        contact_delete_email, contact_delete_telegramId)
            btn_delete.config(state=NORMAL, highlightbackground="gray", highlightthickness=2)
            btn_delete.config(state=DISABLED)
            lable_delete_status.config(text="Deleted", fg="lime")

    positioning.centeralize_window(start_form)
    start_form.mainloop()


if __name__ == "__main__":
    start()
