import tkinter as tk
from tkinter import ttk


# Number button class
class ButtonNum:
    def __init__(self, n: str):
        self.value = n
        self.button = tk.Button(
            buttonframe,
            text=n,
            command=lambda: self.click(),
            font=("Ariala", 18),
            bg="#303131",
            fg="#ffffff",
        )
        window.bind(n, lambda e: self.click())

    # function handling on click event
    def click(self):
        global tmp

        if len(tmp) < 9:
            for i in btnsFun.values():
                i.button.configure(fg="#ffffff", bg="#f69906")

            if label.cget("text") == "0" or label.cget("text") == "Error" or tmp == "":
                label.configure(text=self.value)
            else:
                label.configure(text=label.cget("text") + self.value)

            tmp += self.value
            if tmp[0] == "0":
                tmp = tmp[1:]


# function button class
class ButtonFun:
    def __init__(self, n: str):
        self.value = n
        self.button = tk.Button(
            buttonframe,
            text=n,
            command=lambda: self.click(),
            font=("Ariala", 18),
            bg="#f69906",
            fg="#ffffff",
        )
        window.bind(n, lambda e: self.click())

    # function handling on click event
    def click(self):
        global expression, tmp

        expression += tmp
        tmp = ""

        for i in btnsFun.values():
            i.button.configure(fg="#ffffff", bg="#f69906")

        if expression[-1] in "+-*/=":
            expression = expression[: len(expression) - 1] + self.value
        else:
            expression += self.value

        if "/0" in expression:
            label.configure(text="Error")
        else:
            if float(expression) != 0 and (
                abs(eval(expression[:-1])) > 999999999
                or abs(eval(expression[:-1])) < 0.0000001
            ):
                label.configure(text=f"{eval(expression[:-1]):.3e}")
            else:
                try:
                    label.configure(text=f"{eval(expression[:-1]):.9}")
                except:
                    label.configure(text=eval(expression[:-1]))
        self.button.configure(bg="#ffffff", fg="#f69906")


# function handling event clearing everything
def clearAll():
    global expression, tmp
    expression = ""
    tmp = ""
    label.configure(text="0")
    for i in btnsFun.values():
        i.button.configure(fg="#ffffff", bg="#f69906")


def writePoint():
    global tmp
    if label.cget("text") == "0" or label.cget("text") == "Error" or tmp == "":
        tmp = "0."
        label.configure(text="0.")
    elif not "." in tmp:
        tmp += "."
        label.configure(text=label.cget("text") + ".")


def changeSign():
    global tmp
    if len(tmp) > 0 and tmp != "Error" and tmp != "0":
        tmp = tmp[1:] if tmp[0] == "-" else "-" + tmp
        label.configure(text=tmp)


def getPercentage():
    global tmp
    if len(tmp) > 0 and tmp != "Error" and tmp != "0":
        tmp = "(" + tmp + ")*0.01"
        try:
            label.configure(text=f"{eval(tmp):.9}")
        except:
            label.configure(text=eval(tmp))


def calculate():
    global expression, tmp

    expression += tmp
    tmp = ""

    for i in btnsFun.values():
        i.button.configure(fg="#ffffff", bg="#f69906")

    if expression == "":
        expression = "0"

    if expression[-1] in "+-*/=":
        expression = expression[:-1]
    if "/0" in expression:
        label.configure(text="Error")
    else:
        if float(expression) != 0 and (
            abs(eval(expression)) > 999999999 or abs(eval(expression)) < 0.0000001
        ):
            label.configure(text=f"{eval(expression):.3e}")
        else:
            try:
                label.configure(text=f"{eval(expression):.9}")
            except:
                label.configure(text=eval(expression))
    expression = ""


# seting variables
expression = ""
tmp = ""

# initializing app gui
window = tk.Tk()
window.title("calculator")
window.geometry("370x500+100+100")
window.configure(bg="#000000")

s = ttk.Style()
s.configure("TFrame", background="#000000")

buttonframe = ttk.Frame(window)
buttonframe["padding"] = (10, 10, 10, 10)

label = tk.Label(
    window, text="0", font=("Ariala", 48), fg="white", bg="black", anchor="se"
)

# setting app grid layout
for i in range(7):
    w = 3 if not i % 2 else 1
    buttonframe.columnconfigure(i, weight=w)

for i in range(9):
    w = 3 if not i % 2 else 1
    buttonframe.rowconfigure(i, weight=w)

buttonframe.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)
label.place(relx=0, rely=0, relwidth=0.975, relheight=0.25)

# initializing and positionig buttons
btnsNum = []

for i in range(10):
    btnsNum.append(ButtonNum(str(i)))

for i in range(9):
    btnsNum[i + 1].button.grid(
        row=(8 - i) // 3 * 2 + 2, column=i % 3 * 2, sticky="nswe"
    )

btnsNum[0].button.grid(row=8, column=0, columnspan=3, sticky="nswe")


btnPOI = tk.Button(
    buttonframe,
    text=".",
    command=writePoint,
    font=("Ariala", 18),
    bg="#303131",
    fg="#ffffff",
)
btnPOI.grid(row=8, column=4, sticky="nswe")
window.bind(".", lambda e: writePoint())
window.bind(",", lambda e: writePoint())


btnAC = tk.Button(
    buttonframe, text="AC", command=clearAll, font=("Ariala", 18), bg="#9f9f9f"
)
btnAC.grid(row=0, column=0, sticky="nswe")
window.bind("<BackSpace>", lambda e: clearAll())
window.bind("<Delete>", lambda e: clearAll())

btnPM = tk.Button(
    buttonframe, text="+/-", command=changeSign, font=("Ariala", 18), bg="#9f9f9f"
)
btnPM.grid(row=0, column=2, sticky="nswe")

btnPER = tk.Button(
    buttonframe, text="%", command=getPercentage, font=("Ariala", 18), bg="#9f9f9f"
)
btnPER.grid(row=0, column=4, sticky="nswe")

btnsFun = {}

btnsFun["/"] = ButtonFun("/")
btnsFun["/"].button.grid(row=0, column=6, sticky="nswe")

btnsFun["*"] = ButtonFun("*")
btnsFun["*"].button.grid(row=2, column=6, sticky="nswe")

btnsFun["-"] = ButtonFun("-")
btnsFun["-"].button.grid(row=4, column=6, sticky="nswe")

btnsFun["+"] = ButtonFun("+")
btnsFun["+"].button.grid(row=6, column=6, sticky="nswe")

btnEQU = tk.Button(
    buttonframe,
    text="=",
    command=calculate,
    font=("Ariala", 18),
    bg="#f69906",
    fg="#ffffff",
)
btnEQU.grid(row=8, column=6, sticky="nswe")
window.bind("<Return>", lambda e: calculate())
window.bind("=", lambda e: calculate())

window.mainloop()
