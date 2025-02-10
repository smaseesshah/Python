# Kaun Banega Crore Pati
print("""Welcome to the Quiz Game!

This game is inspired by "Kaun Banega Crorepati", where you will answer a series of multiple-choice questions to earn points. Each correct answer will earn you points. If you answer incorrectly, you won't earn points for that question.

Instructions:
1. You will be presented with a series of questions.
2. Each question has multiple-choice answers labeled A, B, C, and D.
3. Choose the correct answer by entering the corresponding letter.
4. Your score will be displayed after each correct answer.
5. You can quit the game anytime by entering 'q'.

Let's see how many points you can score!""")

questions = questions = [
    ["Q-1. Who is the current Prime Minister of Pakistan?", 
        "A. Imran Khan", 
        "B. Nawaz Sharif", 
        "C. Asif Ali Zardari", 
        "D. Pervez Musharraf"],
    ["Q-2. Which river is the longest in Pakistan?", 
        "A. Indus", 
        "B. Jhelum", 
        "C. Chenab", 
        "D. Ravi"],
    ["Q-3. What is the capital city of Pakistan?", 
        "A. Islamabad", 
        "B. Karachi", 
        "C. Lahore", 
        "D. Peshawar"],
    ['Q-4. Which Pakistani cricketer has the nickname "Rawalpindi Express"?', 
        "A. Shahid Afridi", 
        "B. Wasim Akram", 
        "C. Shoaib Akhtar", 
        "D. Misbah-ul-Haq"],
    ["Q-5. What is the official language of Pakistan?", 
        "A. English", 
        "B. Urdu", 
        "C. Punjabi", 
        "D. Pashto"],
    ["Q-6. Who is the founder of Pakistan?", 
        "A. Allama Iqbal", 
        "B. Liaquat Ali Khan", 
        "C. Muhammad Ali Jinnah", 
        "D. Ayub Khan"],
    ["Q-7. Which province of Pakistan is known as the 'Land of the Pure'?", 
        "A. Punjab", 
        "B. Sindh", 
        "C. Balochistan", 
        "D. Khyber Pakhtunkhwa"],
    ["Q-8. Which mountain peak is the highest in Pakistan and the second highest in the world?", 
        "A. Nanga Parbat", 
        "B. Gasherbrum I", 
        "C. K2", 
        "D. Broad Peak"],
    ["Q-9. What is the national animal of Pakistan?", 
        "A. Markhor", 
        "B. Snow Leopard", 
        "C. Ibex", 
        "D. Chinkara"],
    ["Q-10. Who wrote the Pakistani national anthem?", 
        "A. Allama Iqbal", 
        "B. Faiz Ahmed Faiz", 
        "C. Ahmed Ghulamali Chagla", 
        "D. Hafeez Jullundhri"]
]
answers = ["B","A","A","C","B","C",'A','C','A','D']
score = 0
q = 0
for i in range(100):
    if q==10:
        break
    print(f"Your Current Score is {score}")
    print(questions[q][0],questions[q][1],questions[q][2],questions[q][3],questions[q][4],sep="\n")
    c_a = (input("Enter your answer (A/B/C/D) or Q to Quit: ")).upper()
    if c_a==answers[q]:
        print("\nCorrect Answer")
        score=score+10
        q = q+1
    elif (len(c_a)>1)or(ord(c_a)>68 and ord(c_a) < 81)or(ord(c_a)>81):
        print("\ninvalid input!")
        continue
    elif c_a=='Q':
        break
    else:
        print("\nWrong Answer")
        print(f"Correct Answer Is : {answers[q]}")
        q = q+1
print(f"\nYour Total Score is {score}")
