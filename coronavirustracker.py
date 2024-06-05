from bs4 import BeautifulSoup
import requests
import plyer
from tkinter import *
from tkinter import messagebox, filedialog
import pandas as pd
import os

def notification(title, message):
    icon_path = 'corona.ico'
    if os.path.exists(icon_path):
        plyer.notification.notify(
            title=title,
            message=message,
            app_icon=icon_path,
            timeout=15
        )
    else:
        plyer.notification.notify(
            title=title,
            message=message,
            timeout=15
        )

def format_number(number_str):
    try:
        number = int(number_str.replace(',', '').replace('+', ''))
        return "{:,}".format(number)
    except ValueError:
        return number_str

def datacollected():
    url = "https://www.worldometers.info/coronavirus/"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    tbody = soup.find('tbody')
    abc = tbody.find_all('tr')
    countrynotification = cntdata.get().strip().lower()

    if countrynotification == "":
        countrynotification = "world"

    data = []
    for i in abc:
        id = i.find_all('td')
        country = id[1].text.strip().lower()
        if country == countrynotification:
            totalcases1 = format_number(id[2].text.strip())
            totaldeath = format_number(id[4].text.strip())
            newcases = format_number(id[3].text.strip())
            newdeaths = format_number(id[5].text.strip())
            notification(
                "CORONA RECENT UPDATES {}".format(countrynotification.capitalize()),
                "Total Cases: {}\nTotal Deaths: {}\nNew Cases: {}\nNew Deaths: {}".format(
                    totalcases1, totaldeath, newcases, newdeaths
                )
            )
            display_result(countrynotification.capitalize(), totalcases1, totaldeath, newcases, newdeaths)
        data.append({
            "country": country.capitalize(),
            "total_cases": format_number(id[2].text.strip()),
            "total_deaths": format_number(id[4].text.strip()),
            "new_cases": format_number(id[3].text.strip()),
            "new_deaths": format_number(id[5].text.strip())
        })

    dataframe = pd.DataFrame(data)
    sorts = dataframe.sort_values('total_cases', ascending=False)
    save_files(sorts)

def save_files(dataframe):
    global path
    for a in flist:
        try:
            if a == 'html':
                path2 = os.path.join(path, 'coronadata.html')
                dataframe.to_html(path2, index=False)
                print(f"Saved HTML to {path2}")

            elif a == 'json':
                path2 = os.path.join(path, 'coronadata.json')
                dataframe.to_json(path2, orient='records')
                print(f"Saved JSON to {path2}")

            elif a == 'excel':
                path2 = os.path.join(path, 'coronadata.xlsx')
                dataframe.to_excel(path2, index=False)
                print(f"Saved Excel to {path2}")
        except Exception as e:
            print(f"Error saving {a} file: {e}")

    
    if len(flist) != 0:
        messagebox.showinfo("Notification", f"Corona Record is saved at {path}", parent=coro)
    else:
        print("No file format selected for saving.")

def display_result(country, total_cases, total_deaths, new_cases, new_deaths):
    for widget in result_frame.winfo_children():
        widget.destroy()
    
    result_label = Label(result_frame, text=f"Results for {country}\n\nTotal Cases: {total_cases}\nTotal Deaths: {total_deaths}\nNew Cases: {new_cases}\nNew Deaths: {new_deaths}",
                         font=("arial", 12, "bold"), bg="black", fg="white", justify=LEFT)
    result_label.pack()

    alpha = 0.0
    while alpha <= 1.0:
        result_frame.attributes('-alpha', alpha)
        result_frame.update()
        result_frame.after(50)
        alpha += 0.05

def downloaddata():
    global path
    if len(flist) != 0:
        path = filedialog.askdirectory()
        if path:
            print(f"Selected path: {path}")
            datacollected()
            path = os.path.join(path, 'Corona_Record')  # Update the path to include a folder name
            os.makedirs(path, exist_ok=True)  # Create the folder if it doesn't exist
            save_files(path)
        else:
            messagebox.showerror("Error", "No directory selected")
        flist.clear()
        Inhtml.configure(state='normal')
        Injson.configure(state='normal')
        Inexcel.configure(state='normal')  # Enable all format buttons after clearing the list
    else:
        messagebox.showerror("Error", "Please select at least one file format")

def inhtmldownload():
    flist.append('html')
    Inhtml.configure(state='disabled')

def injsondownload():
    flist.append('json')
    Injson.configure(state='disabled')

def inexceldownload():
    flist.append('excel')
    Inexcel.configure(state='disabled')

coro = Tk()
coro.title("Corona Virus Information")
coro.geometry('800x700+200+100')
coro.configure(bg='#046173')
flist = []
path = ''

try:
    coro.iconbitmap('corona.ico')
except Exception as e:
    print(f"Error: {e}")

mainlabel = Label(coro, text="Corona Virus Live Tracker", font=("new roman", 30, "italic bold"), bg="#05897A", width=33, fg="black", bd=5)
mainlabel.place(relx=0.5, y=50, anchor=CENTER)

label1 = Label(coro, text="Country name", font=("arial", 30, "italic bold"), bg="#046713", fg="white")
label1.place(x=15, y=100)

label2 = Label(coro, text="Download file in", font=("arial", 20, "italic bold"), bg="#046713", fg="white")
label2.place(x=15, y=200)

cntdata = StringVar()
entry1 = Entry(coro, textvariable=cntdata, font=("arial", 20, "italic bold"), relief=RIDGE, bd=2, width=32)
entry1.place(x=400, y=100)

Inhtml = Button(coro, text="Html", bg='#2DAE9A', font=("arial", 15, "italic bold"), relief=RIDGE, activebackground="#059458",
                activeforeground="white", bd=5, width=5, command=inhtmldownload)
Inhtml.place(x=300, y=200)

Injson = Button(coro, text="json", bg='#2DAE9A', font=("arial", 15, "italic bold"), relief=RIDGE, activebackground="#05945B", 
                activeforeground="white", bd=5, width=5, command=injsondownload)
Injson.place(x=300, y=260)

Inexcel = Button(coro, text="excel", bg='#2DAE9A', font=("arial", 15, "italic bold"), relief=RIDGE, activebackground="#05945B", 
                 activeforeground="white", bd=5, width=5, command=inexceldownload)
Inexcel.place(x=300, y=320)

Submit = Button(coro, text="submit", bg='red', font=("arial", 15, "italic bold"), relief=RIDGE, activebackground="#8B0000", 
                activeforeground="white", bd=5, width=25, command=downloaddata)
Submit.place(x=450, y=260)

result_frame = Frame(coro, bg="black", bd=10, relief=RIDGE)
result_frame.place(x=50, y=370, width=700, height=150)

coro.mainloop()