# Comand Line To Do List Application

Tasks = []

def add_task():
    task = input("Ce task doresti sa adaugi?\n")
    Tasks.append(task)

def delete_task():
    taskDel = input("Alege numar corespunzator taskului pe care vrei sa-l stergi.\n")
    Tasks.pop(taskDel)

def afisare_taskuri():
    for t in Tasks:
                print(f"{Tasks.index(t)}. {t}\n")

Variante = {"adaugare", "stergere", "afisare", "inchidere"}

def asteptare_comanda():

    while True:
        raspuns = input("Ce doresti sa faci? \nAdaugare (Task) \nStergere (task) \n Afisare (task) \n Inchidere (aplicatie)")
        while raspuns.lower() not in Variante:
            print("Aceasta varianta nu exista!\n Alege una din cele sugerate.\n")
            raspuns = input("Ce doresti sa faci? \nAdaugare (Task) \nStergere (task) \n Afisare (task) \n Inchidere (aplicatie)")
        
        if raspuns.lower() == "adaugare":
            add_task()
        elif raspuns.lower() == "stergere":
            delete_task()
        elif raspuns.lower() == "afisare":
            afisare_taskuri()
        elif raspuns.lower() == "inchidere":
            break

asteptare_comanda()