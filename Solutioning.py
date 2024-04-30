# Solutioning tool for Premier Logitech sales team
# Created By Dusty Baker January 2024
# Last Updated: 1/17/24
# Version 1.0


import tkinter
import customtkinter
from tkinter import *
from tkinter import filedialog
from pathlib import Path
from docxtpl import DocxTemplate
from PIL import Image
import os

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

# Set the path to the Word template
document_path = Path(__file__).parent / "Word_template.docx"

# Initialize the Word document template
doc = DocxTemplate(document_path)

# Initial context with placeholder values
context = {"Question1": "", "Question2": "", "Question3": "", "Question4": "", "Question5": ""}

# Define entries list
entries = []


def update_context():
    # Update the context with user's answers
    for i, entry in enumerate(entries, start=1):
        if isinstance(entry, customtkinter.CTkEntry):
            context[f"Question{i}"] = entry.get()
        elif isinstance(entry, customtkinter.CTkCheckBox):
            context[f"Question{i}"] = entry._text if entry.get() else ""
        elif isinstance(entry, customtkinter.CTkComboBox):
            context[f"Question{i}"] = entry.get()


def save_word_document():
    # Update the context before saving
    update_context()

    # Render the document with the updated context
    doc.render(context)

    # Ask the user to specify the file path and name
    file_path = filedialog.asksaveasfilename(
        defaultextension=".docx",
        filetypes=[("Word Documents", "*.docx")],
        initialdir=os.path.expanduser('~\\Downloads\\'),  # Initial directory
        title="Save the Word Document"
    )

    # Check if the user has selected a file path
    if file_path:
        # Save the Word document at the specified path
        doc.save(file_path)



# Create a function to clear the entries and checkboxes
def clear_entries():
    for entry in entries:
        if isinstance(entry, customtkinter.CTkEntry):
            entry.delete(0, END)
        elif isinstance(entry, customtkinter.CTkCheckBox):
            if entry.get():  # If checkbox is checked
                entry.toggle()  # Change its state
        elif isinstance(entry, customtkinter.CTkComboBox):
            entry.set("")


# GUI setup using custom tkinter
root = customtkinter.CTk()
root.title("Premier Solutioning Questionnaire")
root.geometry("700x1100")
root.iconbitmap("images/Lambda.ico")

Header_Image = customtkinter.CTkImage(light_image=Image.open("images/Picture1.jpg"),
                                      dark_image=Image.open("images/Picture1.jpg"),
                                      size=(400, 100))

Header_Label = customtkinter.CTkLabel(root, text="", image=Header_Image)
Header_Label.pack(pady=10)

# Create label
Header_Label1 = customtkinter.CTkLabel(root, text="Premier Solutioning Questionnaire")
Header_Label1.pack(pady=5)

# create tabview
My_tab = customtkinter.CTkTabview(root)
My_tab.pack(expand=1, fill="both")

# create tab
tab_1 = My_tab.add("3PL")
tab_2 = My_tab.add("Forward/Reverse Logistics")
tab_3 = My_tab.add("Life Cycle Services")
tab_4 = My_tab.add("Technology Services")

# put stuff in tab


# Create a scrollable frame for tab_1
scrollable_frame1 = customtkinter.CTkScrollableFrame(tab_1)
scrollable_frame1.pack(fill="both", expand=True)

# Create a scrollable frame for tab_2
scrollable_frame2 = customtkinter.CTkScrollableFrame(tab_2)
scrollable_frame2.pack(fill="both", expand=True)

# Create a scrollable frame for tab_3
scrollable_frame3 = customtkinter.CTkScrollableFrame(tab_3)
scrollable_frame3.pack(fill="both", expand=True)

# Create a scrollable frame for tab_4
scrollable_frame4 = customtkinter.CTkScrollableFrame(tab_4)
scrollable_frame4.pack(fill="both", expand=True)

# THIS IS THE START OF TAB 1 FOR 3PL


# Create a label for tab_1
tab_1_header = customtkinter.CTkLabel(scrollable_frame1, text="3rd Party Logistics", font=("Helvetica", 20))
tab_1_header.pack(pady=10)

# Basic Information label
BI_Label = customtkinter.CTkLabel(scrollable_frame1, text="Basic Information", font=("Helvetica", 20))
BI_Label.pack()

# Question 1
Q1_Label = customtkinter.CTkLabel(scrollable_frame1, text="Company")
Q1_Label.pack()

Q1_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q1_Entry.pack(pady=10)
entries.append(Q1_Entry)

# Question 2
Q2_Label = customtkinter.CTkLabel(scrollable_frame1, text="Mailing Address")
Q2_Label.pack()

Q2_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q2_Entry.pack(pady=10)
entries.append(Q2_Entry)

# Question 3
Q3_Label = customtkinter.CTkLabel(scrollable_frame1, text="Location Address")
Q3_Label.pack()

Q3_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q3_Entry.pack(pady=10)
entries.append(Q3_Entry)

# Question 4
Q4_Label = customtkinter.CTkLabel(scrollable_frame1, text="City")
Q4_Label.pack()

Q4_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q4_Entry.pack(pady=10)
entries.append(Q4_Entry)

# Question 5
Q5_Label = customtkinter.CTkLabel(scrollable_frame1, text="State")
Q5_Label.pack()

Q5_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q5_Entry.pack(pady=10)
entries.append(Q5_Entry)

# Question 6
Q6_Label = customtkinter.CTkLabel(scrollable_frame1, text="Zip Code")
Q6_Label.pack()

Q6_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q6_Entry.pack(pady=10)
entries.append(Q6_Entry)

# Question 7
Q7_Label = customtkinter.CTkLabel(scrollable_frame1, text="Primary Contact/Title")
Q7_Label.pack()

Q7_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q7_Entry.pack(pady=10)
entries.append(Q7_Entry)

# Question 8
Q8_Label = customtkinter.CTkLabel(scrollable_frame1, text="Phone Number")
Q8_Label.pack()

Q8_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q8_Entry.pack(pady=10)
entries.append(Q8_Entry)

# Question 9
Q9_Label = customtkinter.CTkLabel(scrollable_frame1, text="Extension")
Q9_Label.pack()

Q9_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q9_Entry.pack(pady=10)
entries.append(Q9_Entry)

# Question 10
Q10_Label = customtkinter.CTkLabel(scrollable_frame1, text="Email Address")
Q10_Label.pack()

Q10_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q10_Entry.pack(pady=10)
entries.append(Q10_Entry)

# Question 11
Q11_Label = customtkinter.CTkLabel(scrollable_frame1, text="Web address")
Q11_Label.pack()

Q11_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q11_Entry.pack(pady=10)
entries.append(Q11_Entry)

# Question 12
Q12_Label = customtkinter.CTkLabel(scrollable_frame1, text="Anticipated Start-Up Date")
Q12_Label.pack()

Q12_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q12_Entry.pack(pady=10)
entries.append(Q12_Entry)

# Question 13
Q13_Label = customtkinter.CTkLabel(scrollable_frame1, text="How did you hear about us?")
Q13_Label.pack()

Q13_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q13_Entry.pack(pady=10)
entries.append(Q13_Entry)

# value-added services label
VAS_Label = customtkinter.CTkLabel(scrollable_frame1, text="Value-Added Services", font=("Helvetica", 20))
VAS_Label.pack()

# light assembly label
LAS_Label = customtkinter.CTkLabel(scrollable_frame1, text="Light Assembly (Please select all that apply)")
LAS_Label.pack()

# value-added services checkbox
# question 14
Q14_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Electrical Assembly")
Q14_Entry.pack(pady=10)
entries.append(Q14_Entry)

# question 15
Q15_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Flashing/imaging")
Q15_Entry.pack(pady=10)
entries.append(Q15_Entry)

# question 16
Q16_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Kitting")
Q16_Entry.pack(pady=10)
entries.append(Q16_Entry)

# Packaging Requirements label
PR_Label = customtkinter.CTkLabel(scrollable_frame1, text="Packaging Requirements", font=("Helvetica", 20))
PR_Label.pack()

# select all that apply label
SATA_Label = customtkinter.CTkLabel(scrollable_frame1, text="Select all that apply")
SATA_Label.pack()

# question 17
Q17_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Clam Shelling")
Q17_Entry.pack(pady=10)
entries.append(Q17_Entry)

# question 18
Q18_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Full Seal")
Q18_Entry.pack(pady=10)
entries.append(Q18_Entry)

# question 19
Q19_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Partial Seal")
Q19_Entry.pack(pady=10)
entries.append(Q19_Entry)

# question 20
Q20_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Bagging")
Q20_Entry.pack(pady=10)
entries.append(Q20_Entry)

# question 21
Q21_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Blister")
Q21_Entry.pack(pady=10)
entries.append(Q21_Entry)

# question 22
Q22_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Shrink Wrapping")
Q22_Entry.pack(pady=10)
entries.append(Q22_Entry)

# question 23
Q23_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Repackaging")
Q23_Entry.pack(pady=10)
entries.append(Q23_Entry)

# question 24
Q24_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Fulfillment")
Q24_Entry.pack(pady=10)
entries.append(Q24_Entry)

# question 25
Q25_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Bundling")
Q25_Entry.pack(pady=10)
entries.append(Q25_Entry)

# question 26
Q26_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Labeling")
Q26_Entry.pack(pady=10)
entries.append(Q26_Entry)

# question 27
Q27_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Filling")
Q27_Entry.pack(pady=10)
entries.append(Q27_Entry)

# question 28
Q28_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Promotional Item Assembly")
Q28_Entry.pack(pady=10)
entries.append(Q28_Entry)

# question 29
Q29_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Display Assembly")
Q29_Entry.pack(pady=10)
entries.append(Q29_Entry)

# question 30
Q30_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Mass Merchandiser Assembly")
Q30_Entry.pack(pady=10)
entries.append(Q30_Entry)

# question 31
Q31_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Bulk Transfer Chemicals")
Q31_Entry.pack(pady=10)
entries.append(Q31_Entry)

# question 32
Q32_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Bulk Transfer Resins")
Q32_Entry.pack(pady=10)
entries.append(Q32_Entry)

# question 33
Q33_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Product Inspection")
Q33_Entry.pack(pady=10)
entries.append(Q33_Entry)

# question 34
Q34_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Other Please Specify", width=250)
Q34_Entry.pack(pady=10)
entries.append(Q34_Entry)

# Reverse Logistics label
RL_Label = customtkinter.CTkLabel(scrollable_frame1, text="Reverse Logistics", font=("Helvetica", 20))
RL_Label.pack(pady=10)

# select all that apply label
SATA_Label = customtkinter.CTkLabel(scrollable_frame1, text="Reverse Logistics Requirements: (Select all that apply)")
SATA_Label.pack()

# question 35
Q35_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Return management")
Q35_Entry.pack(pady=10)
entries.append(Q35_Entry)

# question 36
Q36_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Sorting")
Q36_Entry.pack(pady=10)
entries.append(Q36_Entry)

# question 37
Q37_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Visual Inspections")
Q37_Entry.pack(pady=10)
entries.append(Q37_Entry)

# question 38
Q38_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Level 1 repairs")
Q38_Entry.pack(pady=10)
entries.append(Q38_Entry)

# question 39
Q39_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Other Please Specify", width=250)
Q39_Entry.pack(pady=10)
entries.append(Q39_Entry)

# Warehousing Product information label
WPI_Label = customtkinter.CTkLabel(scrollable_frame1, text="Warehousing Product Information", font=("Helvetica", 20))
WPI_Label.pack()

# question 40
Q40_Label = customtkinter.CTkLabel(scrollable_frame1, text="Product Description:")
Q40_Label.pack()

Q40_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q40_Entry.pack(pady=10)
entries.append(Q40_Entry)

# question 41
Q41_Label = customtkinter.CTkLabel(scrollable_frame1, text="What is the volume expectation and timing?")
Q41_Label.pack()

Q41_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q41_Entry.pack(pady=10)
entries.append(Q41_Entry)

# question 42
Q42_Label = customtkinter.CTkLabel(scrollable_frame1, text="How do you want your rate to be quoted:")
Q42_Label.pack()

Q42_answers = ["", "Case", "Carton", "Pallet"]
Q42_Entry = customtkinter.CTkComboBox(scrollable_frame1, values=Q42_answers)
Q42_Entry.pack(pady=10)
entries.append(Q42_Entry)

# Inventory/Storage Criteria label
ISC_Label = customtkinter.CTkLabel(scrollable_frame1, text="Inventory/Storage Criteria", font=("Helvetica", 20))
ISC_Label.pack()

# question 43
Q43_Label = customtkinter.CTkLabel(scrollable_frame1, text="How many sku's will be inventoried?")
Q43_Label.pack()

Q43_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q43_Entry.pack(pady=10)
entries.append(Q43_Entry)

# question 44
Q44_Label = customtkinter.CTkLabel(scrollable_frame1, text="Will there be new SKU(s)")
Q44_Label.pack()

Q44_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q44_Entry.pack(pady=10)
entries.append(Q44_Entry)

# question 45
Q45_Label = customtkinter.CTkLabel(scrollable_frame1,
                                   text="What are the elements of the inventroy report? Will the inventory report be real-time? ")
Q45_Label.pack()

Q45_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q45_Entry.pack(pady=10)
entries.append(Q45_Entry)

# question 46
Q46_Label = customtkinter.CTkLabel(scrollable_frame1, text="How many inventory turns per year?")
Q46_Label.pack()

Q46_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q46_Entry.pack(pady=10)
entries.append(Q46_Entry)

# question 47
Q47_Label = customtkinter.CTkLabel(scrollable_frame1, text="Indicate inventory levels in:")
Q47_Label.pack()

Q47_Answers = ["", "Average Min number Pallets", "Average Max number Pallets"]
Q47_Entry = customtkinter.CTkComboBox(scrollable_frame1, values=Q47_Answers)
Q47_Entry.pack(pady=10)
entries.append(Q47_Entry)

# question 48
Q48_Label = customtkinter.CTkLabel(scrollable_frame1, text="How many cases per pallet:")
Q48_Label.pack()

Q48_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q48_Entry.pack(pady=10)
entries.append(Q48_Entry)

# question 49
Q49_Label = customtkinter.CTkLabel(scrollable_frame1, text="What is weight per pallet:")
Q49_Label.pack()

Q49_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q49_Entry.pack(pady=10)
entries.append(Q49_Entry)

# question 50
Q50_Label = customtkinter.CTkLabel(scrollable_frame1, text="What is the weight per case:")
Q50_Label.pack()

Q50_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q50_Entry.pack(pady=10)
entries.append(Q50_Entry)

# question 51
Q51_Label = customtkinter.CTkLabel(scrollable_frame1, text="Can Customer's product be stacked: If so, how high?")
Q51_Label.pack()

Q51_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q51_Entry.pack(pady=10)
entries.append(Q51_Entry)

# question 52
Q52_Label = customtkinter.CTkLabel(scrollable_frame1,
                                   text="Does the product require temperature or humidity control? If so, what range")
Q52_Label.pack()

Q52_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q52_Entry.pack(pady=10)
entries.append(Q52_Entry)

# question 53
Q53_Label = customtkinter.CTkLabel(scrollable_frame1, text="Will Premier need to pick inventory via FIFO method?")
Q53_Label.pack()

Q53_Entry = customtkinter.CTkComboBox(scrollable_frame1, values=["", "Yes", "No"])
Q53_Entry.pack(pady=10)
entries.append(Q53_Entry)

# question 54
Q54_Label = customtkinter.CTkLabel(scrollable_frame1,
                                   text="Do Customer require more than the standard FIFO control, if yes, explain.")
Q54_Label.pack()

Q54_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q54_Entry.pack(pady=10)
entries.append(Q54_Entry)

# question 55
Q55_Label = customtkinter.CTkLabel(scrollable_frame1,
                                   text="Are there any hazardous materials involved? If yes, explain.")
Q55_Label.pack()

Q55_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q55_Entry.pack(pady=10)
entries.append(Q55_Entry)

# Inbound Shipment Criteria label
ISC_Label = customtkinter.CTkLabel(scrollable_frame1, text="Inbound Shipment Criteria", font=("Helvetica", 20))
ISC_Label.pack()

# Inbound Shipment Criteria Check all that apply label
ISC_Check_Label = customtkinter.CTkLabel(scrollable_frame1, text="Inbound Shipment Criteria: Check all that apply")
ISC_Check_Label.pack()

# question 56
Q56_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Floor Loaded")
Q56_Entry.pack(pady=10)
entries.append(Q56_Entry)

# question 57
Q57_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Palletized")
Q57_Entry.pack(pady=10)
entries.append(Q57_Entry)

# question 58
Q58_Entry = customtkinter.CTkCheckBox(scrollable_frame1, text="Slip Sheeted")
Q58_Entry.pack(pady=10)
entries.append(Q58_Entry)

# question 59
Q59_LABEL = customtkinter.CTkLabel(scrollable_frame1,
                                   text="Are inbound shipping pallets standard 40 x 48, 4 way GMA pallets? If no, explain:")
Q59_LABEL.pack()

Q59_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q59_Entry.pack(pady=10)
entries.append(Q59_Entry)

# question 60
Q60_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Does Customer require a pallet exchange on I/B shipments?")
Q60_LABEL.pack()

Q60_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q60_Entry.pack(pady=10)
entries.append(Q60_Entry)

# question 61
Q61_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Does Customer require a pallet exchange on O/B shipments?")
Q61_LABEL.pack()

Q61_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q61_Entry.pack(pady=10)
entries.append(Q61_Entry)

# question 62
Q62_LABEL = customtkinter.CTkLabel(scrollable_frame1,
                                   text="Inbound shipments will be by: ( Carrier, Logistics Company?)")
Q62_LABEL.pack()

Q62_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q62_Entry.pack(pady=10)
entries.append(Q62_Entry)

# Outbound Shiping/Transportation Criteria/Carriers label
OSTCC_Label = customtkinter.CTkLabel(scrollable_frame1, text="Outbound Shipping/Transportation Criteria/Carriers",
                                     font=("Helvetica", 20))
OSTCC_Label.pack()

# question 63
Q63_LABEL = customtkinter.CTkLabel(scrollable_frame1,
                                   text="What is the anticipated volume of outbound shipments per day?")
Q63_LABEL.pack()

Q63_Entry = customtkinter.CTkComboBox(scrollable_frame1, values=["", "LTL", "FTL", "Parcel"])
Q63_Entry.pack(pady=10)
entries.append(Q63_Entry)

# question 64
Q64_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Transportation Criteria")
Q64_LABEL.pack()

Q64_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q64_Entry.pack(pady=10)
entries.append(Q64_Entry)

# question 65
Q65_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Shipping Points")
Q65_LABEL.pack()

Q65_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q65_Entry.pack(pady=10)
entries.append(Q65_Entry)

# question 66
Q66_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Freight Class")
Q66_LABEL.pack()

Q66_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q66_Entry.pack(pady=10)
entries.append(Q66_Entry)

# question 67
Q67_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Other Special Requirements")
Q67_LABEL.pack()

Q67_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q67_Entry.pack(pady=10)
entries.append(Q67_Entry)

# question 68
Q68_LABEL = customtkinter.CTkLabel(scrollable_frame1,
                                   text="Which carrier will be used? Is it a combination of carierrs?")
Q68_LABEL.pack()

Q68_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q68_Entry.pack(pady=10)
entries.append(Q68_Entry)

# question 69
Q69_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Who will be responsible for setting up carrier pick up?")
Q69_LABEL.pack()

Q69_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q69_Entry.pack(pady=10)
entries.append(Q69_Entry)

# question 70
Q70_LABEL = customtkinter.CTkLabel(scrollable_frame1,
                                   text="Will Premier utilize Customer/End-Customer carrier accounts?")
Q70_LABEL.pack()

Q70_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q70_Entry.pack(pady=10)
entries.append(Q70_Entry)

# question 71
Q71_LABEL = customtkinter.CTkLabel(scrollable_frame1,
                                   text="If Customer has other special requirements in handling Customer product, please specify additional requirement here:")
Q71_LABEL.pack()

Q71_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q71_Entry.pack(pady=10)
entries.append(Q71_Entry)

# question 72
Q72_LABEL = customtkinter.CTkLabel(scrollable_frame1,
                                   text="Please indicate Customer's shipping volume in terms of number of orders per quarter:")
Q72_LABEL.pack()

Q72_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q72_Entry.pack(pady=10)
entries.append(Q72_Entry)

# question 73
Q73_LABEL = customtkinter.CTkLabel(scrollable_frame1,
                                   text="Are any systems in OCONUS locations (defined as outside the continental US)? \nIf yes, what is the number of OCONUS systems? Provide specific addresses and quantities.")
Q73_LABEL.pack()

Q73_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q73_Entry.pack(pady=10)
entries.append(Q73_Entry)

# question 74
Q74_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="What is the max delivery time to location in days?")
Q74_LABEL.pack()

Q74_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q74_Entry.pack(pady=10)
entries.append(Q74_Entry)

# question 75
Q75_LABEL = customtkinter.CTkLabel(scrollable_frame1,
                                   text="What percent of outbound movement is pulled by Serialized vs. Non serialized")
Q75_LABEL.pack()

Q75_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q75_Entry.pack(pady=10)
entries.append(Q75_Entry)

# question 76
Q76_LABEL = customtkinter.CTkLabel(scrollable_frame1,
                                   text="Does Customer product require temperature controlled transportation?")
Q76_LABEL.pack()

Q76_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q76_Entry.pack(pady=10)
entries.append(Q76_Entry)

# question 77
Q77_LABEL = customtkinter.CTkLabel(scrollable_frame1,
                                   text="Will there be specific labeling requirements for outbound orders?")
Q77_LABEL.pack()

Q77_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q77_Entry.pack(pady=10)
entries.append(Q77_Entry)

# question 78
Q78_LABEL = customtkinter.CTkLabel(scrollable_frame1,
                                   text="Will Premier be required to overpack (i.e. consolidate multiple items in larger box),\nif multiple items are ordered by a Customer? Or will Customer/End-Customer \nreceive new equipment in original boxes packaged separately?  Provide an explanation of expectations.")
Q78_LABEL.pack()

Q78_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q78_Entry.pack(pady=10)
entries.append(Q78_Entry)

# question 79
Q79_LABEL = customtkinter.CTkLabel(scrollable_frame1,
                                   text="Will specific boxes with logos be required? If yes, will Customer/End-Customer supply such boxes to Premier?")
Q79_LABEL.pack()

Q79_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q79_Entry.pack(pady=10)
entries.append(Q79_Entry)

# question 80
Q80_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="What is the desired shipping cycle? Be specific.")
Q80_LABEL.pack()

Q80_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q80_Entry.pack(pady=10)
entries.append(Q80_Entry)

# Basic Outbound Order information label
BOOI_Label = customtkinter.CTkLabel(scrollable_frame1, text="Basic Outbound Order information", font=("Helvetica", 20))
BOOI_Label.pack()

# question 81
Q81_LABEL = customtkinter.CTkLabel(scrollable_frame1,
                                   text="How will Premier receive orders? At what point can an order be processed? Is there any \nadditional paperwork required with orders? i.e.  packing slips, order documents?")
Q81_LABEL.pack()

Q81_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q81_Entry.pack(pady=10)
entries.append(Q81_Entry)

# question 82
Q82_LABEL = customtkinter.CTkLabel(scrollable_frame1,
                                   text="What is the cycle time expectation? i.e. order receipt cutoff for shipping (same day?)  and will \norders that are placed by Customer overnight be sent to Premier in a batch of orders at 8:00 \na.m.? If so, how many batches?")
Q82_LABEL.pack()

Q82_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q82_Entry.pack(pady=10)
entries.append(Q82_Entry)

# question 83
Q83_LABEL = customtkinter.CTkLabel(scrollable_frame1,
                                   text="If Premier is shipping multiple units to the same client, will Premier ship out in original boxes or \ndo we overpack when possible or use multiple boxes/containers?  \nIf overpack or multiple boxes,who will provide the boxes - Premier, Customer, End-Customer?")
Q83_LABEL.pack()

Q83_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q83_Entry.pack(pady=10)
entries.append(Q83_Entry)

# question 84
Q84_LABEL = customtkinter.CTkLabel(scrollable_frame1,
                                   text="What are the parameters of order cancellation? i.e. At what point can the order be cancelled?")
Q84_LABEL.pack()

Q84_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q84_Entry.pack(pady=10)
entries.append(Q84_Entry)

# question 85
Q85_LABEL = customtkinter.CTkLabel(scrollable_frame1,
                                   text="Are there any special packaging requirements that need to be considered.")
Q85_LABEL.pack()

Q85_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q85_Entry.pack(pady=10)
entries.append(Q85_Entry)

# question 86
Q86_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Average weight per order")
Q86_LABEL.pack()

Q86_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q86_Entry.pack(pady=10)
entries.append(Q86_Entry)

# question 87
Q87_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Average number of lines per order")
Q87_LABEL.pack()

Q87_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q87_Entry.pack(pady=10)
entries.append(Q87_Entry)

# question 88
Q88_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Number of Sku's per order")
Q88_LABEL.pack()

Q88_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q88_Entry.pack(pady=10)
entries.append(Q88_Entry)

# question 89
Q89_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Number of cases per order")
Q89_LABEL.pack()

Q89_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q89_Entry.pack(pady=10)
entries.append(Q89_Entry)

# question 90
Q90_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="How will orders be sent")
Q90_LABEL.pack()

Q90_Entry = customtkinter.CTkComboBox(scrollable_frame1, values=["", "EDI", "Email"])
Q90_Entry.pack(pady=10)
entries.append(Q90_Entry)

# question 91
Q91_LABEL = customtkinter.CTkLabel(scrollable_frame1,
                                   text="Will Customer use Premier's order template to place orders?")
Q91_LABEL.pack()

Q91_Entry = customtkinter.CTkComboBox(scrollable_frame1, values=["", "Yes", "No"])
Q91_Entry.pack(pady=10)
entries.append(Q91_Entry)

# question 92
Q92_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Chemical Criteria")
Q92_LABEL.pack()

Q92_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q92_Entry.pack(pady=10)
entries.append(Q92_Entry)

# question 93
Q93_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Description of product")
Q93_LABEL.pack()

Q93_Entry = customtkinter.CTkComboBox(scrollable_frame1,
                                      values=["", "Hazardous", "Non-hazardous", "FDA/OTC requirements"])
Q93_Entry.pack(pady=10)
entries.append(Q93_Entry)

# question 94
Q94_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Special Handling Requirements")
Q94_LABEL.pack()

Q94_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q94_Entry.pack(pady=10)
entries.append(Q94_Entry)

# question 95
Q95_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Special Shipping Requirements")
Q95_LABEL.pack()

Q95_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q95_Entry.pack(pady=10)
entries.append(Q95_Entry)

# question 96
Q96_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Other Special Considerations")
Q96_LABEL.pack()

Q96_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q96_Entry.pack(pady=10)
entries.append(Q96_Entry)

# question 97
Q97_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Location")
Q97_LABEL.pack()

Q97_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="City", width=250)
Q97_Entry.pack()
entries.append(Q97_Entry)

Q98_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="State", width=250)
Q98_Entry.pack()
entries.append(Q98_Entry)

# Setup and Systems label
SS_Label = customtkinter.CTkLabel(scrollable_frame1, text="Setup and Systems", font=("Helvetica", 20))
SS_Label.pack()

# question 99
Q99_LABEL = customtkinter.CTkLabel(scrollable_frame1,
                                   text="Is the Serial/Lot number requirement a front end requirement forsome or all skus?")
Q99_LABEL.pack()

Q99_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q99_Entry.pack(pady=10)
entries.append(Q99_Entry)

# question 100
Q100_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Can skus that are Serial/Lot number on receipt \nbe "
                                                            "different than SKU(s) with Serial/Lot number on ship?")
Q100_LABEL.pack()

Q100_Entry = customtkinter.CTkComboBox(scrollable_frame1, values=["", "Yes", "No"])
Q100_Entry.pack(pady=10)
entries.append(Q100_Entry)

# question 101
Q101_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Are the Serial/Lot numbers scannable?")
Q101_LABEL.pack()

Q101_Entry = customtkinter.CTkComboBox(scrollable_frame1, values=["", "Yes", "No"])
Q101_Entry.pack(pady=10)
entries.append(Q101_Entry)

# question 102
Q102_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="What is the Serial/Lot number format?")
Q102_LABEL.pack()

Q102_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q102_Entry.pack(pady=10)
entries.append(Q102_Entry)

# question 103
Q103_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="When utilizing ecommerce business, is there a "
                                                            "requirement to track available inventory? \nalert end "
                                                            "customers of items shipped? and provide tracking "
                                                            "information?\nHow will this information be exchanged?")
Q103_LABEL.pack()

Q103_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q103_Entry.pack(pady=10)
entries.append(Q103_Entry)

# question 104
Q104_LABEL = customtkinter.CTkLabel(scrollable_frame1,
                                    text="What type of remote visibility or data is needed?  Inventory, kits, shipments, tracking?")
Q104_LABEL.pack()

Q104_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q104_Entry.pack(pady=10)
entries.append(Q104_Entry)

# question 105
Q105_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="How many interfaces are required, and what are the "
                                                            "interfaces?\n(Interfaces are defined as files exchanged "
                                                            "between Customer's system andPremier's)?")
Q105_LABEL.pack()

Q105_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q105_Entry.pack(pady=10)
entries.append(Q105_Entry)

# question 106
Q106_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Are specs and sample files available for all interfaces?")
Q106_LABEL.pack()

Q106_Entry = customtkinter.CTkComboBox(scrollable_frame1, values=["", "Yes", "No"])
Q106_Entry.pack(pady=10)
entries.append(Q106_Entry)

# question 107
Q107_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Does Customer need any customized reporting?")
Q107_LABEL.pack()

Q107_Entry = customtkinter.CTkComboBox(scrollable_frame1, values=["", "Yes", "No"])
Q107_Entry.pack(pady=10)
entries.append(Q107_Entry)

# question 108
Q108_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Is UPS / FedEx integration needed?")
Q108_LABEL.pack()

Q108_Entry = customtkinter.CTkComboBox(scrollable_frame1, values=["", "Yes", "No"])
Q108_Entry.pack(pady=10)
entries.append(Q108_Entry)

# question 109
Q109_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Will Premier be required to maintain limited liability "
                                                            "insurance for loss while in storage?")
Q109_LABEL.pack()

Q109_Entry = customtkinter.CTkComboBox(scrollable_frame1, values=["", "Yes", "No"])
Q109_Entry.pack(pady=10)
entries.append(Q109_Entry)

# Customer Service label
CS_Label = customtkinter.CTkLabel(scrollable_frame1, text="Customer Service", font=("Helvetica", 20))
CS_Label.pack()

# question 110
Q110_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="How will returns be processed?")
Q110_LABEL.pack()

Q110_Entry = customtkinter.CTkEntry(scrollable_frame1, placeholder_text="Enter your answer here", width=250)
Q110_Entry.pack(pady=10)
entries.append(Q110_Entry)

# question 111
Q111_LABEL = customtkinter.CTkLabel(scrollable_frame1, text="Most ecommerce business has Customer service support for "
                                                            "order status,\nreturns, etc. Who will provide Customer "
                                                            "service to Customer/ End-Customer users?")
Q111_LABEL.pack()

Q111_Entry = customtkinter.CTkComboBox(scrollable_frame1, values=["", "Yes", "No"])
Q111_Entry.pack(pady=10)
entries.append(Q111_Entry)

# THIS IS THE START OF TAB 2 FOR FORWARD AND REVERSE LOGISTICS

# Forward and Reverse Logistics label
FRL_Label = customtkinter.CTkLabel(scrollable_frame2, text="Forward and Reverse Logistics", font=("Helvetica", 20))
FRL_Label.pack(pady=10)

# basic information label
BI_Label = customtkinter.CTkLabel(scrollable_frame2, text="Basic Information", font=("Helvetica", 20))
BI_Label.pack()

# the follwing questions are in scrollable_frame2 and exactly mirror questions 1-13
# question 112
Q112_Label = customtkinter.CTkLabel(scrollable_frame2, text="Company")
Q112_Label.pack()

Q112_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q112_Entry.pack(pady=10)
entries.append(Q112_Entry)

# question 113
Q113_Label = customtkinter.CTkLabel(scrollable_frame2, text="Mailing Address")
Q113_Label.pack()

Q113_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q113_Entry.pack(pady=10)
entries.append(Q113_Entry)

# question 114
Q114_Label = customtkinter.CTkLabel(scrollable_frame2, text="Location Address")
Q114_Label.pack()

Q114_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q114_Entry.pack(pady=10)
entries.append(Q114_Entry)

# question 115
Q115_Label = customtkinter.CTkLabel(scrollable_frame2, text="City")
Q115_Label.pack()

Q115_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q115_Entry.pack(pady=10)
entries.append(Q115_Entry)

# question 116
Q116_Label = customtkinter.CTkLabel(scrollable_frame2, text="State")
Q116_Label.pack()

Q116_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q116_Entry.pack(pady=10)
entries.append(Q116_Entry)

# question 117
Q117_Label = customtkinter.CTkLabel(scrollable_frame2, text="Zip Code")
Q117_Label.pack()

Q117_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q117_Entry.pack(pady=10)
entries.append(Q117_Entry)

# question 118
Q118_Label = customtkinter.CTkLabel(scrollable_frame2, text="Primary Contact/Title")
Q118_Label.pack()

Q118_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q118_Entry.pack(pady=10)
entries.append(Q118_Entry)

# question 119
Q119_Label = customtkinter.CTkLabel(scrollable_frame2, text="Phone Number")
Q119_Label.pack()

Q119_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q119_Entry.pack(pady=10)
entries.append(Q119_Entry)

# question 120
Q120_Label = customtkinter.CTkLabel(scrollable_frame2, text="Extension")
Q120_Label.pack()

Q120_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q120_Entry.pack(pady=10)
entries.append(Q120_Entry)

# question 121
Q121_Label = customtkinter.CTkLabel(scrollable_frame2, text="Email Address")
Q121_Label.pack()

Q121_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q121_Entry.pack(pady=10)
entries.append(Q121_Entry)

# question 122
Q122_Label = customtkinter.CTkLabel(scrollable_frame2, text="Web Address")
Q122_Label.pack()

Q122_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q122_Entry.pack(pady=10)
entries.append(Q122_Entry)

# question 123
Q123_Label = customtkinter.CTkLabel(scrollable_frame2, text="Anticipated Start-Up Date")
Q123_Label.pack()

Q123_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q123_Entry.pack(pady=10)
entries.append(Q123_Entry)

# question 124
Q124_Label = customtkinter.CTkLabel(scrollable_frame2, text="How did you hear about us")
Q124_Label.pack()

Q124_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q124_Entry.pack(pady=10)
entries.append(Q124_Entry)

# Logistics label
L_Label = customtkinter.CTkLabel(scrollable_frame2, text="Logistics", font=("Helvetica", 20))
L_Label.pack()

# Logistics small label
LS_Label = customtkinter.CTkLabel(scrollable_frame2, text="Please see the 3PL tab")
LS_Label.pack()

# Prospecting Questions label
PQ_Label = customtkinter.CTkLabel(scrollable_frame2, text="Prospecting Questions", font=("Helvetica", 20))
PQ_Label.pack(pady=10)

# question 125
Q125_Label = customtkinter.CTkLabel(scrollable_frame2, text="Please indicate which category your company fall under:")
Q125_Label.pack()

Q125_Entry = customtkinter.CTkComboBox(scrollable_frame2,
                                       values=["", "OEM/ODM", " 3rd Party Logistics", "Distributor", "Wholesaler",
                                               "Retailer"])
Q125_Entry.pack(pady=10)
entries.append(Q125_Entry)

# question 126
Q126_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="Description of your products (i.e. smartphone, security devices, IOT, FWA, computers, etc.)")
Q126_Label.pack()

Q126_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q126_Entry.pack(pady=10)
entries.append(Q126_Entry)

# question 127
Q127_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="Does Customer currently have a team that supports after-sales and end users' returns?")
Q127_Label.pack()

Q127_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q127_Entry.pack(pady=10)
entries.append(Q127_Entry)

# question 128
Q128_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="How do you support after-sales activities for in-warranty & out-of-warranty returns, \nsame unit repair? Please attach process flow charts if available.")
Q128_Label.pack()

Q128_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q128_Entry.pack(pady=10)
entries.append(Q128_Entry)

# question 129
Q129_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="Who issues the RMA to initiate the returns? Do you need Premier's return portal to initiate,\nprocess, and manage returns from end users?")
Q129_Label.pack()

Q129_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q129_Entry.pack(pady=10)
entries.append(Q129_Entry)

# question 130
Q130_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="Do you have ASC (authorized service center) or PSC (private service center) program in place for your repair program?")
Q130_Label.pack()

Q130_Entry = customtkinter.CTkComboBox(scrollable_frame2, values=["", "Yes", "No"])
Q130_Entry.pack(pady=10)
entries.append(Q130_Entry)

# question 131
Q131_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="How are you capturing returns data and analyze to reduce such returns and/or minimize the return cost?")
Q131_Label.pack()

Q131_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q131_Entry.pack(pady=10)
entries.append(Q131_Entry)

# question 132
Q132_Label = customtkinter.CTkLabel(scrollable_frame2, text="What is your biggest challenges and painpoints currently?")
Q132_Label.pack()

Q132_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q132_Entry.pack(pady=10)
entries.append(Q132_Entry)

# question 133
Q133_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="Does Customer support SUR (same unit repair) and bulk repair for in-warranty and out of warranty?")
Q133_Label.pack()

Q133_Entry = customtkinter.CTkComboBox(scrollable_frame2, values=["", "Yes", "No"])
Q133_Entry.pack(pady=10)
entries.append(Q133_Entry)

# question 134
Q134_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="What percent of Customer total revenue was spent on reverse logistics last year?")
Q134_Label.pack()

Q134_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q134_Entry.pack(pady=10)
entries.append(Q134_Entry)

# question 135
Q135_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="Is there any CPR (Cost Per Repair) reduction program in place \n(i.e. cosmetic parts reclamation, parts harvesting, display buff & polish)?")
Q135_Label.pack()

Q135_Entry = customtkinter.CTkComboBox(scrollable_frame2, values=["", "Yes", "No"])
Q135_Entry.pack(pady=10)
entries.append(Q135_Entry)

# question 136
Q136_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="Do you see a benefit if there were a system and data set related\nto your reverse logistics that were standardized across your company and divisions?\nIn relation to this question, what is your current reporting requirements?")
Q136_Label.pack()

Q136_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q136_Entry.pack(pady=10)
entries.append(Q136_Entry)

# question 137
Q137_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="Which area in your reverse logistics process do you think needs improvements?")
Q137_Label.pack()

Q137_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q137_Entry.pack(pady=10)
entries.append(Q137_Entry)

# question 138
Q138_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="Who in your organization would be primarily involved in doing cost \nanalysis and deciding to discuss some options to achieve cost savings and \nimplementation of necessary changes in current reverse logistics process?")
Q138_Label.pack()

Q138_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q138_Entry.pack(pady=10)
entries.append(Q138_Entry)

# question 139
Q139_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="What level of repair service are you authorizing your service provider?")
Q139_Label.pack()

Q139_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q139_Entry.pack(pady=10)
entries.append(Q139_Entry)

# question 140
Q140_Label = customtkinter.CTkLabel(scrollable_frame2, text="What is monthly volume?")
Q140_Label.pack()

Q140_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q140_Entry.pack(pady=10)
entries.append(Q140_Entry)

# question 141
Q141_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="Who is responsible for delivery from the service provider to the customer?")
Q141_Label.pack()

Q141_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q141_Entry.pack(pady=10)
entries.append(Q141_Entry)

# Returns Management /Test Triage label
RMTT_Label = customtkinter.CTkLabel(scrollable_frame2, text="Returns Management /Test Triage", font=("Helvetica", 20))
RMTT_Label.pack()

# question 142
Q142_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="At the time of receiving returns, what information is captured for return analysis?")
Q142_Label.pack()

Q142_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q142_Entry.pack(pady=10)
entries.append(Q142_Entry)

# question 143
Q143_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="How does Premier get ASN (i.e. API, EDI, email, etc.)? Will system integration be needed?")
Q143_Label.pack()

Q143_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q143_Entry.pack(pady=10)
entries.append(Q143_Entry)

# question 144
Q144_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="Are those returns from the field individually or store level or from collection point? Parcel or bulk?")
Q144_Label.pack()

Q144_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q144_Entry.pack(pady=10)
entries.append(Q144_Entry)

# question 145
Q145_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="How many handling points does a returned device pass through until it gets to Product Return Center?")
Q145_Label.pack()

Q145_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q145_Entry.pack(pady=10)
entries.append(Q145_Entry)

# question 146
Q146_Label = customtkinter.CTkLabel(scrollable_frame2, text="What data is captured upon receipt of such returns?")
Q146_Label.pack()

Q146_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q146_Entry.pack(pady=10)
entries.append(Q146_Entry)

# question 147
Q147_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="Do you provide a program to adjudicate In & Out of Warranty status?")
Q147_Label.pack()

Q147_Entry = customtkinter.CTkComboBox(scrollable_frame2, values=["", "Yes", "No"])
Q147_Entry.pack(pady=10)
entries.append(Q147_Entry)

# question 148
Q148_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="How do you determine repairable and non-repairable, and at which point of process?")
Q148_Label.pack()

Q148_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q148_Entry.pack(pady=10)
entries.append(Q148_Entry)

# question 149
Q149_Label = customtkinter.CTkLabel(scrollable_frame2, text="Thresholds on parts and labor leading to BER")
Q149_Label.pack()

Q149_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q149_Entry.pack(pady=10)
entries.append(Q149_Entry)

# question 150
Q150_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="What is the exceptions process such OSD at receiving (overage, shortage, damaged)?")
Q150_Label.pack()

Q150_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q150_Entry.pack(pady=10)
entries.append(Q150_Entry)

# question 151
Q151_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="Is Customer EDI capable or flat file via API for such data traffic?")
Q151_Label.pack()

Q151_Entry = customtkinter.CTkComboBox(scrollable_frame2, values=["", "Yes", "No"])
Q151_Entry.pack(pady=10)
entries.append(Q151_Entry)

# question 152
Q152_Label = customtkinter.CTkLabel(scrollable_frame2, text="Does service provider work with 3rd party call center to "
                                                            "manage RMA and reconcile RMA?\nDo you expect service "
                                                            "provider to work with end-user directly?")
Q152_Label.pack()

Q152_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q152_Entry.pack(pady=10)
entries.append(Q152_Entry)

# question 153
Q153_Label = customtkinter.CTkLabel(scrollable_frame2, text="Do you allow using 3rd party diagnostic program for "
                                                            "functional test?\nOr Does your device have in-device "
                                                            "diagnostic tool?")
Q153_Label.pack()

Q153_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q153_Entry.pack(pady=10)
entries.append(Q153_Entry)

# Repair/Production label
RP_Label = customtkinter.CTkLabel(scrollable_frame2, text="Repair/Production", font=("Helvetica", 20))
RP_Label.pack()

# question 154
Q154_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="What level of repair do you allow your service provider to perform?")
Q154_Label.pack()

Q154_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q154_Entry.pack(pady=10)
entries.append(Q154_Entry)

# question 155
Q155_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="Do you allow your service provider to harvest core parts from BERs and Scraps?")
Q155_Label.pack()

Q155_Entry = customtkinter.CTkComboBox(scrollable_frame2, values=["", "Yes", "No"])
Q155_Entry.pack(pady=10)
entries.append(Q155_Entry)

# question 156
Q156_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="Do you allow your service provider to perform cosmetic repair?")
Q156_Label.pack()

Q156_Entry = customtkinter.CTkComboBox(scrollable_frame2, values=["", "Yes", "No"])
Q156_Entry.pack(pady=10)
entries.append(Q156_Entry)

# question 157
Q157_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="How do you provide repair parts to service provider, consignment or purchase?")
Q157_Label.pack()

Q157_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q157_Entry.pack(pady=10)
entries.append(Q157_Entry)

# question 158
Q158_Label = customtkinter.CTkLabel(scrollable_frame2, text="What is your current lead time for repair parts?")
Q158_Label.pack()

Q158_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q158_Entry.pack(pady=10)
entries.append(Q158_Entry)

# question 159
Q159_Label = customtkinter.CTkLabel(scrollable_frame2, text="What is your expected yield rate from the total return?")
Q159_Label.pack()

Q159_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q159_Entry.pack(pady=10)
entries.append(Q159_Entry)

# question 160
Q160_Label = customtkinter.CTkLabel(scrollable_frame2, text="Do you provide enough seedstock when yield rate is lower "
                                                            "than the requirements resulted from higher L3, RTM, BER?")
Q160_Label.pack()

Q160_Entry = customtkinter.CTkComboBox(scrollable_frame2, values=["", "Yes", "No"])
Q160_Entry.pack(pady=10)
entries.append(Q160_Entry)

# question 161
Q161_Label = customtkinter.CTkLabel(scrollable_frame2, text="What is your KPI such as TAT, bounce rate, yield rate, "
                                                            "quality and what are the exceptions for each one of them?")
Q161_Label.pack()

Q161_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q161_Entry.pack(pady=10)
entries.append(Q161_Entry)

# Repair proccess label
RP_Label = customtkinter.CTkLabel(scrollable_frame2, text="Please provide your repair process flow chart by different "
                                                          "repair level.\nAlso, provide us with general time study "
                                                          "for each repair level including SW update & testing.")
RP_Label.pack(pady=10)

# Scrap process label
SP_Label = customtkinter.CTkLabel(scrollable_frame2,
                                  text="Please provide your scrap process for defective device, PCBA, parts.")
SP_Label.pack(pady=10)

# Service manual label
SM_Label = customtkinter.CTkLabel(scrollable_frame2, text="Please provide repair BOM, SLA, and Service manual")
SM_Label.pack(pady=10)

# Swap label
Swap_Label = customtkinter.CTkLabel(scrollable_frame2, text="Please provide device and PCBA swap process")
Swap_Label.pack(pady=10)

# question 162
Q162_Label = customtkinter.CTkLabel(scrollable_frame2, text="Do you require multiple testing if a device fails at "
                                                            "functional test such as RF test at first?\nIf so, "
                                                            "what is the requirements of maximum number of time?")
Q162_Label.pack()

Q162_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q162_Entry.pack(pady=10)
entries.append(Q162_Entry)

# question 163
Q163_Label = customtkinter.CTkLabel(scrollable_frame2,
                                    text="Do you need supports on EWP, DOA, FAI? If so, please provide the process flow charts")
Q163_Label.pack()

Q163_Entry = customtkinter.CTkComboBox(scrollable_frame2, values=["", "Yes", "No"])
Q163_Entry.pack(pady=10)
entries.append(Q163_Entry)

# question 164
Q164_Label = customtkinter.CTkLabel(scrollable_frame2, text="What are your reporting requirements?")
Q164_Label.pack()

Q164_Entry = customtkinter.CTkEntry(scrollable_frame2, placeholder_text="Enter your answer here", width=250)
Q164_Entry.pack(pady=10)
entries.append(Q164_Entry)

# THIS IS THE START OF TAB 3 FOR LCH

# LCH label
LCH_Label = customtkinter.CTkLabel(scrollable_frame3, text="Life Cycle Services", font=("Helvetica", 20))
LCH_Label.pack(pady=10)

# LCH/LCS Services Scope and Questions label
LCHSQ_Label = customtkinter.CTkLabel(scrollable_frame3, text="LCH/LCS Services Scope and Questions",
                                     font=("Helvetica", 20))
LCHSQ_Label.pack(pady=10)

# question 165
Q165_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="What is the OEM and model of the devices that will be supported?")
Q165_Label.pack()

Q165_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q165_Entry.pack(pady=10)
entries.append(Q165_Entry)

# question 166
Q166_Label = customtkinter.CTkLabel(scrollable_frame3, text="How many locations will be supported?")
Q166_Label.pack()

Q166_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q166_Entry.pack(pady=10)
entries.append(Q166_Entry)

# question 167
Q167_Label = customtkinter.CTkLabel(scrollable_frame3, text="What are the locations?")
Q167_Label.pack()

Q167_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q167_Entry.pack(pady=10)
entries.append(Q167_Entry)

# question 168
Q168_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="What is the estimated volume of seedstock on hand at all times to support monthly ticket volumes?")
Q168_Label.pack()

Q168_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q168_Entry.pack(pady=10)
entries.append(Q168_Entry)

# question 169
Q169_Label = customtkinter.CTkLabel(scrollable_frame3, text="Laptop qty?")
Q169_Label.pack()

Q169_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q169_Entry.pack(pady=10)
entries.append(Q169_Entry)

# question 170
Q170_Label = customtkinter.CTkLabel(scrollable_frame3, text="Desktop qty?")
Q170_Label.pack()

Q170_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q170_Entry.pack(pady=10)
entries.append(Q170_Entry)

# question 171
Q171_Label = customtkinter.CTkLabel(scrollable_frame3, text="Docking Stations Qty?")
Q171_Label.pack()

Q171_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q171_Entry.pack(pady=10)
entries.append(Q171_Entry)

# question 172
Q172_Label = customtkinter.CTkLabel(scrollable_frame3, text="Monitors (denote if different sizes per the above)")
Q172_Label.pack()

Q172_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q172_Entry.pack(pady=10)
entries.append(Q172_Entry)

# question 173
Q173_Label = customtkinter.CTkLabel(scrollable_frame3, text="K/M")
Q173_Label.pack()

Q173_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q173_Entry.pack(pady=10)
entries.append(Q173_Entry)

# Service Communications label
SC_Label = customtkinter.CTkLabel(scrollable_frame3, text="Service Communications", font=("Helvetica", 20))
SC_Label.pack(pady=10)

# question 174
Q174_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="Will communication be done through e-mail distribution, \nor ticketing system integration to requests event type fulfillment?")
Q174_Label.pack()

Q174_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q174_Entry.pack(pady=10)
entries.append(Q174_Entry)

# question 175
Q175_Label = customtkinter.CTkLabel(scrollable_frame3, text="What hours will services be performed?")
Q175_Label.pack()

Q175_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q175_Entry.pack(pady=10)
entries.append(Q175_Entry)

# SLA's label
SLA_Label = customtkinter.CTkLabel(scrollable_frame3, text="SLA's", font=("Helvetica", 20))
SLA_Label.pack(pady=10)

# question 176
Q176_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="What is the SLA for tickets received to shipped out? (per event type)")
Q176_Label.pack()

Q176_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q176_Entry.pack(pady=10)
entries.append(Q176_Entry)

# question 177
Q177_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="What percent of tickets will be urgent, same day requests?")
Q177_Label.pack()

Q177_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q177_Entry.pack(pady=10)
entries.append(Q177_Entry)

# question 178
Q178_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="What is the preferred cutoff time for same day and next day requests?")
Q178_Label.pack()

Q178_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q178_Entry.pack(pady=10)
entries.append(Q178_Entry)

# Kitting label
K_Label = customtkinter.CTkLabel(scrollable_frame3, text="Kitting", font=("Helvetica", 20))
K_Label.pack(pady=10)

# question 179
Q179_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="Does Premier need to perform kitting services or only perform order consolidation\n(i.e.,  Premier only sets up equipment that has specifically been requested)?")
Q179_Label.pack()

Q179_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q179_Entry.pack(pady=10)
entries.append(Q179_Entry)

# question 180
Q180_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="What are the items that will need to be kitted with system?")
Q180_Label.pack()

Q180_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q180_Entry.pack(pady=10)
entries.append(Q180_Entry)

# question 181
Q181_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="Does Premier need to include a ground return shipping label in the box for any assets to be sent back to Premier?")
Q181_Label.pack()

Q181_Entry = customtkinter.CTkComboBox(scrollable_frame3, values=["", "Yes", "No"])
Q181_Entry.pack(pady=10)
entries.append(Q181_Entry)

# question 182
Q182_Label = customtkinter.CTkLabel(scrollable_frame3, text="What event types require kitting services?")
Q182_Label.pack()

Q182_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q182_Entry.pack(pady=10)
entries.append(Q182_Entry)

# question 183
Q183_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="If so, will Premier need to report against this return tracking number?")
Q183_Label.pack()

Q183_Entry = customtkinter.CTkComboBox(scrollable_frame3, values=["", "Yes", "No"])
Q183_Entry.pack(pady=10)
entries.append(Q183_Entry)

# Cofiguration label
C_Label = customtkinter.CTkLabel(scrollable_frame3, text="Configuration", font=("Helvetica", 20))
C_Label.pack(pady=10)

# question 184
Q184_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="What imaging solution will be utilized for the configuration of devices?")
Q184_Label.pack()

Q184_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q184_Entry.pack(pady=10)
entries.append(Q184_Entry)

# question 185
Q185_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="If using a connected solution, what hardware will be stored at Premier?")
Q185_Label.pack()

Q185_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q185_Entry.pack(pady=10)
entries.append(Q185_Entry)

# question 186
Q186_Label = customtkinter.CTkLabel(scrollable_frame3, text="What is the expected touch time to deploy the image?")
Q186_Label.pack()

Q186_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q186_Entry.pack(pady=10)
entries.append(Q186_Entry)

# question 187
Q187_Label = customtkinter.CTkLabel(scrollable_frame3, text="What is the expected bench time to deploy the image?")
Q187_Label.pack()

Q187_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q187_Entry.pack(pady=10)
entries.append(Q187_Entry)

# question 188
Q188_Label = customtkinter.CTkLabel(scrollable_frame3, text="Are any BIOS Settings required?")
Q188_Label.pack()

Q188_Entry = customtkinter.CTkComboBox(scrollable_frame3, values=["", "Yes", "No"])
Q188_Entry.pack(pady=10)
entries.append(Q188_Entry)

# Wipe and Disposal label
WD_Label = customtkinter.CTkLabel(scrollable_frame3, text="Wipe and Disposal", font=("Helvetica", 20))
WD_Label.pack(pady=10)

# question 189
Q189_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="What even types require a hard drive wipe for a returned asset?")
Q189_Label.pack()

Q189_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q189_Entry.pack(pady=10)
entries.append(Q189_Entry)

# question 190
Q190_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="What are the data wipe requirements? (i.e. 3 pass, 7 pass, NIST compliant)")
Q190_Label.pack()

Q190_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q190_Entry.pack(pady=10)
entries.append(Q190_Entry)

# question 191
Q191_Label = customtkinter.CTkLabel(scrollable_frame3, text="Is an individual COD required for each HD wipe?")
Q191_Label.pack()

Q191_Entry = customtkinter.CTkComboBox(scrollable_frame3, values=["", "Yes", "No"])
Q191_Entry.pack(pady=10)
entries.append(Q191_Entry)

# question 192
Q192_Label = customtkinter.CTkLabel(scrollable_frame3, text="How long do COD's need to be retained?")
Q192_Label.pack()

Q192_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q192_Entry.pack(pady=10)
entries.append(Q192_Entry)

# question 193
Q193_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="Will HD wipes be required as a one of line item, or blended into event rates?")
Q193_Label.pack()

Q193_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q193_Entry.pack(pady=10)
entries.append(Q193_Entry)

# question 194
Q194_Label = customtkinter.CTkLabel(scrollable_frame3, text="Are disposal services required?")
Q194_Label.pack()

Q194_Entry = customtkinter.CTkComboBox(scrollable_frame3, values=["", "Yes", "No"])
Q194_Entry.pack(pady=10)
entries.append(Q194_Entry)

# question 195
Q195_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="Will disposal be managed through Premier, or Customer provider?")
Q195_Label.pack()

Q195_Entry = customtkinter.CTkComboBox(scrollable_frame3, values=["", "Premier", "Customer"])
Q195_Entry.pack(pady=10)
entries.append(Q195_Entry)

# Asset Tagging label
AT_Label = customtkinter.CTkLabel(scrollable_frame3, text="Asset Tagging", font=("Helvetica", 20))
AT_Label.pack(pady=10)

# question 196
Q196_Label = customtkinter.CTkLabel(scrollable_frame3, text="What event types require asset tagging services?")
Q196_Label.pack()

Q196_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q196_Entry.pack(pady=10)
entries.append(Q196_Entry)

# question 197
Q197_Label = customtkinter.CTkLabel(scrollable_frame3, text="Are asset tags Premier, or customer provided?")
Q197_Label.pack()

Q197_Entry = customtkinter.CTkComboBox(scrollable_frame3, values=["", "Premier", "Customer"])
Q197_Entry.pack(pady=10)
entries.append(Q197_Entry)

# question 198
Q198_Label = customtkinter.CTkLabel(scrollable_frame3, text="What is the approximate size and color of the asset tag?")
Q198_Label.pack()

Q198_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q198_Entry.pack(pady=10)
entries.append(Q198_Entry)

# question 199
Q199_Label = customtkinter.CTkLabel(scrollable_frame3, text="Are asset tags serial number specific?")
Q199_Label.pack()

Q199_Entry = customtkinter.CTkComboBox(scrollable_frame3, values=["", "Yes", "No"])
Q199_Entry.pack(pady=10)
entries.append(Q199_Entry)

# question 200
Q200_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="How are damaged asset tags handled when returned back to Premier?")
Q200_Label.pack()

Q200_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q200_Entry.pack(pady=10)
entries.append(Q200_Entry)

# question 201
Q201_Label = customtkinter.CTkLabel(scrollable_frame3, text="How many asset tags per system?")
Q201_Label.pack()

Q201_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q201_Entry.pack(pady=10)
entries.append(Q201_Entry)

# question 202
Q202_Label = customtkinter.CTkLabel(scrollable_frame3, text="Will asset tag values need to be reported to end user?")
Q202_Label.pack()

Q202_Entry = customtkinter.CTkComboBox(scrollable_frame3, values=["", "Yes", "No"])
Q202_Entry.pack(pady=10)
entries.append(Q202_Entry)

# ONB - (On Boarding) label
ONB_Label = customtkinter.CTkLabel(scrollable_frame3, text="ONB - (On Boarding)", font=("Helvetica", 20))
ONB_Label.pack(pady=10)

# question 203
Q203_Label = customtkinter.CTkLabel(scrollable_frame3, text="Tickets per month?")
Q203_Label.pack()

Q203_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q203_Entry.pack(pady=10)
entries.append(Q203_Entry)

# question 204
Q204_Label = customtkinter.CTkLabel(scrollable_frame3, text="Assets included in an ONB and qty")
Q204_Label.pack()

Q204_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q204_Entry.pack(pady=10)
entries.append(Q204_Entry)

# question 205
Q205_Label = customtkinter.CTkLabel(scrollable_frame3, text="System OEM/Model – Qty?")
Q205_Label.pack()

Q205_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q205_Entry.pack(pady=10)
entries.append(Q205_Entry)

# question 206
Q206_Label = customtkinter.CTkLabel(scrollable_frame3, text="Monitor OEM/Model – Qty?")
Q206_Label.pack()

Q206_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q206_Entry.pack(pady=10)
entries.append(Q206_Entry)

# question 207
Q207_Label = customtkinter.CTkLabel(scrollable_frame3, text="Peripherals OEM/Model – Qty?")
Q207_Label.pack()

Q207_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q207_Entry.pack(pady=10)
entries.append(Q207_Entry)

# OFB (Off Boarding) /Leaver label
OFB_Label = customtkinter.CTkLabel(scrollable_frame3, text="OFB (Off Boarding) /Leaver", font=("Helvetica", 20))
OFB_Label.pack(pady=10)

# question 208
Q208_Label = customtkinter.CTkLabel(scrollable_frame3, text="Tickets per month?")
Q208_Label.pack()

Q208_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q208_Entry.pack(pady=10)
entries.append(Q208_Entry)

# question 209
Q209_Label = customtkinter.CTkLabel(scrollable_frame3, text="Assets included in an OFB and qty")
Q209_Label.pack()

Q209_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q209_Entry.pack(pady=10)
entries.append(Q209_Entry)

# question 210
Q210_Label = customtkinter.CTkLabel(scrollable_frame3, text="System OEM/Model – Qty?")
Q210_Label.pack()

Q210_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q210_Entry.pack(pady=10)
entries.append(Q210_Entry)

# question 211
Q211_Label = customtkinter.CTkLabel(scrollable_frame3, text="Monitor OEM/Model – Qty?")
Q211_Label.pack()

Q211_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q211_Entry.pack(pady=10)
entries.append(Q211_Entry)

# question 212
Q212_Label = customtkinter.CTkLabel(scrollable_frame3, text="Peripherals OEM/Model – Qty")
Q212_Label.pack()

Q212_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q212_Entry.pack(pady=10)
entries.append(Q212_Entry)

# question 213
Q213_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="Will Premier need to send boxing material to end user to return to depot?")
Q213_Label.pack()

Q213_Entry = customtkinter.CTkComboBox(scrollable_frame3, values=["", "Yes", "No"])
Q213_Entry.pack(pady=10)
entries.append(Q213_Entry)

# question 214
Q214_Label = customtkinter.CTkLabel(scrollable_frame3, text="Should Premier assume all systems are under warranty and "
                                                            "in good working order?\nIf not, "
                                                            "what is disposition/repair process?")
Q214_Label.pack()

Q214_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q214_Entry.pack(pady=10)
entries.append(Q214_Entry)

# question 215
Q215_Label = customtkinter.CTkLabel(scrollable_frame3, text="If not under warranty. will be a non-warranty repair be "
                                                            "a one-off process\nuse an hourly rate in 30 min "
                                                            "intervals for support/service; \nPremier will need value "
                                                            "thresholds for repairing OOW")
Q215_Label.pack()

Q215_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q215_Entry.pack(pady=10)
entries.append(Q215_Entry)

# AE (Advanced Exchange/Break Fix) label
AE_Label = customtkinter.CTkLabel(scrollable_frame3, text="AE (Advanced Exchange/Break Fix)", font=("Helvetica", 20))
AE_Label.pack(pady=10)

# question 216
Q216_Label = customtkinter.CTkLabel(scrollable_frame3, text="Tickets per month?")
Q216_Label.pack()

Q216_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q216_Entry.pack(pady=10)
entries.append(Q216_Entry)

# question 217
Q217_Label = customtkinter.CTkLabel(scrollable_frame3, text="Assets included in an AE/BF and qty")
Q217_Label.pack()

Q217_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q217_Entry.pack(pady=10)
entries.append(Q217_Entry)

# question 218
Q218_Label = customtkinter.CTkLabel(scrollable_frame3, text="System OEM/Model – Qty?")
Q218_Label.pack()

Q218_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q218_Entry.pack(pady=10)
entries.append(Q218_Entry)

# question 219
Q219_Label = customtkinter.CTkLabel(scrollable_frame3, text="Monitor OEM/Model – Qty?")
Q219_Label.pack()

Q219_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q219_Entry.pack(pady=10)
entries.append(Q219_Entry)

# question 220
Q220_Label = customtkinter.CTkLabel(scrollable_frame3, text="Peripherals OEM/Model – Qty")
Q220_Label.pack()

Q220_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q220_Entry.pack(pady=10)
entries.append(Q220_Entry)

# question 221
Q221_Label = customtkinter.CTkLabel(scrollable_frame3, text="Assuming assets under warranty? If No, more details?")
Q221_Label.pack()

Q221_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q221_Entry.pack(pady=10)
entries.append(Q221_Entry)

# question 222
Q222_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="Will packing material need to be provided, or will customer use OEM packaging provided with the replacement unit?")
Q222_Label.pack()

Q222_Entry = customtkinter.CTkComboBox(scrollable_frame3, values=["", "Yes", "No"])
Q222_Entry.pack(pady=10)
entries.append(Q222_Entry)

# question 223
Q223_Label = customtkinter.CTkLabel(scrollable_frame3, text="Will all units still be under warranty?")
Q223_Label.pack()

Q223_Entry = customtkinter.CTkComboBox(scrollable_frame3, values=["", "Yes", "No"])
Q223_Entry.pack(pady=10)
entries.append(Q223_Entry)

# question 224
Q224_Label = customtkinter.CTkLabel(scrollable_frame3, text="Will Premier, OEM, or Customer handle repair of the unit?")
Q224_Label.pack()

Q224_Entry = customtkinter.CTkComboBox(scrollable_frame3, values=["", "Premier", "OEM", "Customer"])
Q224_Entry.pack(pady=10)
entries.append(Q224_Entry)

# question 225
Q225_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="How much warranty must be left on a returned asset to be eligible to be moved to ready stock?")
Q225_Label.pack()

Q225_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q225_Entry.pack(pady=10)
entries.append(Q225_Entry)

# Upgrade/Refresh label
UR_Label = customtkinter.CTkLabel(scrollable_frame3, text="Upgrade/Refresh", font=("Helvetica", 20))
UR_Label.pack(pady=10)

# question 226
Q226_Label = customtkinter.CTkLabel(scrollable_frame3, text="Tickets per month - ?")
Q226_Label.pack()

Q226_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q226_Entry.pack(pady=10)
entries.append(Q226_Entry)

# question 227
Q227_Label = customtkinter.CTkLabel(scrollable_frame3, text="Assets included in an Upgrade")
Q227_Label.pack()

Q227_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q227_Entry.pack(pady=10)
entries.append(Q227_Entry)

# question 228
Q228_Label = customtkinter.CTkLabel(scrollable_frame3, text="System OEM/Model – Qty?")
Q228_Label.pack()

Q228_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q228_Entry.pack(pady=10)
entries.append(Q228_Entry)

# question 229
Q229_Label = customtkinter.CTkLabel(scrollable_frame3, text="Monitor OEM/Model – Qty?")
Q229_Label.pack()

Q229_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q229_Entry.pack(pady=10)
entries.append(Q229_Entry)

# question 230
Q230_Label = customtkinter.CTkLabel(scrollable_frame3, text="Peripherals OEM/Model – Qty?")
Q230_Label.pack()

Q230_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q230_Entry.pack(pady=10)
entries.append(Q230_Entry)

# question 231
Q231_Label = customtkinter.CTkLabel(scrollable_frame3, text="Will refreshed devices be returned to Premier?")
Q231_Label.pack()

Q231_Entry = customtkinter.CTkComboBox(scrollable_frame3, values=["", "Yes", "No"])
Q231_Entry.pack(pady=10)
entries.append(Q231_Entry)

# question 232
Q232_Label = customtkinter.CTkLabel(scrollable_frame3, text="If so, what items will be included in the return?")
Q232_Label.pack()

Q232_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q232_Entry.pack(pady=10)
entries.append(Q232_Entry)

# question 233
Q233_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="Will Premier need to send boxing material to end user to return to depot?")
Q233_Label.pack()

Q233_Entry = customtkinter.CTkComboBox(scrollable_frame3, values=["", "Yes", "No"])
Q233_Entry.pack(pady=10)
entries.append(Q233_Entry)

# question 234
Q234_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="How will the Customer provide Premier returned asset information prior to arrival at Premier's  warehouse?")
Q234_Label.pack()

Q234_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q234_Entry.pack(pady=10)
entries.append(Q234_Entry)

# question 235
Q235_Label = customtkinter.CTkLabel(scrollable_frame3, text="What is your refresh cycle: (i.e., 3 years, 4 years etc.)")
Q235_Label.pack()

Q235_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q235_Entry.pack(pady=10)
entries.append(Q235_Entry)

# question 236
Q236_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="Will any bulk refreshed be performed? (i.e. groups of units sent to distribution centers)")
Q236_Label.pack()

Q236_Entry = customtkinter.CTkComboBox(scrollable_frame3, values=["", "Yes", "No"])
Q236_Entry.pack(pady=10)
entries.append(Q236_Entry)

# Shipping label
S_Label = customtkinter.CTkLabel(scrollable_frame3, text="Shipping", font=("Helvetica", 20))
S_Label.pack(pady=10)

# question 237
Q237_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="Are any Customer or End-Customer locations OCONUS (defined as locations outside the continental US). \nIf yes. what percentage of total systems are in OCONUS sites? or Provide the number of _OCONUS systems.  \nProvide specific address and quantities per site.")
Q237_Label.pack()

Q237_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q237_Entry.pack(pady=10)
entries.append(Q237_Entry)

# question 238
Q238_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="Office locations;  specify the number of site and ship-to addresses")
Q238_Label.pack()

Q238_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q238_Entry.pack(pady=10)
entries.append(Q238_Entry)

# question 239
Q239_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="End user locations; specify the number of site and ship-to addresses")
Q239_Label.pack()

Q239_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q239_Entry.pack(pady=10)
entries.append(Q239_Entry)

# question 240
Q240_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="Will Premier use Reseller, Customer, or own shipping account?")
Q240_Label.pack()

Q240_Entry = customtkinter.CTkComboBox(scrollable_frame3, values=["", "Reseller", "Customer", "Own"])
Q240_Entry.pack(pady=10)
entries.append(Q240_Entry)

# question 241
Q241_Label = customtkinter.CTkLabel(scrollable_frame3,
                                    text="What is the expected service level for shipping by event type?")
Q241_Label.pack()

Q241_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q241_Entry.pack(pady=10)
entries.append(Q241_Entry)

# question 242
Q242_Label = customtkinter.CTkLabel(scrollable_frame3, text="What is expected daily shipment qty?")
Q242_Label.pack()

Q242_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q242_Entry.pack(pady=10)
entries.append(Q242_Entry)

# question 243
Q243_Label = customtkinter.CTkLabel(scrollable_frame3, text="How will the Customer provide Premier returned asset "
                                                            "information prior to arrival at Premier?")
Q243_Label.pack()

Q243_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q243_Entry.pack(pady=10)
entries.append(Q243_Entry)

# Contract Term & Pricing label
CTP_Label = customtkinter.CTkLabel(scrollable_frame3, text="Contract Term & Pricing", font=("Helvetica", 20))
CTP_Label.pack(pady=10)

# question 244
Q244_Label = customtkinter.CTkLabel(scrollable_frame3, text="What are the contract terms")
Q244_Label.pack()

Q244_Entry = customtkinter.CTkEntry(scrollable_frame3, placeholder_text="Enter your answer here", width=250)
Q244_Entry.pack(pady=10)
entries.append(Q244_Entry)

# Include a T&M rate table for Out of Warranty (OOW) repair services label
ITM_Label = customtkinter.CTkLabel(scrollable_frame3, text="Include a T&M rate table for Out of Warranty (OOW) repair "
                                                           "services")
ITM_Label.pack(pady=10)

# question 245
Q245_Label = customtkinter.CTkLabel(scrollable_frame3, text="Will shipping costs be handled by customer or partner "
                                                            "account?")
Q245_Label.pack()

Q245_Entry = customtkinter.CTkComboBox(scrollable_frame3, values=["", "Customer", "Partner"])
Q245_Entry.pack(pady=10)
entries.append(Q245_Entry)

# question 246
Q246_Label = customtkinter.CTkLabel(scrollable_frame3, text="Will setup fees be billed in a single up front fee, "
                                                            "or blended into the event fees?")
Q246_Label.pack()

Q246_Entry = customtkinter.CTkComboBox(scrollable_frame3, values=["", "Single", "Blended"])
Q246_Entry.pack(pady=10)
entries.append(Q246_Entry)

# THE FOLLOWING SECTION IS FOR THE TECHNOLOGY SERVICES TAB

# Technology Services label
TS_Label = customtkinter.CTkLabel(scrollable_frame4, text="Technology Services", font=("Helvetica", 20))
TS_Label.pack(pady=10)

# Basic Customer Information label
BCI_Label = customtkinter.CTkLabel(scrollable_frame4, text="Basic Customer Information", font=("Helvetica", 20))
BCI_Label.pack(pady=10)

# question 247
Q247_Label = customtkinter.CTkLabel(scrollable_frame4, text="Customer Name")
Q247_Label.pack()

Q247_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q247_Entry.pack(pady=10)
entries.append(Q247_Entry)

# question 248
Q248_Label = customtkinter.CTkLabel(scrollable_frame4, text="Partner")
Q248_Label.pack()

Q248_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q248_Entry.pack(pady=10)
entries.append(Q248_Entry)

# question 249
Q249_Label = customtkinter.CTkLabel(scrollable_frame4, text="Mailing Address")
Q249_Label.pack()

Q249_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q249_Entry.pack(pady=10)
entries.append(Q249_Entry)

# question 250
Q250_Label = customtkinter.CTkLabel(scrollable_frame4, text="Location Address")
Q250_Label.pack()

Q250_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q250_Entry.pack(pady=10)
entries.append(Q250_Entry)

# question 251
Q251_Label = customtkinter.CTkLabel(scrollable_frame4, text="City")
Q251_Label.pack()

Q251_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q251_Entry.pack(pady=10)
entries.append(Q251_Entry)

# question 252
Q252_Label = customtkinter.CTkLabel(scrollable_frame4, text="State")
Q252_Label.pack()

Q252_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q252_Entry.pack(pady=10)
entries.append(Q252_Entry)

# question 253
Q253_Label = customtkinter.CTkLabel(scrollable_frame4, text="Zip Code")
Q253_Label.pack()

Q253_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q253_Entry.pack(pady=10)
entries.append(Q253_Entry)

# question 254
Q254_Label = customtkinter.CTkLabel(scrollable_frame4, text="Deal ID")
Q254_Label.pack()

Q254_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q254_Entry.pack(pady=10)
entries.append(Q254_Entry)

# question 255
Q255_Label = customtkinter.CTkLabel(scrollable_frame4, text="Customer Segment")
Q255_Label.pack()

Q255_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q255_Entry.pack(pady=10)
entries.append(Q255_Entry)

# question 256
Q256_Label = customtkinter.CTkLabel(scrollable_frame4, text="Expected inbound order volume (# of ASN uploads)")
Q256_Label.pack()

Q256_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q256_Entry.pack(pady=10)
entries.append(Q256_Entry)

# question 257
Q257_Label = customtkinter.CTkLabel(scrollable_frame4, text="Expected outbound shipment volume (# of shipment uploads)")
Q257_Label.pack()

Q257_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q257_Entry.pack(pady=10)
entries.append(Q257_Entry)

# question 258
Q258_Label = customtkinter.CTkLabel(scrollable_frame4, text="Where are we configuring systems? ")
Q258_Label.pack()

Q258_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q258_Entry.pack(pady=10)
entries.append(Q258_Entry)

# question 259
Q259_Label = customtkinter.CTkLabel(scrollable_frame4, text="Are we deploying systems at Customer site(s)? ")
Q259_Label.pack()

Q259_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q259_Entry.pack(pady=10)
entries.append(Q259_Entry)

# question 260
Q260_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will receive equipment at our warehouse?")
Q260_Label.pack()

Q260_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q260_Entry.pack(pady=10)
entries.append(Q260_Entry)

# Shipping information label
SI_Label = customtkinter.CTkLabel(scrollable_frame4, text="Shipping information", font=("Helvetica", 20))
SI_Label.pack(pady=10)

# question 261
Q261_Label = customtkinter.CTkLabel(scrollable_frame4, text="Do we need to ship equipment to customer?")
Q261_Label.pack()

Q261_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q261_Entry.pack(pady=10)
entries.append(Q261_Entry)

# question 262
Q262_Label = customtkinter.CTkLabel(scrollable_frame4, text="Are we able to utilize Dell/Customer shipping account?")
Q262_Label.pack()

Q262_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q262_Entry.pack(pady=10)
entries.append(Q262_Entry)

# question 263
Q263_Label = customtkinter.CTkLabel(scrollable_frame4, text="What % of shipments will be FTL?")
Q263_Label.pack()

Q263_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q263_Entry.pack(pady=10)
entries.append(Q263_Entry)

# question 264
Q264_Label = customtkinter.CTkLabel(scrollable_frame4, text="What % of shipments will be LTL?")
Q264_Label.pack()

Q264_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q264_Entry.pack(pady=10)
entries.append(Q264_Entry)

# question 265
Q265_Label = customtkinter.CTkLabel(scrollable_frame4, text="What % of shipments will be Parcel?")
Q265_Label.pack()

Q265_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q265_Entry.pack(pady=10)
entries.append(Q265_Entry)

# question 266
Q266_Label = customtkinter.CTkLabel(scrollable_frame4, text="Are there any Special Delivery Requirements?")
Q266_Label.pack()

Q266_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q266_Entry.pack(pady=10)
entries.append(Q266_Entry)

# question 267
Q267_Label = customtkinter.CTkLabel(scrollable_frame4, text="Are any locations OCONUS (defined as outside the "
                                                            "continental US)? \nWhat percentage of systems will ship "
                                                            "to OCONUS sites, if any? \nProvide specific address and "
                                                            "quantities per site.")
Q267_Label.pack()

Q267_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q267_Entry.pack(pady=10)
entries.append(Q267_Entry)

# question 268
Q268_Label = customtkinter.CTkLabel(scrollable_frame4, text="How many CONUS locations will we be shipping to,\n"
                                                            "how many shipments and qty per shipment,\nand physical "
                                                            "address of each site?")
Q268_Label.pack()

Q268_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q268_Entry.pack(pady=10)
entries.append(Q268_Entry)

# question 269
Q269_Label = customtkinter.CTkLabel(scrollable_frame4, text="Are there any special circumstances Premier needs to be "
                                                            "aware of at the individual sites \n(i.e. no elevators, "
                                                            "no carts allowed in bldg., etc.)?")

Q269_Label.pack()

Q269_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q269_Entry.pack(pady=10)
entries.append(Q269_Entry)

# question 270
Q270_Label = customtkinter.CTkLabel(scrollable_frame4, text="Are there any special packaging, or pallet preparation "
                                                            "requirements?")
Q270_Label.pack()

Q270_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q270_Entry.pack(pady=10)
entries.append(Q270_Entry)

# question 271
Q271_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="Are there are height or capacity restrictions for delivery sites?")
Q271_Label.pack()

Q271_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q271_Entry.pack(pady=10)
entries.append(Q271_Entry)

# Warehouse Information label
WI_Label = customtkinter.CTkLabel(scrollable_frame4, text="Warehouse Information", font=("Helvetica", 20))
WI_Label.pack(pady=10)

# question 272
Q272_Label = customtkinter.CTkLabel(scrollable_frame4, text="What systems (models) & qty of each item will we be "
                                                            "receiving?")
Q272_Label.pack()

Q272_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q272_Entry.pack(pady=10)
entries.append(Q272_Entry)

# question 273
Q273_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="What monitors (models) & qty of each item will we be receiving?")
Q273_Label.pack()

Q273_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q273_Entry.pack(pady=10)
entries.append(Q273_Entry)

# question 274
Q274_Label = customtkinter.CTkLabel(scrollable_frame4, text="What peripherals & qty of each item will we be receiving?")
Q274_Label.pack()

Q274_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q274_Entry.pack(pady=10)
entries.append(Q274_Entry)

# question 275
Q275_Label = customtkinter.CTkLabel(scrollable_frame4, text="How many months will we need to warehouse the equipment?")
Q275_Label.pack()

Q275_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q275_Entry.pack(pady=10)
entries.append(Q275_Entry)

# question 276
Q276_Label = customtkinter.CTkLabel(scrollable_frame4, text="Any special warehouse requirements?")
Q276_Label.pack()

Q276_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q276_Entry.pack(pady=10)
entries.append(Q276_Entry)

# question 277
Q277_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will we receive any laptop/Chromebook carts?")
Q277_Label.pack()

Q277_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q277_Entry.pack(pady=10)
entries.append(Q277_Entry)

# question 278
Q278_Label = customtkinter.CTkLabel(scrollable_frame4, text="If so, do the carts need to be pre-wired?")
Q278_Label.pack()

Q278_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q278_Entry.pack(pady=10)
entries.append(Q278_Entry)

# Asset Tag Information label
ATI_Label = customtkinter.CTkLabel(scrollable_frame4, text="Asset Tag Information", font=("Helvetica", 20))
ATI_Label.pack(pady=10)

# question 279
Q279_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will the new system and/or peripherals need to be asset "
                                                            "tagged?")
Q279_Label.pack()

Q279_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q279_Entry.pack(pady=10)
entries.append(Q279_Entry)

# question 280
Q280_Label = customtkinter.CTkLabel(scrollable_frame4, text="If so, who will provide the asset tags?")
Q280_Label.pack()

Q280_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q280_Entry.pack(pady=10)
entries.append(Q280_Entry)

# question 281
Q281_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="What size do the asset tags need to be? \n(1.5 inch x 3 inch and 2 inch x 1 inch are standard)")
Q281_Label.pack()

Q281_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q281_Entry.pack(pady=10)
entries.append(Q281_Entry)

# question 282
Q282_Label = customtkinter.CTkLabel(scrollable_frame4, text="How many asset tags per system?")
Q282_Label.pack()

Q282_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "1", "2", "3", "4", "5"])
Q282_Entry.pack(pady=10)
entries.append(Q282_Entry)

# question 283
Q283_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="What color text is preferred? (Anything other than black is a significant upcharge)")
Q283_Label.pack()

Q283_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q283_Entry.pack(pady=10)
entries.append(Q283_Entry)

# question 284
Q284_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="What color tag is preferred? (Silver and white mylar are standard)")
Q284_Label.pack()

Q284_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q284_Entry.pack(pady=10)
entries.append(Q284_Entry)

# Box Label Information label
BLI_Label = customtkinter.CTkLabel(scrollable_frame4, text="Box Label Information", font=("Helvetica", 20))
BLI_Label.pack(pady=10)

# question 285
Q285_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="Will the new system and/or peripherals need to be box labeled?")
Q285_Label.pack()

Q285_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q285_Entry.pack(pady=10)
entries.append(Q285_Entry)

# question 286
Q286_Label = customtkinter.CTkLabel(scrollable_frame4, text="If so, who will provide the labels?")
Q286_Label.pack()

Q286_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q286_Entry.pack(pady=10)
entries.append(Q286_Entry)

# question 287
Q287_Label = customtkinter.CTkLabel(scrollable_frame4, text="What size do the box labels need to be? \n(1.5 inch x 3 "
                                                            "inch and 4 inch x 4 inch are standard)")
Q287_Label.pack()

Q287_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q287_Entry.pack(pady=10)
entries.append(Q287_Entry)

# question 288
Q288_Label = customtkinter.CTkLabel(scrollable_frame4, text="How many box labels per system?")
Q288_Label.pack()

Q288_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "1", "2", "3", "4", "5"])
Q288_Entry.pack(pady=10)
entries.append(Q288_Entry)

# question 289
Q289_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="What color text is preferred? (Anything other than black is a significant upcharge)")
Q289_Label.pack()

Q289_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q289_Entry.pack(pady=10)
entries.append(Q289_Entry)

# question 290
Q290_Label = customtkinter.CTkLabel(scrollable_frame4, text="What color tag is preferred? (white paper is standard)")
Q290_Label.pack()

Q290_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q290_Entry.pack(pady=10)
entries.append(Q290_Entry)

# Kitting and Overpack label
KO_Label = customtkinter.CTkLabel(scrollable_frame4, text="Kitting and Overpack", font=("Helvetica", 20))
KO_Label.pack(pady=10)

# question 291
Q291_Label = customtkinter.CTkLabel(scrollable_frame4, text="Are kitting or overpack services required?")
Q291_Label.pack()

Q291_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q291_Entry.pack(pady=10)
entries.append(Q291_Entry)

# question 292
Q292_Label = customtkinter.CTkLabel(scrollable_frame4, text="If so, what items will be kitted/overpacked?")
Q292_Label.pack()

Q292_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q292_Entry.pack(pady=10)
entries.append(Q292_Entry)

# question 293
Q293_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will there be standard defined kits? If so, how many?")
Q293_Label.pack()

Q293_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q293_Entry.pack(pady=10)
entries.append(Q293_Entry)

# question 294
Q294_Label = customtkinter.CTkLabel(scrollable_frame4, text="If not, how will kits be defined?")
Q294_Label.pack()

Q294_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q294_Entry.pack(pady=10)
entries.append(Q294_Entry)

# question 295
Q295_Label = customtkinter.CTkLabel(scrollable_frame4, text="Does the shipped asset report need to report what is "
                                                            "physically in each kit? \n(Master Carton reporting vs "
                                                            "generic asset report)")
Q295_Label.pack()

Q295_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q295_Entry.pack(pady=10)
entries.append(Q295_Entry)

# question 296
Q296_Label = customtkinter.CTkLabel(scrollable_frame4, text="Is any special labeling required for the kits? \nIf so, "
                                                            "please fill out box label portion as well.")
Q296_Label.pack()

Q296_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q296_Entry.pack(pady=10)
entries.append(Q296_Entry)

# Miscellaneous label
M_Label = customtkinter.CTkLabel(scrollable_frame4, text="Miscellaneous", font=("Helvetica", 20))
M_Label.pack(pady=10)

# question 297
Q297_Label = customtkinter.CTkLabel(scrollable_frame4, text="Is MAC address capture required?")
Q297_Label.pack()

Q297_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q297_Entry.pack(pady=10)
entries.append(Q297_Entry)

# question 298
Q298_Label = customtkinter.CTkLabel(scrollable_frame4, text="Are multipack services required?")
Q298_Label.pack()

Q298_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q298_Entry.pack(pady=10)
entries.append(Q298_Entry)

# question 299
Q299_Label = customtkinter.CTkLabel(scrollable_frame4, text="If so, what models and how many per box is requested?")
Q299_Label.pack()

Q299_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q299_Entry.pack(pady=10)
entries.append(Q299_Entry)

# BIOS Updates label
BU_Label = customtkinter.CTkLabel(scrollable_frame4, text="BIOS Updates", font=("Helvetica", 20))
BU_Label.pack(pady=10)

# question 300
Q300_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will any BIOS changes be required?")
Q300_Label.pack()

Q300_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q300_Entry.pack(pady=10)
entries.append(Q300_Entry)

# question 301
Q301_Label = customtkinter.CTkLabel(scrollable_frame4, text="If so, what changes are required?")
Q301_Label.pack()

Q301_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q301_Entry.pack(pady=10)
entries.append(Q301_Entry)

# question 302
Q302_Label = customtkinter.CTkLabel(scrollable_frame4, text="Are they different per model?")
Q302_Label.pack()

Q302_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q302_Entry.pack(pady=10)
entries.append(Q302_Entry)

# question 303
Q303_Label = customtkinter.CTkLabel(scrollable_frame4, text="Does the BIOS firmware need to be updated?")
Q303_Label.pack()

Q303_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q303_Entry.pack(pady=10)
entries.append(Q303_Entry)

# question 304
Q304_Label = customtkinter.CTkLabel(scrollable_frame4, text="Does the asset tag value need to be added to the BIOS?")
Q304_Label.pack()

Q304_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q304_Entry.pack(pady=10)
entries.append(Q304_Entry)

# Chromebook Enrollment label
CE_Label = customtkinter.CTkLabel(scrollable_frame4, text="Chromebook Enrollment", font=("Helvetica", 20))
CE_Label.pack(pady=10)

# question 305
Q305_Label = customtkinter.CTkLabel(scrollable_frame4, text="Are Chromebook enrollment services required")
Q305_Label.pack()

Q305_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q305_Entry.pack(pady=10)
entries.append(Q305_Entry)

# question 306
Q306_Label = customtkinter.CTkLabel(scrollable_frame4, text="How many environments will we be enrolling to?")
Q306_Label.pack()

Q306_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "1", "2", "3", "4", "5"])
Q306_Entry.pack(pady=10)
entries.append(Q306_Entry)

# question 307
Q307_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will OU group moves be required?")
Q307_Label.pack()

Q307_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q307_Entry.pack(pady=10)
entries.append(Q307_Entry)

# question 308
Q308_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will the asset tag need to be added to the admin console?")
Q308_Label.pack()

Q308_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q308_Entry.pack(pady=10)
entries.append(Q308_Entry)

# question 309
Q309_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="Will devices need to be shipped by OU? (palletized for LTL/FTL or delivery)")
Q309_Label.pack()

Q309_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q309_Entry.pack(pady=10)
entries.append(Q309_Entry)

# Static Image label
SI_Label = customtkinter.CTkLabel(scrollable_frame4, text="Static Image", font=("Helvetica", 20))
SI_Label.pack(pady=10)

# question 310
Q310_Label = customtkinter.CTkLabel(scrollable_frame4, text="If Premier will be using Customer/OEM imaging "
                                                            "process.\n a). how many minutes does it take to image"
                                                            "each system?\nb). how many systems can we image "
                                                            "concurrently?")
Q310_Label.pack()

Q310_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q310_Entry.pack(pady=10)
entries.append(Q310_Entry)

# question 311
Q311_Label = customtkinter.CTkLabel(scrollable_frame4, text="How many different images are there?")
Q311_Label.pack()

Q311_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "1", "2", "3", "4", "5"])
Q311_Entry.pack(pady=10)
entries.append(Q311_Entry)

# question 312
Q312_Label = customtkinter.CTkLabel(scrollable_frame4, text="How large are the images?")
Q312_Label.pack()

Q312_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q312_Entry.pack(pady=10)
entries.append(Q312_Entry)

# question 313
Q313_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="Will the image be in a sealed state once the image has been properly deployed?")
Q313_Label.pack()

Q313_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q313_Entry.pack(pady=10)
entries.append(Q313_Entry)

# question 314
Q314_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="Are there any post-image steps required? If so, what is total touch time?")
Q314_Label.pack()

Q314_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q314_Entry.pack(pady=10)
entries.append(Q314_Entry)

# question 315
Q315_Label = customtkinter.CTkLabel(scrollable_frame4, text="How often are updates to the image(s) made?")
Q315_Label.pack()

Q315_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q315_Entry.pack(pady=10)
entries.append(Q315_Entry)

# Connected Configuration label
CC_Label = customtkinter.CTkLabel(scrollable_frame4, text="Connected Configuration", font=("Helvetica", 20))
CC_Label.pack(pady=10)

# question 316
Q316_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="Are any security clearances or background checks required for access? If so, what are they?")
Q316_Label.pack()

Q316_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q316_Entry.pack(pady=10)
entries.append(Q316_Entry)

# question 317
Q317_Label = customtkinter.CTkLabel(scrollable_frame4, text="How will DP updates be communicated to Premier team?")
Q317_Label.pack()

Q317_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q317_Entry.pack(pady=10)
entries.append(Q317_Entry)

# question 318
Q318_Label = customtkinter.CTkLabel(scrollable_frame4, text="If Premier will be using Customer/OEM imaging "
                                                            "process.\na). How many minutes does it take to image each"
                                                            " system?\nb). How many systems can we image concurrently?")
Q318_Label.pack()

Q318_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q318_Entry.pack(pady=10)
entries.append(Q318_Entry)

# question 319
Q319_Label = customtkinter.CTkLabel(scrollable_frame4, text="How many different images are there?")
Q319_Label.pack()

Q319_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "1", "2", "3", "4", "5"])
Q319_Entry.pack(pady=10)
entries.append(Q319_Entry)

# question 320
Q320_Label = customtkinter.CTkLabel(scrollable_frame4, text="How large are the images?")
Q320_Label.pack()

Q320_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q320_Entry.pack(pady=10)
entries.append(Q320_Entry)

# question 321
Q321_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="Will the image be in a sealed state once the image has been properly deployed?")
Q321_Label.pack()

Q321_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q321_Entry.pack(pady=10)
entries.append(Q321_Entry)

# question 322
Q322_Label = customtkinter.CTkLabel(scrollable_frame4, text="Are there any post-image steps required?\nIf so, what is "
                                                            "total touch time?")
Q322_Label.pack()

Q322_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q322_Entry.pack(pady=10)
entries.append(Q322_Entry)

# question 323
Q323_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="What portion of image deployment are pulled over VPN vs local DP?")
Q323_Label.pack()

Q323_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q323_Entry.pack(pady=10)
entries.append(Q323_Entry)

# question 324
Q324_Label = customtkinter.CTkLabel(scrollable_frame4, text="How many task sequences will the local DP store")
Q324_Label.pack()

Q324_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q324_Entry.pack(pady=10)
entries.append(Q324_Entry)

# question 325
Q325_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="How many input prompts are there for task sequence kick off? What are they?")
Q325_Label.pack()

Q325_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q325_Entry.pack(pady=10)
entries.append(Q325_Entry)

# question 326
Q326_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will Premier need to provide DP hardware?")
Q326_Label.pack()

Q326_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q326_Entry.pack(pady=10)
entries.append(Q326_Entry)

# question 327
Q327_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="Can Premier run the VPN through Premier's established Firewall,\nor will Customer provide firewall/switches?")
Q327_Label.pack()

Q327_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q327_Entry.pack(pady=10)
entries.append(Q327_Entry)

# question 328
Q328_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="What are the security requirements for the DP and/or network?")
Q328_Label.pack()

Q328_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q328_Entry.pack(pady=10)
entries.append(Q328_Entry)

# question 329
Q329_Label = customtkinter.CTkLabel(scrollable_frame4, text="How is the task sequence applied i.e. MDT/SCCM?")
Q329_Label.pack()

Q329_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q329_Entry.pack(pady=10)
entries.append(Q329_Entry)

# question 330
Q330_Label = customtkinter.CTkLabel(scrollable_frame4, text="How long does task sequence deployment take?")
Q330_Label.pack()

Q330_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q330_Entry.pack(pady=10)
entries.append(Q330_Entry)

# question 331
Q331_Label = customtkinter.CTkLabel(scrollable_frame4, text="How will software be deployed for specific end users?")
Q331_Label.pack()

Q331_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q331_Entry.pack(pady=10)
entries.append(Q331_Entry)

# Autopilot Provisioning label
AP_Label = customtkinter.CTkLabel(scrollable_frame4, text="Autopilot Provisioning", font=("Helvetica", 20))
AP_Label.pack(pady=10)

# question 332
Q332_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will a bloat free image need to be applied?")
Q332_Label.pack()

Q332_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q332_Entry.pack(pady=10)
entries.append(Q332_Entry)

# question 333
Q333_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will Premier need to capture the hash values?")
Q333_Label.pack()

Q333_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q333_Entry.pack(pady=10)
entries.append(Q333_Entry)

# question 334
Q334_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will Premier need to upload the hash values?")
Q334_Label.pack()

Q334_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q334_Entry.pack(pady=10)
entries.append(Q334_Entry)

# question 335
Q335_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="If hash is to be uploaded into Customer's management system,\nwill Customer supply Premier necessary enablement?")
Q335_Label.pack()

Q335_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q335_Entry.pack(pady=10)
entries.append(Q335_Entry)

# question 336
Q336_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will Premier need to pull down the provisioning package?")
Q336_Label.pack()

Q336_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q336_Entry.pack(pady=10)
entries.append(Q336_Entry)

# question 337
Q337_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="Once the provisioning package has been pulled down,\nare there any additional steps required?")
Q337_Label.pack()

Q337_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q337_Entry.pack(pady=10)
entries.append(Q337_Entry)

# On Site Deployment Services label
OSDS_Label = customtkinter.CTkLabel(scrollable_frame4, text="On Site Deployment Services", font=("Helvetica", 20))
OSDS_Label.pack(pady=10)

# question 338
Q338_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="Will the new systems already be imaged, or will they need to be imaged by Premier prior to deployment?")
Q338_Label.pack()

Q338_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q338_Entry.pack(pady=10)
entries.append(Q338_Entry)

# question 339
Q339_Label = customtkinter.CTkLabel(scrollable_frame4, text="If equipment needs to be imaged, will the equipment be "
                                                            "imaged on-site\nor does the Customer need new systems "
                                                            "imaged prior to the delivery (i.e. at Premier's "
                                                            "warehouse)?")
Q339_Label.pack()

Q339_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q339_Entry.pack(pady=10)
entries.append(Q339_Entry)

# question 340
Q340_Label = customtkinter.CTkLabel(scrollable_frame4, text="If Premier will be imaging on-site, will Premier be "
                                                            "using Customer imaging process\nor will Premier need to "
                                                            "supply a mobile imaging solution?")
Q340_Label.pack()

Q340_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q340_Entry.pack(pady=10)
entries.append(Q340_Entry)

# question 341
Q341_Label = customtkinter.CTkLabel(scrollable_frame4, text="If yes and Customer will be shipping legacy systems back "
                                                            "to Premier, \nwill Premier need to remove the hard "
                                                            "drives, wipe the hard drives from the legacy systems as "
                                                            "part of process?\nIf so, where does Premier send the "
                                                            "pulled hard drives?")
Q341_Label.pack()

Q341_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q341_Entry.pack(pady=10)
entries.append(Q341_Entry)

# question 342
Q342_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will the legacy systems be Recycled, picked up by "
                                                            "leasing company? Other?")
Q342_Label.pack()

Q342_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Recycled", "Picked up"])
Q342_Entry.pack(pady=10)
entries.append(Q342_Entry)

# question 343
Q343_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will Customer/End-Customer utilize its own shipping "
                                                            "account, \nor will Customer/End-Customer require Premier"
                                                            " to ship returned equipment?")
Q343_Label.pack()

Q343_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q343_Entry.pack(pady=10)
entries.append(Q343_Entry)

# question 344
Q344_Label = customtkinter.CTkLabel(scrollable_frame4, text="How many new systems will be deployed?")
Q344_Label.pack()

Q344_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q344_Entry.pack(pady=10)
entries.append(Q344_Entry)

# question 345
Q345_Label = customtkinter.CTkLabel(scrollable_frame4, text="What type of systems and models will be deployed (i.e. "
                                                            "desktops, laptops, tablets, etc.)?")
Q345_Label.pack()

Q345_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q345_Entry.pack(pady=10)
entries.append(Q345_Entry)

# question 346
Q346_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will there be monitors included with these systems?\nIf "
                                                            "yes, what is the size/sizes of monitors to be deployed?")
Q346_Label.pack()

Q346_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q346_Entry.pack(pady=10)
entries.append(Q346_Entry)

# question 347
Q347_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will Premier need to connect any additional peripherals "
                                                            "or accessories \n(keyboard, mouse, camera, sound bar, "
                                                            "fingerprint reader, etc.)?")
Q347_Label.pack()

Q347_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q347_Entry.pack(pady=10)
entries.append(Q347_Entry)

# question 348
Q348_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will some machines have multiple monitors?")
Q348_Label.pack()

Q348_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q348_Entry.pack(pady=10)
entries.append(Q348_Entry)

# question 349
Q349_Label = customtkinter.CTkLabel(scrollable_frame4, text="If so, are there monitor arms/mounts, or is the standard "
                                                            "monitor base used to sit on desk?")
Q349_Label.pack()

Q349_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q349_Entry.pack(pady=10)
entries.append(Q349_Entry)

# question 350
Q350_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="How will systems with multiple monitor setups be identified?")
Q350_Label.pack()

Q350_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q350_Entry.pack(pady=10)
entries.append(Q350_Entry)

# question 351
Q351_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will cable management be required?")
Q351_Label.pack()

Q351_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q351_Entry.pack(pady=10)
entries.append(Q351_Entry)

# question 352
Q352_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="A) If so, is there a preference to Velcro versus Zip Ties?")
Q352_Label.pack()

Q352_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Velcro", "Zip Ties"])
Q352_Entry.pack(pady=10)
entries.append(Q352_Entry)

# question 353
Q353_Label = customtkinter.CTkLabel(scrollable_frame4, text="B) Color Preference?")
Q353_Label.pack()

Q353_Entry = customtkinter.CTkComboBox(scrollable_frame4,
                                       values=["", "Black", "White", "Blue", "Red", "Green", "Yellow"])
Q353_Entry.pack(pady=10)
entries.append(Q353_Entry)

# question 354
Q354_Label = customtkinter.CTkLabel(scrollable_frame4, text="How many different locations will receive deployed new "
                                                            "system? Provide specific deployment addresses?")
Q354_Label.pack()

Q354_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q354_Entry.pack(pady=10)
entries.append(Q354_Entry)

# question 355
Q355_Label = customtkinter.CTkLabel(scrollable_frame4, text="How many systems per site?")
Q355_Label.pack()

Q355_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q355_Entry.pack(pady=10)
entries.append(Q355_Entry)

# question 356
Q356_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will a site map of the location be available for our "
                                                            "lead technician?")
Q356_Label.pack()

Q356_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q356_Entry.pack(pady=10)
entries.append(Q356_Entry)

# question 357
Q357_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will Customer/End-Customer provide a list/map prior to "
                                                            "deployment \ndetailing the new system locations with "
                                                            "each deployment site?")
Q357_Label.pack()

Q357_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q357_Entry.pack(pady=10)
entries.append(Q357_Entry)

# question 358
Q358_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will the new systems already be located in a central "
                                                            "storage room within the deployment building?\nOr does "
                                                            "Premier require warehousing and delivery? If "
                                                            "delivery?\nHow many days prior to onsite Services can "
                                                            "systems be delivered?")
Q358_Label.pack()

Q358_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q358_Entry.pack(pady=10)
entries.append(Q358_Entry)

# question 359
Q359_Label = customtkinter.CTkLabel(scrollable_frame4, text="Are there any special circumstances Premier needs to be "
                                                            "aware of at the individual sites?\n(i.e. no elevators, "
                                                            "no carts allowed in bldg., etc.)?")
Q359_Label.pack()

Q359_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q359_Entry.pack(pady=10)
entries.append(Q359_Entry)

# question 360
Q360_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="Will deployment be completed during standard M-F workdays?")
Q360_Label.pack()

Q360_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q360_Entry.pack(pady=10)
entries.append(Q360_Entry)

# question 361
Q361_Label = customtkinter.CTkLabel(scrollable_frame4, text="What are the hours Premier will be able to deploy?")
Q361_Label.pack()

Q361_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q361_Entry.pack(pady=10)
entries.append(Q361_Entry)

# question 362
Q362_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will all assets be deployed concurrent and continuous, "
                                                            "once begun,\n or staggered? Explain requirements.")
Q362_Label.pack()

Q362_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q362_Entry.pack(pady=10)
entries.append(Q362_Entry)

# question 363
Q363_Label = customtkinter.CTkLabel(scrollable_frame4, text="If Premier needs to deliver the systems to the "
                                                            "deployment locations, does each location have a loading "
                                                            "dock?\nOr will Customer/End-Customer's delivery require "
                                                            "a truck with a lift-gate? or a special sized truck?")
Q363_Label.pack()

Q363_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q363_Entry.pack(pady=10)
entries.append(Q363_Entry)

# question 364
Q364_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will Premier be able to move pallets through the "
                                                            "deployment locations?")
Q364_Label.pack()

Q364_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q364_Entry.pack(pady=10)
entries.append(Q364_Entry)

# question 365
Q365_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will Customer provide a secured area within the "
                                                            "deployment locations as a staging area?")
Q365_Label.pack()

Q365_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q365_Entry.pack(pady=10)
entries.append(Q365_Entry)

# question 366
Q366_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will Premier be able to use Customer carts to transport "
                                                            "the systems from the staging area\nto the final "
                                                            "destination within the deployment locations, "
                                                            "or will Premier be required to supply carts?\nIf "
                                                            "floor-covering protection is required, "
                                                            "will Customer/End-Customer Premier such floor-covering,"
                                                            "\nor is Premier required to supply floor-covering?")
Q366_Label.pack()

Q366_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q366_Entry.pack(pady=10)
entries.append(Q366_Entry)

# question 367
Q367_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will Premier be allowed unlimited access to freight or "
                                                            "building elevators in the event of multiple level "
                                                            "deployment?")
Q367_Label.pack()

Q367_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q367_Entry.pack(pady=10)
entries.append(Q367_Entry)

# question 368
Q368_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will de-installation the legacy systems be required?")
Q368_Label.pack()

Q368_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q368_Entry.pack(pady=10)
entries.append(Q368_Entry)

# question 369
Q369_Label = customtkinter.CTkLabel(scrollable_frame4, text="If so, where will the legacy systems be removed too?")
Q369_Label.pack()

Q369_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q369_Entry.pack(pady=10)
entries.append(Q369_Entry)

# question 370
Q370_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will Premier need to remove the hard drives from "
                                                            "the\nlegacy systems as part of the de-installation "
                                                            "process?")
Q370_Label.pack()

Q370_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q370_Entry.pack(pady=10)
entries.append(Q370_Entry)

# question 371
Q371_Label = customtkinter.CTkLabel(scrollable_frame4, text="Does Customer require data transfer or data migration "
                                                            "for new systems?\nIf data is to be transferred, "
                                                            "will Customer/End-User require users to put all of files "
                                                            "to be\ntransferred in a desktop folder labelled My "
                                                            "Documents prior to Services?")
Q371_Label.pack()

Q371_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q371_Entry.pack(pady=10)
entries.append(Q371_Entry)

# question 372
Q372_Label = customtkinter.CTkLabel(scrollable_frame4, text="Does Customer/End-Customer have a process currently in "
                                                            "use to perform data migrations?\nIf so, what is the "
                                                            "process currently in use?")
Q372_Label.pack()

Q372_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q372_Entry.pack(pady=10)
entries.append(Q372_Entry)

# question 373
Q373_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will Premier need to transfer data from the legacy "
                                                            "systems to the new systems?")
Q373_Label.pack()

Q373_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q373_Entry.pack(pady=10)
entries.append(Q373_Entry)

# question 374
Q374_Label = customtkinter.CTkLabel(scrollable_frame4, text="If so, can we use your network to transfer data, or can "
                                                            "Premier transfer directly from system to system?")
Q374_Label.pack()

Q374_Entry = customtkinter.CTkComboBox(scrollable_frame4,
                                       values=["", "Shared Drive", "Cloud (O365)", "Crossover Cables",
                                               "External drive (Thumb drive or hard drive)"])
Q374_Entry.pack(pady=10)
entries.append(Q374_Entry)

# question 375
Q375_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="What is the average amount of data to be migrated or transferred?")
Q375_Label.pack()

Q375_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q375_Entry.pack(pady=10)
entries.append(Q375_Entry)

# question 376
Q376_Label = customtkinter.CTkLabel(scrollable_frame4, text="What needs to be transferred - profiles, bookmarks, data?")
Q376_Label.pack()

Q376_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q376_Entry.pack(pady=10)
entries.append(Q376_Entry)

# question 377
Q377_Label = customtkinter.CTkLabel(scrollable_frame4, text="What is not to be transferred - pics, music?")
Q377_Label.pack()

Q377_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q377_Entry.pack(pady=10)
entries.append(Q377_Entry)

# question 378
Q378_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will Premier be able to use the Customer/End-Customer "
                                                            "dumpsters at each location to dispose of the "
                                                            "trash\nWithin deployment building or within a maximum of "
                                                            "50 ft from deployment site?\nOr does Customer require "
                                                            "Premier to remove deployment trash from the "
                                                            "location?\nIf Premier is required to remove, "
                                                            "will Customer provide a location onsite for temporary "
                                                            "storage,\nso deployment trash can temporarily be "
                                                            "accumulated onsite?")
Q378_Label.pack()

Q378_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q378_Entry.pack(pady=10)
entries.append(Q378_Entry)

# question 379
Q379_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="What reporting data will Customer require for this deployment project\n(i.e. serial # of system, serial # of monitor, floor #, room #, etc.)?\nWhat frequency will Customer require deployment reporting?")
Q379_Label.pack()

Q379_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q379_Entry.pack(pady=10)
entries.append(Q379_Entry)

# Staff Augmentation label
SA_Label = customtkinter.CTkLabel(scrollable_frame4, text="Staff Augmentation", font=("Helvetica", 20))
SA_Label.pack(pady=10)

# question 380
Q380_Label = customtkinter.CTkLabel(scrollable_frame4, text="What level of technician is required?")
Q380_Label.pack()

Q380_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q380_Entry.pack(pady=10)
entries.append(Q380_Entry)

# question 381
Q381_Label = customtkinter.CTkLabel(scrollable_frame4, text="What will their primary responsibilities be?")
Q381_Label.pack()

Q381_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q381_Entry.pack(pady=10)
entries.append(Q381_Entry)

# question 382
Q382_Label = customtkinter.CTkLabel(scrollable_frame4, text="Any certifications required?")
Q382_Label.pack()

Q382_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q382_Entry.pack(pady=10)
entries.append(Q382_Entry)

# question 383
Q383_Label = customtkinter.CTkLabel(scrollable_frame4, text="What background checks are required?")
Q383_Label.pack()

Q383_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q383_Entry.pack(pady=10)
entries.append(Q383_Entry)

# question 384
Q384_Label = customtkinter.CTkLabel(scrollable_frame4, text="What is the duration of the staff augmentation?")
Q384_Label.pack()

Q384_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q384_Entry.pack(pady=10)
entries.append(Q384_Entry)

# question 385
Q385_Label = customtkinter.CTkLabel(scrollable_frame4, text="How many resources are needed?")
Q385_Label.pack()

Q385_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q385_Entry.pack(pady=10)
entries.append(Q385_Entry)

# question 386
Q386_Label = customtkinter.CTkLabel(scrollable_frame4, text="Will travel be required?")
Q386_Label.pack()

Q386_Entry = customtkinter.CTkComboBox(scrollable_frame4, values=["", "Yes", "No"])
Q386_Entry.pack(pady=10)
entries.append(Q386_Entry)

# question 387
Q387_Label = customtkinter.CTkLabel(scrollable_frame4,
                                    text="How will expenses for mileage, parking, etc. be billed to the customer?")
Q387_Label.pack()

Q387_Entry = customtkinter.CTkEntry(scrollable_frame4, placeholder_text="Enter your answer here", width=250)
Q387_Entry.pack(pady=10)
entries.append(Q387_Entry)

# Create submit button
Submit_Button = customtkinter.CTkButton(root, text="Submit", command=save_word_document)
Submit_Button.pack(pady=10)

# Create a button to clear the entries
Clear_Button = customtkinter.CTkButton(root, text="Clear entire form", command=clear_entries)
Clear_Button.pack(pady=10)

# Run the GUI
root.mainloop()
