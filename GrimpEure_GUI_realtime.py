from tkinter import Label, Entry, Tk
import time
try:  
    def calculs_triple(list_ord):
        for i in range(1, 5):
            if i == 1:triple = [list_ord[0], list_ord[1], list_ord[2]]
            if i == 2:triple = [list_ord[0], list_ord[1], list_ord[3]]
            if i == 3:triple = [list_ord[0], list_ord[2], list_ord[3]]
            if i == 4:triple = [list_ord[1], list_ord[2], list_ord[3]]
            globals()[f"label_triple_{i}"]["text"]=triple
            
            # Plateau A
            globals()[f"label_triple_A_{i}"].config(fg="green")
            try:
                if int(triple[2]) >= 4:
                    globals()[f"label_triple_A_{i}"]["text"]="A"
                else:
                    globals()[f"label_triple_A_{i}"]["text"]=""
            except:
                globals()[f"label_triple_A_{i}"]["text"]=""
                
            # Plateau B
            globals()[f"label_triple_B_{i}"].config(fg="blue")
            try:
                if int(triple[2]) >= 3 and int(triple[1]) >= 2:
                    globals()[f"label_triple_B_{i}"]["text"]="B"
                else:
                    globals()[f"label_triple_B_{i}"]["text"]=""
            except:
                globals()[f"label_triple_B_{i}"]["text"]=""
                 
            # Plateau C
            globals()[f"label_triple_C_{i}"].config(fg="gold")
            try:
                if int(triple[2]) >= 2 and int(triple[0]) >= 2:
                    globals()[f"label_triple_C_{i}"]["text"]="C"
                else:
                    globals()[f"label_triple_C_{i}"]["text"]=""
            except:
                globals()[f"label_triple_C_{i}"]["text"]=""

    def calculs_double(list_ord):
        for i in range(1, 7):
            if i == 1:double = [list_ord[0], list_ord[1]]
            if i == 2:double = [list_ord[0], list_ord[2]]
            if i == 3:double = [list_ord[0], list_ord[3]]
            if i == 4:double = [list_ord[1], list_ord[2]]
            if i == 5:double = [list_ord[1], list_ord[3]]
            if i == 6:double = [list_ord[2], list_ord[3]]
            globals()[f"label_double_{i}"]["text"]=double
            
            # Plateau A
            globals()[f"label_double_A_{i}"].config(fg="green")
            try:
                if int(double[1]) >= 7:
                    globals()[f"label_double_A_{i}"]["text"]="A"
                else:
                    globals()[f"label_double_A_{i}"]["text"]=""
            except:
                globals()[f"label_double_A_{i}"]["text"]=""

            # Plateau B
            globals()[f"label_double_B_{i}"].config(fg="blue")
            try:
                if int(double[0]) >= 2 and int(double[1]) >= 6:
                    globals()[f"label_double_B_{i}"]["text"]="B"
                else:
                    globals()[f"label_double_B_{i}"]["text"]=""
            except:
                globals()[f"label_double_B_{i}"]["text"]=""
            
            # Plateau C
            globals()[f"label_double_C_{i}"].config(fg="gold")
            try:
                if int(double[0]) >= 3 and int(double[1]) >= 5:
                    globals()[f"label_double_C_{i}"]["text"]="C"
                else:
                    globals()[f"label_double_C_{i}"]["text"]=""
            except:
                globals()[f"label_double_C_{i}"]["text"]=""

    def modules():
        if module1 != m1.get():
            module1 = m1.get()
            module2 = m2.get()
            module3 = m3.get()
            module4 = m4.get()

            try:
                module1 = int(module1)
                if module1 > 11:
                    module1 = "x"
                    m1.config(bg="red")
                else:m1.config(bg="white")
            except ValueError:
                module1 = "x"
                if m1.get() != "":m1.config(bg="red")
                else:m1.config(bg="white")
            try:
                module2 = int(module2)
                if module2 > 11:
                    module2 = "x"
                    m2.config(bg="red")
                else:m2.config(bg="white")
            except ValueError:
                module2 = "x"
                if m2.get() != "":m2.config(bg="red")
                else:m2.config(bg="white")
            try:
                module3 = int(module3)
                if module3 > 11:
                    module3 = "x"
                    m3.config(bg="red")
                else:m3.config(bg="white")
            except ValueError:
                module3 = "x"
                if m3.get() != "":m3.config(bg="red")
                else:m3.config(bg="white")
            try:
                module4 = int(module4)
                if module4 > 11:
                    module4 = "x"
                    m4.config(bg="red")
                else:m4.config(bg="white")
            except ValueError:
                module4 = "x"
                if m4.get() != "":m4.config(bg="red")
                else:m4.config(bg="white")

            list_ord = sorted([module1, module2, module3, module4], key = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, "x"].index)
            ord["text"] = list_ord   

            calculs_triple(list_ord)
            calculs_double(list_ord)
        else:
            None

    app = Tk()
    app.config(padx=10,pady=10)
    app.title("Modules Baby Grimp'Eure")
    app.resizable(0, 0)

    Label(app, text="Modules Choisis :", font="Helvetica 10 underline").grid(column=0, row=0,padx=(0,10))
    l = Label(app)
    l.grid(row=2)
    l.config(height=1)
    Label(app, text="Plateaux Triple :", font="Helvetica 10 underline").grid(column=0, row=3)
    l = Label(app)
    l.grid(row=9)
    l.config(height=1)
    Label(app, text="Plateaux Double :", font="Helvetica 10 underline").grid(column=0, row=10)
    m1 = Entry(app)
    m1.grid(column=1, row=0)
    m2 = Entry(app)
    m2.grid(column=2, row=0)
    m3 = Entry(app)
    m3.grid(column=3, row=0)
    m4 = Entry(app)
    m4.grid(column=4, row=0)
    
    # Create all dynamic variables/labels
    ord = Label(app)
    ord.grid(row=1)       
    
    module1 = m1.get()
    module2 = m2.get()
    module3 = m3.get()
    module4 = m4.get()
            
    for i in range(1,5):
        globals()[f"label_triple_{i}"] = Label(app)
        globals()[f"label_triple_{i}"].grid(column=1, row=2 + i)
        for n in range(1,4):
            if n == 1: abc = "A"
            if n == 2: abc = "B"
            if n == 3: abc = "C"
            globals()[f"label_triple_{abc}_{i}"] = Label(app)
            globals()[f"label_triple_{abc}_{i}"].grid(column=1 + n, row=2 + i)
            
    for i in range(1,7):
        globals()[f"label_double_{i}"] = Label(app)
        globals()[f"label_double_{i}"].grid(column=1, row=9 + i)
        for n in range(1,4):
            if n == 1: abc = "A"
            if n == 2: abc = "B"
            if n == 3: abc = "C"
            globals()[f"label_double_{abc}_{i}"] = Label(app)
            globals()[f"label_double_{abc}_{i}"].grid(column=1 + n, row=9 + i)
    
    # Updating continuously
    while True:
        app.update()
        if module1 != m1.get():
            modules()
    
except:
    app.update()