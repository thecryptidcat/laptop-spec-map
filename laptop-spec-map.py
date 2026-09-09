import customtkinter as ctk
import json
import os

testlist = ["asus zenbook 14", "lenovo yoga", "hp omnibook"]

laptops = []
laptop_names = []
good_laptops = []

dropdownlist = []


laptops = [
    {"name": "asus zenbook 14",
    "sku": "n/a",    
    "processor": "int ult 5",
    "ram": "16gb ddr5",
    "storage": "512gb",
    "rating": 7.5
    }
]

reference_dict = laptops[0]


laptop_names = [laptop["name"] for laptop in laptops]

root = ctk.CTk()
root.title("laptop layout")
root.geometry("1600x950")

title = ctk.CTkLabel(root, text="laptop layout map")
title.pack(side=ctk.TOP)

centre_frame = ctk.CTkFrame(root)
centre_frame.pack(side=ctk.TOP)

output_label = ctk.CTkLabel(root, text="")
output_label.pack(side=ctk.TOP)

def create_laptop_frame(masterroot):
    frame = ctk.CTkFrame(masterroot)

    frame.grid_rowconfigure(0, weight=0)

    labels = []

    def set_laptop(choice):
                laptopchoice = next((laptop for laptop in laptops if laptop.get("name") == choice), None)
                output_text = ""
                for key, value in laptopchoice.items():
                     output_text+=(f"{key}: {value} \n")
                     output_label.configure(text=(output_text))
                for i, (key, value) in enumerate(laptopchoice.items()):
                     value_text = (f"{key}: {value}")
                     labels[i].configure(text=value_text)

    dropdownbox = ctk.CTkOptionMenu(master = frame, values=laptop_names, font=("Helvetica", 10), width=30, height=15, command = set_laptop)
    dropdownbox.pack(side=ctk.TOP)
    dropdownlist.append(dropdownbox)

    innerframe = ctk.CTkFrame(frame)
    innerframe.pack(side=ctk.TOP)

    for i, key,in enumerate(reference_dict):
         label = ctk.CTkLabel(innerframe, text=f"{key}:", font=("Helvetica", 10), height=13)
         label.grid(row=i+1, column=0)
         labels.append(label)

    

    return frame

def update_dropdowns():
     for dropdown in dropdownlist:
          dropdown.configure(values=laptop_names)

def create_new_laptop():
    new_laptop = {"name": "",
                  "sku": "",
                  "processor": "",
                  "ram": "",
                  "storage": "",
                  "rating": 0
                  }
    for key in new_laptop:
        new_laptop[key] = input(f"What is the {key} of the laptop? \n")
    laptops.append(new_laptop)
    laptop_names.append(new_laptop["name"])
    update_dropdowns()

    
def test_display_laptop(laptop):
    for item in laptop:
        print(laptop[item])


def create_table_frame(masterroot, columns, rows):
    frame = ctk.CTkFrame(masterroot)

    frame.grid_columnconfigure(0, weight=1)

    for row in range(rows):
         for column in range(columns):
              laptopslot = create_laptop_frame(frame)
              laptopslot.grid(row=row, column=column)

    return frame
    

# ----------------


# -----------------------------------

# top rightmost frame

toprr_frame = create_table_frame(centre_frame, 3, 2)
toprr_frame.grid(row=0, column=3, padx=5, pady=5)






# -----------------------------------

# top centreright frame

topr_frame = create_table_frame(centre_frame, 3, 2)
topr_frame.grid(row=0, column=2, padx=5, pady=5)

# -----------------------------------------

# top centreleft frame

topl_frame = create_table_frame(centre_frame, 3, 2)
topl_frame.grid(row=0, column=1, padx=5, pady=5)

# ---------------------------------------

# top leftmost frame

topll_frame = create_table_frame(centre_frame, 3, 2)
topll_frame.grid(row=0, column=0, padx=5, pady=5)

# -----------------------------------

# middle rightmost frame


# -----------------------------------

# middle centre frame


# -----------------------------------

# microsoft table frame


# -----------------------------------

# intel table frame


# ---------------------------------------

# bottom rightmost frame


# -----------------------------------

# bottom centreright frame 


# -----------------------------------

# bottom centreleft frame


# --------------------------------------------------------

#create_new_laptop()
#print(laptop_names)

print(dropdownlist)

good_laptops = [laptop["name"] for laptop in laptops if int(laptop["rating"]) > 5]

root.mainloop()