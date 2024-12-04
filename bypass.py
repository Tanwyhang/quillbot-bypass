import customtkinter as ctk

# Initialize the app
ctk.set_appearance_mode("dark")  # Set dark mode
ctk.set_default_color_theme("blue")  # Set color theme

def replace_periods():
    input_text = text_input.get("1.0", "end-1c")  # Get input text from the textbox
    replaced_text = input_text.replace('.', ' . ')  # Replace periods
    result_text.delete("1.0", "end")  # Clear the result textbox
    result_text.insert("1.0", replaced_text)  # Insert the modified text

# Create the main window
app = ctk.CTk()
app.title("Replace Periods")
app.geometry("600x400")

# Input label
input_label = ctk.CTkLabel(app, text="Enter your paragraph:", font=("Raleway", 14))
input_label.pack(pady=10)

# Input text box
text_input = ctk.CTkTextbox(app, width=500, height=100)
text_input.pack(pady=10)

# Button to replace periods
replace_button = ctk.CTkButton(app, text="Replace Periods", command=replace_periods)
replace_button.pack(pady=10)

# Result label
result_label = ctk.CTkLabel(app, text="Modified Paragraph:", font=("Raleway", 14))
result_label.pack(pady=10)

# Result text box
result_text = ctk.CTkTextbox(app, width=500, height=100)
result_text.pack(pady=10)

# Run the application
app.mainloop()
