from tkinter import Tk, Button, Label, Text, W
from PIL import Image, ImageTk
import random
from words import words

BACKGROUND_COLOR = "#000000"
seg = 60


def start():
    global window, selected_words

    def finish():
        global start        
        for widget in window.winfo_children():
            widget.grid_forget()
        i = 0
        errors = 0
        for word in user_words:           
            if word != selected_words[i]:
                errors += 1
            i += 1
        wpm = i-errors
        cpm = user_char
        if i == 0 :
            acurracy = 0
        else: 
            acurracy = int(wpm/i*100)
        with open('high_Score.txt', ) as file:
            high_score = int(file.read())
            if wpm > high_score:
                high_score = wpm
                with open('high_Score.txt', mode='w' ) as file:
                    file.write(f'{high_score}')     

        text_label = Label(text=f'THIS ARE YOUR RESULTS', font=('Arial', 38, 'bold'), background=BACKGROUND_COLOR, foreground='#fafafa', justify='center')
        text_label.grid(column=0, row=1, columnspan=2, padx= (50, 90))

        reset_button = Button(text='Reset', font=('Arial', 38, 'bold'), background='#fafafa', fg=BACKGROUND_COLOR, command=reset)
        reset_button.grid(column=0, row=2)

        exit_ = Button(text='Exit', font=('Arial', 38, 'bold'), background='#fafafa', fg=BACKGROUND_COLOR, command=window.quit)
        exit_.grid(column=1, row=2, sticky=W)
        
        wpm_label = Label(text=f'Words per minute\n(WPM)\n{wpm}', font=('Arial', 18, 'bold'), background='#fafafa', foreground=BACKGROUND_COLOR)
        wpm_label.grid(column=2, row=0)

        cpm_label = Label(text=f'Characters per minute\n(CPM)\n{cpm}', font=('Arial', 18, 'bold'), background='#fafafa', foreground=BACKGROUND_COLOR)
        cpm_label.grid(column=2, row=1, pady=40)

        acurracy_label =  Label(text=f'Acurracy\n{acurracy} %', font=('Arial', 18, 'bold'), background='#fafafa', foreground=BACKGROUND_COLOR)
        acurracy_label.grid(column=2, row=2, pady=(0, 40))

        high_score_label = Label(text=f'Your High Score\n(CPM)\n{high_score}', font=('Arial', 18, 'bold'), background='#fafafa', foreground=BACKGROUND_COLOR)
        high_score_label.grid(column=2, row=3)

    def count(seg):
        if seg >=0 :
            time_left.config(text=seg)
            window.after(200, count, seg-1)
        else: 
            results = Button(text=('TIME OUT !!!\nSHOW RESULTS'), font=('Arial', 18, 'bold'),  background='red', fg=BACKGROUND_COLOR, command=finish)
            results.grid(column=0, row=5,  pady=(30, 0))

    def typing(event):
        global user_words, user_char
        user_char += len(input_text.get("1.0", "end-1c").strip().lower())
        user_words.append(input_text.get("1.0", "end-1c").strip().lower())
        input_text.delete("1.0", "end")

    for widget in window.winfo_children():
        widget.grid_forget()
    
    timer = Label(text='TIMER', font=('Arial', 18, 'bold'), background=BACKGROUND_COLOR, fg='#fafafa')
    timer.grid(column=0, row=0)

    time_left = Label(text='60', font=('Arial', 28, 'bold'), background=BACKGROUND_COLOR, fg='#fafafa')
    time_left.grid(column=0, row=1)
    
    selected_words = random.sample(words, 50)
    paragraph = Label(text=selected_words, font=('Arial', 20, 'bold'),  wraplength=1000, border=10 )
    paragraph.grid(column=0, row=2, pady=10)

    write_below = Label(text='Write Below', font=('arial', 16, 'bold'), background=BACKGROUND_COLOR, fg='#fafafa')
    write_below.grid(column=0, row=3, pady=20)

    input_text = Text(window, height=1, width=15, wrap="word", font=('arial', 20, 'bold'), bd=6,)
    input_text.grid(column=0, row=4)
    input_text.focus()

    window.bind('<space>', typing )
    count(seg)

def reset():
    global window
    for widget in window.winfo_children():
        widget.grid_forget()
    main()

window = Tk()
def main():
    global window, user_words, user_char
    user_words = []
    user_char = 0  
    window.title('Typing Speed Test App')
    window.minsize(height=620, width=1100)
    window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

    image1 = Image.open('images.jfif')
    photo = ImageTk.PhotoImage(image1)
    image_ = Label(window, image=photo)
    image_.grid(row=0, column=1, padx=10, pady=10)

    welcome = Label(text='Welcome to type speed test', font=('Arial', 24, 'bold'), background=BACKGROUND_COLOR, fg='#fafafa')
    welcome.grid(row=1, column=1)

    text = Label(text='\nThis app allows you to check your typing speed\n'
                    'Click to START button to start. Type in the word as faster as possible. You will have 60 seconds.\n'
                    'The app will count and provide you with the final results.\n'
                    'The application automatically saves the highest score.', font=('Arial', 18, 'bold'), background=BACKGROUND_COLOR, fg='#fafafa')
    text.grid(row=2, column=1)

    space = Label(text='\n', background=BACKGROUND_COLOR)
    space.grid(column=1, row=3)

    start_button = Button(text='START', font=('Arial', 24, 'bold'), command=start)
    start_button.grid(row=4, column=1, rowspan=1, sticky='S')

    window.mainloop()

if __name__ == "__main__":
    main()
