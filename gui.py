import customtkinter as ctk
import diec
from CTkMenuBar import CTkMenuBar
from CTkMessagebox import CTkMessagebox
from plyer import notification
import os
import subprocess
import sys
from tkinter import messagebox, filedialog
from tkinter import ttk

# GUI setup
app = ctk.CTk()
app.geometry("1000x600")
app.title("diec-test-gui")
app.resizable(False, False)

# Info message
def info_messagebox():
    CTkMessagebox(title="diec-test-gui", message="Package: diec\nPyPi Version: 3.2\nRelease Date: 26.12.2024\nMade by: Eldritchyl")

# Restart the application
def restart_gui():
    app.destroy()
    python = sys.executable
    script_path = os.path.abspath(__file__)
    subprocess.Popen([python, script_path])

# Notify when conversion is done
def converting_done():
    notification.notify(
        title="diec-test-gui",
        message="Your text was converted!\nIt's saved in the same directory as the gui.py.\nYou can decode it with our other tool in the tabview!",
        timeout=2
    )

# Function to clear textboxes
def clear_textboxes():
    encode_textbox_encode.delete("1.0", "end")
    decode_textbox.delete("1.0", "end")
    encode_passphrase_entry.delete(0, "end")
    decode_passphrase_entry.delete(0, "end")

# Encoding function with file choice
def convert_to_diec():
    input_text = encode_textbox_encode.get("1.0", 'end-1c')
    passphrase = encode_passphrase_entry.get()

    if not input_text:
        messagebox.showinfo("No Text", "Please enter some text to encode.")
        return

    try:
        # Encoding process with passphrase
        diec.encode(input_text, passphrase)
        converting_done()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during encoding: {e}")

# Function to decode the selected DIEC file
def convert_to_text():
    filename = filedialog.askopenfilename(filetypes=[("DIEC files", "*.diec")])
    if not filename:
        messagebox.showinfo("No file selected", "Please select a file.")
        return
    
    passphrase = decode_passphrase_entry.get()
    if not passphrase:
        messagebox.showinfo("No passphrase", "Please enter the passphrase for decoding.")
        return

    try:
        # Decoding process with passphrase
        decoded_text = diec.decode(passphrase)
        decode_textbox.configure(state="normal")
        decode_textbox.delete("1.0", "end")
        decode_textbox.insert("1.0", decoded_text)
        decode_textbox.configure(state="disabled")
        messagebox.showinfo("Success", "File decoded successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during decoding: {e}")

# Validate selected file and check for counterpart
def is_valid_file(selected_file):
    directory = os.path.dirname(selected_file)
    base_name = os.path.basename(selected_file)
    
    if base_name == "encoded.diec":
        counterpart = os.path.join(directory, "key.diec")
    elif base_name == "key.diec":
        counterpart = os.path.join(directory, "encoded.diec")
    else:
        messagebox.showinfo("Invalid file", "Please select a file named 'encoded.diec' or 'key.diec'.")
        return False

    if not os.path.exists(counterpart):
        messagebox.showinfo("Missing counterpart", f"The directory must contain both 'key.diec' and 'encoded.diec'. Missing: {os.path.basename(counterpart)}")
        return False
    return True

# Exit confirmation
def on_close():
    if messagebox.askokcancel("Quit", "Do you really want to exit?"):
        app.quit()

# Menu bar with options
menubar = CTkMenuBar(master=app)
menubar.add_cascade("Restart", command=restart_gui)
menubar.add_cascade("Info", command=info_messagebox)

# Title label
label_title = ctk.CTkLabel(app, text="diec-test-gui", font=("Open Sans", 24))
label_title.pack(pady=5, padx=5)

# Tabview for Encode and Decode
tabview = ctk.CTkTabview(app)
tabview.pack(padx=20, pady=20)

# Encode Tab
tabview.add("Encode")
tabview.set("Encode")

encode_label = ctk.CTkLabel(tabview.tab("Encode"), text="Your text:")
encode_label.pack(pady=5, padx=5)

encode_textbox_encode = ctk.CTkTextbox(tabview.tab("Encode"), width=850, height=350)
encode_textbox_encode.pack(pady=5, padx=5)

encode_passphrase_label = ctk.CTkLabel(tabview.tab("Encode"), text="Passphrase:")
encode_passphrase_label.pack(pady=5, padx=5)

encode_passphrase_entry = ctk.CTkEntry(tabview.tab("Encode"), show="*")
encode_passphrase_entry.pack(pady=5, padx=5)

encode_button = ctk.CTkButton(tabview.tab("Encode"), text="Convert", command=convert_to_diec)
encode_button.pack(padx=5, pady=5)

# Clear encoding text box
clear_encode_button = ctk.CTkButton(tabview.tab("Encode"), text="Clear", command=clear_textboxes)
clear_encode_button.pack(padx=5, pady=5)

# Decode Tab
tabview.add("Decode")

decode_label = ctk.CTkLabel(tabview.tab("Decode"), text="Decoded text:")
decode_label.pack(pady=5, padx=5)

decode_textbox = ctk.CTkTextbox(tabview.tab("Decode"), width=850, height=350)
decode_textbox.pack(pady=5, padx=5)

decode_passphrase_label = ctk.CTkLabel(tabview.tab("Decode"), text="Passphrase:")
decode_passphrase_label.pack(pady=5, padx=5)

decode_passphrase_entry = ctk.CTkEntry(tabview.tab("Decode"), show="*")
decode_passphrase_entry.pack(pady=5, padx=5)

decode_button = ctk.CTkButton(tabview.tab("Decode"), text="Decode", command=convert_to_text)
decode_button.pack(padx=5, pady=5)

clear_decode_button = ctk.CTkButton(tabview.tab("Decode"), text="Clear", command=clear_textboxes)
clear_decode_button.pack(padx=5, pady=5)

# Progress bar
progress_bar = ttk.Progressbar(app, orient="horizontal", length=300, mode="indeterminate")
progress_bar.pack(pady=20)

# Run the application
app.protocol("WM_DELETE_WINDOW", on_close)  # Adding exit confirmation
app.mainloop()
