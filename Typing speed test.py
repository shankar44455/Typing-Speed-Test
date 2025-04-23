from tkinter import *
from tkinter import messagebox
from timeit import default_timer as timer

window=Tk()
window.title("Typing speed Test")
window.geometry('1200x1000')
window.configure(bg='white')  
Typing_speed_test = Frame(window)
Typing_speed_test.pack(pady=20)

l = Label(Typing_speed_test, text="Typing Speed Test", fg='red', font=('Arial black', 42))
l.pack()

sample_text = ("Take care of mental health when you are alone "
    "1. Do activities that you love/enjoy. "
    "Try to continue doing the activities that you find meaningful and enjoyable, such as cooking for yourself or your loved ones, "
    "playing with your pet, walking in the park, reading a book, or watching a film or TV series. "
    "Having a regular routine with activities that make you feel happy will help you maintain good mental health."
    "2. Look after your physical health. "
    "Taking care of your physical health helps improve your mental health and well-being. "
    "Be active for at least 30 minutes daily, whether that’s running, walking, yoga, dancing, cycling, or even gardening. "
    "Eat a balanced and healthy diet. Make sure to get enough sleep. ")

text_display = Text(window, wrap=WORD, height=10, width=80, font="Arial 16")
text_display.insert(END, sample_text)
text_display.pack(pady=5)

st = Button(window, text="Start", bg="red", padx=60, pady=10, command=lambda: start_test())
st.pack(pady=10)


sub = Button(window, text="Submit", bg="Green", padx=60, pady=10, command=lambda: submit_test())
sub.pack(pady=10)


text_entry = Entry(window, width=500, font=("arial", 40), selectbackground="black", selectforeground="yellow")
text_entry.pack(pady=50)

Result = Button(window, text="Result", bg="yellow", padx=120, pady=10, command=lambda: result_test())
Result.pack(pady=10)


Result_label = Label(window, text="", font=("Arial", 24), bg='yellow')
Result_label.pack(pady=20)


start_time = None
end_time = None

def start_test():
    global start_time
    start_time = timer()
    text_entry.delete(0, END)  
    text_entry.insert(0, sample_text)  
    text_entry.focus()  

def submit_test():
    global end_time
    if start_time is None:
        messagebox.showinfo("Info", "Please start the test first.")
        return
    
    end_time = timer()
    user_input = text_entry.get()
    calculate_results(user_input)


def Calculate_Results(user_input):
    global sample_text
    
    sample_words = sample_text.split()
    user_words = user_input.split()

    time_taken = end_time - start_time  
    wpm = (len(user_words) / time_taken) * 60
   

    correct_words = sum(1 for i in range(min(len(sample_words), len(user_words))) if sample_words[i] == user_words[i])
    Total_words = len(user_words) - correct_words  
    accuracy = round((correct_words / max(len(sample_words), 1)) * 100, 2)
    result_label.config(text=f"WPM: {wpm:.2f}, Accuracy: {accuracy:.2f}%, Total_words : {Total_words}")



   






















