import random
def kuma(a):
  v_dialog =["Neepadicha school la nan headmaster da","I am waiting", "vanakkamngana", "all aera la ayya gilli da"]
  S_dialog =["Its a great six", "master blaster way 4", "clean drive","pure cricketing shot"]
  dialog1=random.choices(v_dialog)
  dialog2=random.choices(S_dialog)
  if a=="sachin":
    print(dialog2)
    return "Cricket player"
  elif a=="vijay":
    print(dialog1)
    return "flim Actor"
  if a!="vijay" and "sachin":
    c=input("Master or Blaster\n")
    if c=="Master":
      return "Actor "
    elif c=="Blaster":
      return"Cricketer"
    else:
      return "my bad"
        
b="1"
while b=="1":
 print("______________")
 a = input ("\nvijay or sachin:\n")
 print(kuma(a))
 print("--------------\n")
 b = input ("type '1' to   continue\n\n" )