import tkinter as tk
import subprocess

def create_ssh_tunnel(local_port, remote_port, remote_ip, key_file, dynamic):
  if dynamic:
    command = "ssh -i {} -D {} -N".format(key_file, local_port)
  else:
    command = "ssh -i {} -R {}:{}:{} -N".format(key_file, remote_port, remote_ip, local_port)
  subprocess.call(command.split())

def submit():
  local_port = local_port_entry.get()
  remote_port = remote_port_entry.get()
  remote_ip = remote_ip_entry.get()
  key_file = key_file_entry.get()
  dynamic = dynamic_checkbox.get()

  create_ssh_tunnel(local_port, remote_port, remote_ip, key_file, dynamic)

root = tk.Tk()
root.title("Tunnel SSH")

local_port_label = tk.Label(root, text="Port local:")
local_port_label.grid(row=0, column=0)
local_port_entry = tk.Entry(root)
local_port_entry.grid(row=0, column=1)

remote_port_label = tk.Label(root, text="Port de destination:")
remote_port_label.grid(row=1, column=0)
remote_port_entry = tk.Entry(root)
remote_port_entry.grid(row=1, column=1)

remote_ip_label = tk.Label(root, text="Adresse IP de destination:")
remote_ip_label.grid(row=2, column=0)
remote_ip_entry = tk.Entry(root)
remote_ip_entry.grid(row=2, column=1)

key_file_label = tk.Label(root, text="Chemin de la clé:")
key_file_label.grid(row=3, column=0)
key_file_entry = tk.Entry(root)
key_file_entry.grid(row=3, column=1)

dynamic_checkbox = tk.Checkbutton(root, text="Tunnel dynamique")
dynamic_checkbox.grid(row=4, column=0, columnspan=2)

submit_button = tk.Button(root, text="Envoyer", command=submit)
submit_button.grid(row=5, column=0, columnspan=2)

root.mainloop()
