import customtkinter as ctk
import json
import os


laptops = []
good_laptops = []

laptops = [
    {"name": "asus zenbook 14",
    "processor": "int ult 5",
    "ram": "16gb ddr5",
    "storage": "512gb",
    "rating": 7.5
    }
    ]


def create_new_laptop():
    new_laptop = {"name": "",
                  "processor": "",
                  "ram": "",
                  "storage": "",
                  "rating": 0
                  }
    for key in new_laptop:
        new_laptop[key] = input(f"What is the {key} of the laptop? /")
    laptops.append(new_laptop)
    
def test_display_laptop(laptop):
    for item in laptop:
        print(laptop[item])



def create_frame(master):
    frame = ctk.CTkFrame(master)

    def set_laptop(choice):
                laptopchoice = next((laptop for laptop in laptops if laptop.get("name") == choice), None)
                print(laptopchoice)

    dropdownbox = ctk.CTkOptionMenu(frame, values=[laptops], command=set_laptop)
    dropdownbox.pack(side=ctk.TOP)

    innerframe = ctk.CTkFrame(frame)
    innerframe.pack(side=ctk.TOP)

    


    return frame




root = ctk.CTk()
root.title("laptop layout")
root.geometry("1400x800")

title = ctk.CTkLabel(root, text="laptop layout map")
title.pack(side=ctk.TOP)

# -------------------------------------------------------------

centre_frame = ctk.CTkFrame(root)
centre_frame.pack(side=ctk.TOP)

# -----------------------------------------

# top leftmost frame

topll_frame = ctk.CTkFrame(centre_frame)
topll_frame.grid(row=0, column=0)



# -----------------------------------

# top centreleft frame

topl_frame = ctk.CTkFrame(centre_frame)
topl_frame.grid(row=0, column=1)

# -----------------------------------

# top centreright frame

create_frame(centre_frame)


# -----------------------------------

# top rightmost frame



# ---------------------------------------

# intel table frame



# -----------------------------------

# microsoft table frame



# -----------------------------------

# middle centre frame



# -----------------------------------

# middle rightmost frame



# ---------------------------------------

# bottom centreleft frame



# -----------------------------------

# bottom centreright frame 



# -----------------------------------

# bottom rightmost frame



# --------------------------------------------------------





good_laptops = [laptop["name"] for laptop in laptops if laptop["rating"] > 5]
print(good_laptops)


root.mainloop()