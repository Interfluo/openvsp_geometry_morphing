import os
import tkinter as tk


def execute_openvsp():
    """

    """
    cmd = ' '.join([exepath, vsppath, '-des', despath, '-script', scriptpath])
    os.system(cmd)
    return 0


def view_model():
    """

    """
    os.system(objpath)
    return 0


def open_file():
    """

    """
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text Editor Application - {filepath}")


def save_file():
    """

    """
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Text Editor Application - {filepath}")

    execute_openvsp()
    view_model()
    return 0


def find(name, path, arg):
    """
    Function will find a file in a directory and return the absolute or relative path.
    :param name: filename to look for
    :param path: directory to look in (often current working directory = os.getcwd())
    :param arg: if arg=0 returns relative path; if arg=1 return absolute path
    :return: absolute or relative path
    """
    for root, dirs, files in os.walk(path):
        if name in files:
            if arg == 0:
                return os.path.relpath(root, path)
            elif arg == 1:
                return os.path.join(root)


def vsp_directories(case, type):
    """

    """
    vsp_path = find('vsp.exe', os.getcwd(), 0)
    exepath = os.path.join(vsp_path, 'vsp.exe')
    vsppath = os.path.join(vsp_path, case, 'geometry.vsp3')
    despath = os.path.join(vsp_path, case, 'parameters.des')
    scriptpath = os.path.join(vsp_path, case, 'script.vspscript')
    filepath = os.path.join(os.getcwd(), despath)
    objpath = os.path.join(vsp_path, case, 'obj_geom.obj')

    if type=="script":
        filepath = scriptpath
    return vsp_path, exepath, vsppath, despath, scriptpath, filepath, objpath


[vsp_path, exepath, vsppath, despath, scriptpath, filepath, objpath] = vsp_directories('wing_generic', 'script')

window = tk.Tk()
window.title("Text Editor Application")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_exec = tk.Button(fr_buttons, text="execute", command=save_file)
btn_exec.grid(row=0, column=0, sticky="ew", padx=10, pady=15)
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

open_file()
window.mainloop()