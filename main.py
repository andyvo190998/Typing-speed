words = "Vietnam went through prolonged warfare in the 20th century After World War II France returned to reclaim colonial power in the First Indochina War from which Vietnam emerged victorious in 1954 Vietnam was also separated into two parts in same year The Vietnam War began shortly after it was the war between communist North supported by the Soviet Union and China and anti-communist South supported by the United States Upon the North Vietnamese victory in 1975 Vietnam reunified as a unitary socialist state under the Communist Party of Vietnam (CPV) in 1976 An ineffective planned economy a trade embargo by the West and wars with Cambodia and China crippled the country further In 1986 the CPV initiated economic and political reforms similar to the Chinese economic reform transforming the country to a market-oriented economy The reforms facilitated Vietnamese reintegration into global economy and politics"
words_list = words.split(" ")

from random import *
import tkinter
from multiprocessing import Process

window = tkinter.Tk()
window.minsize(width=300, height=400)
window.title("TYPING SPEED")



words_typping = []


list_words = tkinter.Label(text="hey this is text", font=("Arial", 24, "bold"))
list_words.grid(column=0, row=3, padx=5, pady=5)
# list_words.pack()

choice1 = tkinter.Label(text="how many words \n you want to challenge?", font=("Arial", 24, "bold"))
choice1.grid(column=0, row=0, padx=5,pady=5)
# choice1.pack()
score = 0

user_input1 = tkinter.Entry()
user_input1.grid(column=0, row=1, padx=5, pady=5)
# user_input1.pack()
sentence = ""
game_ready = False
scores = tkinter.Label()
scores.grid(column=0, row=5, padx=5, pady=5)
# scores.pack()
user_choice1 = ""

import time

time_second = 0
timer = tkinter.Label(text=f"timer: {time_second}s", font=("Arial", 24, "italic"))
timer.grid(column=0, row=6, padx=5, pady=5)

challenge_ready = False
def on_click():
    global challenge_ready
    global words_typping
    global sentence
    global score
    global user_choice1

    user_choice1 = int(user_input1.get())
    for i in range(1, user_choice1 + 1):
        random_word = choice(words_list)
        words_typping.append(random_word.lower())
    sentence = ' '.join(words_typping)
    global scores
    scores.config(text=f"your scores: {score}/{user_choice1}")

    #delete input
    user_input1.delete(0, tkinter.END)
    user_input1.insert(0, "")
    print(words_typping)
    check(key="char")
    thread2.start()

submit_button = tkinter.Button(text="SUBMIT", command=on_click)
submit_button.grid(column=0, row=2, padx=5, pady=5)



def timer_func():
    global time_second
    while challenge_ready == True:
        time.sleep(1)
        time_second += 1
        timer.config(text=f"timer: {time_second}s")
        window.update()

stt = 0
def check(key):
    global score
    global stt
    check_word = words_typping[stt]
    list_words.config(text=check_word)

    #timmer
    global challenge_ready
    global time_second
    challenge_ready = True
    # while time_second < 100:
    #     time.sleep(10)
    #     time_second += 1
    #     timer.config(text=f"timer: {time_second}s")

    if user_input.get() == check_word:
        if stt < user_choice1 - 1:
            stt += 1
            score += 1
            scores.config(text=f"your scores: {score}/{user_choice1}")
            check_word = words_typping[stt]
            list_words.config(text=check_word)
            user_input.delete(0, tkinter.END)
            user_input.insert(0, "")
        else:
            score += 1
            scores.config(text=f"your final scores: {score}/{user_choice1}")
            user_input.delete(0, tkinter.END)
            user_input.insert(0, "")
            challenge_ready = False
            print("ended")
    elif user_input.get() != check_word and user_input.get()!= "":
        stt += 1
        check_word = words_typping[stt]
        list_words.config(text=check_word)
        user_input.delete(0, tkinter.END)
        user_input.insert(0, "")

import threading

thread2 = threading.Thread(target=timer_func)





user_input = tkinter.Entry()
user_input.grid(column=0, row=4, padx=5, pady=5)
# user_input.pack()
user_input.bind("<Return>", check)





window.mainloop()
