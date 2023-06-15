from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from levels import levels
import random

root = Tk()
root.title("Eesti Learn")
root.geometry("300x250")
root.attributes('-fullscreen', True)

root.configure(background='#3B5C91')


btnStyle = ttk.Style()
btnStyle.configure("btnStyle.TLabel", font="Arial 24", foreground="#91FEC7", padding=20, background="#1C2648")

lableStyle = ttk.Style()
lableStyle.configure('lableStyle.TLabel', font="Arial 18",foreground='#1C2648', background='#1C2648')




def closeGame():
    root.destroy()

def clearWindow():
    for widget in root.winfo_children():
        widget.destroy()

def startScreen():
    clearWindow()
    startScreen = Frame(background='#3B5C91')
    startScreen.place(relx=0.5, rely=0.5, anchor=CENTER)

    heading = ttk.Label(startScreen, text='Eesti Learn Game', font='Arial 64', background='#3B5C91')
    heading.pack(pady=20)

    levelsBtn = ttk.Button(startScreen, text='К списку уровней', command=levelsPage, style='btnStyle.TLabel')
    levelsBtn.pack(pady=20)

    exitBtn = ttk.Button(startScreen, text='Выйти', command=closeGame, style='btnStyle.TLabel')
    exitBtn.pack()

def levelsPage():
    clearWindow()

    levelsScreen = Frame(background='#3B5C91')
    levelsScreen.place(relx=0.5, rely=0.5, anchor=CENTER)

    backBtn = ttk.Button(text='Назад', command=startScreen, style='btnStyle.TLabel')
    backBtn.grid(row=0, column=0, padx=10, pady=10, sticky='w')

    style = ttk.Style()
    style.configure('Custom.TLabelframe', background='#91FEC7"')

    num_levels = len(levels)
    num_columns = 3

    for index, level in enumerate(levels.keys(), start=1):
        level_name = level
        
        levelFrame = ttk.LabelFrame(levelsScreen, text=f'{level_name}', style='lableStyle.TLabel')
        levelFrame.grid(row=(index-1) // num_columns, column=(index-1) % num_columns, padx=10, pady=10)

        learnBtn = ttk.Button(levelFrame, text='Учить Лексику', command=lambda level=level: learnWords(level), style='btnStyle.TLabel')
        learnBtn.pack(pady=8)

        ThemeBtn = ttk.Button(levelFrame, text=f'Уровень {index}',style='btnStyle.TLabel')
        ThemeBtn.pack(pady=0)

        playBtn = ttk.Button(levelFrame, text='Играть', command=lambda level=level: play(level), style='btnStyle.TLabel')
        playBtn.pack(pady=8)

def learnWords(lvl):
    clearWindow()

    backBtn = ttk.Button(text='К списку уровней', command=levelsPage, style='btnStyle.TLabel')
    backBtn.place(relx=0, rely=0)
    
    playBtn = ttk.Button(text='Играть', command=lambda level=lvl: play(level), style='btnStyle.TLabel')
    playBtn.place(relx=1, rely=0, anchor="ne")
    
    wordsScreen = Frame(background='#3B5C91')
    wordsScreen.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    for word in levels[lvl].keys():
        meaning = ttk.Label(wordsScreen, text=f'{word} - {levels[lvl][word]}', background='#3B5C91', font='Arial 14')
        meaning.pack(pady=5)

def play(lvl):
    clearWindow()
    
    def leaveLevel():
        root.after_cancel(makeHit)
        levelsPage()
    
    backBtn = ttk.Button(text='К списку уровней', command=leaveLevel, style='btnStyle.TLabel')
    backBtn.place(relx=0, rely=0)
    
    battleScreen = Frame(background='#3B5C91')
    battleScreen.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    enemyHp = 100
    
    enemyHpText = ttk.Label(battleScreen, text=f'Здоровье противника: {enemyHp}/100', background='#3B5C91', font='Arial 14')
    enemyHpText.pack(pady=5)
    
    enemyHpProgress =  ttk.Progressbar(battleScreen, orient="horizontal", value=enemyHp, max=100)
    enemyHpProgress.pack(fill=X, pady=(5, 200))
    
    attempts = 0
    words = list(levels[lvl].keys())
    random.shuffle(words)
    
    def attack():
        nonlocal enemyHp
        nonlocal attempts
        if answer.get().lower() == words[attempts].lower():
            answer.delete(0, END)
            enemyHp -= 10
            if enemyHp <= 0:
                winScreen()
                return
            enemyHpText.configure(text=f'Здоровье противника: {enemyHp}/100')
            enemyHpProgress.configure(value=enemyHp)
            attempts += 1
            if attempts > len(words) -1:
                attempts = 0
                random.shuffle(words)
            askedWord.configure(text=f'Введите слово "{levels[lvl][words[attempts]]}" на эстонском')
        else:
            messagebox.showerror(title='Ошибка', message='Вы ввели не верное слово')
    
    askedWord = ttk.Label(battleScreen, text=f'Введите слово "{levels[lvl][words[0]]}" на эстонском', background='#3B5C91', font='Arial 14')
    askedWord.pack()
    
    answer = ttk.Entry(battleScreen)
    answer.pack(pady=5, fill='x')
    
    answerBtn = ttk.Button(battleScreen, text="Атаковать", command=attack)
    answerBtn.pack(pady=5, fill='x')
    
    
    playerHp = 100

    playerHpText = ttk.Label(battleScreen, text=f'Ваше здоровье: {playerHp}/100', background='#3B5C91', font='Arial 14')
    playerHpText.pack(pady=(200, 5))
    
    playerHpProgress =  ttk.Progressbar(battleScreen, orient="horizontal", value=playerHp, max=100)
    playerHpProgress.pack(fill=X, padx=5)
    
    def hit():
        global makeHit
        nonlocal playerHp
        playerHp -= 10
        if playerHp <= 0:
            loseScreen()
            return
        playerHpProgress.configure(value=playerHp)
        
        playerHpText.configure(text=f'Ваше здоровье: {playerHp}/100')
        makeHit = root.after(10000, hit)
    global makeHit
    makeHit = root.after(10000, hit)

def winScreen():
    root.after_cancel(makeHit)
    clearWindow()
    
    winScreen = Frame(background='#3B5C91')
    winScreen.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    heading = ttk.Label(winScreen, text='Вы победили!', font='Arial 64', background='#3B5C91')
    heading.pack(pady=20)
    
    levelsBtn = ttk.Button(winScreen, text='К списку уровней', command=levelsPage, style='btnStyle.TLabel')
    levelsBtn.pack(pady=20)
    
def loseScreen():
    root.after_cancel(makeHit)
    clearWindow()
    
    winScreen = Frame(background='#3B5C91')
    winScreen.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    heading = ttk.Label(winScreen, text='Вы проиграли!', font='Arial 64', background='#3B5C91')
    heading.pack(pady=20)
    
    levelsBtn = ttk.Button(winScreen, text='К списку уровней', command=levelsPage, style='btnStyle.TLabel')
    levelsBtn.pack(pady=20)


startScreen()
root.mainloop()
