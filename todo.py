todo_list=[]

def add_list():
    item=input("enter a new task:").strip()
    todo_list.append(item)
    print(f"{item} added to the to do list")
def display_list():
    if not todo_list:
       print("to do list is empty")
       return
    print("______")
    print("to do list")
    for index,item in enumerate(todo_list,start=1):
      print(f"{index}-{item}")
def remove_list():
    display_list()
    try:
       index=int(input("enter your item number to remove:"))-1

       if 0<=index < len(todo_list):
         removed_item=todo_list.pop(index)
         print(f"{removed_item} removed from list")
       else:
        print("invalid input")
    except ValueError:
        print("please enter a valid number")
while True:
    print("to do list app")
    print("1. add to list")
    print("2.display list")
    print("3.remove from list")
    print("4.exit")

    option=input("select your option")

    if option=='1':
        add_list()
    elif option=='2':
        display_list()
    elif option=='3':
        remove_list()
    elif option=='4':
        print("good bye")
        break
    else:
        print("invalid option")
        break