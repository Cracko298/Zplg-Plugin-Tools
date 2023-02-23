from time import sleep
from os import system
from os import path

check_win = path.exists("C:\Windows\SysWOW64")
if check_win == True:
  clear = 'cls'
else:
  clear = 'clear'

plugin = input(".Zplg Plugin Name: ")

with open(plugin, 'r') as file0:
  creator_bytes = file0.readline().rstrip()
  rand0 = file0.readline().rstrip()
  seek_bytes = file0.readline().rstrip()
  rand1 = file0.readline().rstrip()
  min_bytes = file0.readline().rstrip()
  max_bytes = file0.readline().rstrip()
  rand2 = file0.readline().rstrip()
  new_val_bytes = file0.readline().rstrip()
  rand3 = file0.readline().rstrip()
  note_bytes = file0.readline().rstrip()

  output_str0 = ''.join(c for c in creator_bytes if c.isprintable())
  output_str1 = ''.join(c for c in seek_bytes if c.isprintable())
  output_str2 = ''.join(c for c in min_bytes if c.isprintable())
  output_str3 = ''.join(c for c in max_bytes if c.isprintable())
  output_str4 = ''.join(c for c in new_val_bytes if c.isprintable())
  output_str5 = ''.join(c for c in note_bytes if c.isprintable())

  if "CREATOR " in output_str0:
    o0 = output_str0.replace("CREATOR ", "")
    
  if "SEEK " in output_str1:
    o1 = output_str1.replace("SEEK ","")
    
  if "CRASH_VALUE_MIN" in output_str2:
    o2 = output_str2.replace("CRASH_VALUE_MIN","")
    
  if "CRASH_VALUE_MAX" in output_str3:
    o3 = output_str3.replace("CRASH_VALUE_MAX","")
    
  if "NEW_VALUE " in output_str4:
    o4 = output_str4.replace("NEW_VALUE ","")
    
  if "NOTE = " in output_str5:
    o5 = output_str5.replace("NOTE = ","")

  print("Loading Plugin Details.")
  print("#----------------]")
  sleep(0.05)
  system(clear)

  print("Loading Plugin Details.")
  print("[##--------------]")
  sleep(0.05)
  system(clear)

  print("Loading Plugin Details.")
  print("[###-------------]")
  sleep(0.05)
  system(clear)

  print("Loading Plugin Details.")
  print("[####------------]")
  sleep(0.05)
  system(clear)

  print("Loading Plugin Details.")
  print("[#####-----------]")
  sleep(0.05)
  system(clear)

  print("Loading Plugin Details.")
  print("[######----------]")
  sleep(0.05)
  system(clear)

  print("Loading Plugin Details.")
  print("[#######---------]")
  sleep(0.05)
  system(clear)

  print("Loading Plugin Details.")
  print("[########--------]")
  sleep(0.05)
  system(clear)

  print("Loading Plugin Details.")
  print("[#########-------]")
  sleep(0.05)
  system(clear)

  print("Loading Plugin Details.")
  print("[##########------]")
  sleep(0.05)
  system(clear)

  print("Loading Plugin Details.")
  print("[###########-----]")
  sleep(0.05)
  system(clear)

  print("Loading Plugin Details.")
  print("[############----]")
  sleep(0.05)
  system(clear)

  print("Loading Plugin Details.")
  print("[#############---]")
  sleep(0.05)
  system(clear)

  print("Loading Plugin Details.")
  print("[##############--]")
  sleep(0.05)
  system(clear)

  print("Loading Plugin Details.")
  print("[###############-]")
  sleep(0.05)
  system(clear)

  print("Loading Plugin Details.")
  print("[################]")
  sleep(0.05)
  system(clear)
    

  print(f"Creator Name: {o0}.")
  print(" ")
  sleep(0.025)
  print(f"Search Value: {o1}.")
  print(f"Set To Value: {o4}.")
  print(" ")
  sleep(0.025)
  print(f"Minimum Value: {o2}.")
  print(f"Maximum Value: {o3}.")
  print(" ")
  sleep(0.025)
  print(f"Message String: {o5}.")
  print(" ")
  with open("Output.txt",'w+') as bin:
    bin.write(f"Creator Name: {o0}\n")
    bin.write("\n")
    bin.write(f"Search Value: {o1}\n")
    bin.write(f"Set To Value: {o4}\n")
    bin.write("\n")
    bin.write(f"Minimum Value: {o2}\n")
    bin.write(f"Maximum Value: {o3}\n")
    bin.write("\n")
    bin.write(f"Message String: {o5}\n")
  sleep(7.5)