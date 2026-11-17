from exception import InvalidException
from question_set import questions #import questions 
prize=0
totalPrize=len(questions)*10
print(f"Here you compiting for the :${totalPrize}\nEach qustion weatage is $10")
for question in questions:
    print(question[0])
    print(f"1.{question[1]}")
    print(f"2.{question[2]}")
    print(f"3.{question[3]}")
    print(f"4.{question[4]}")
    #cheack wheather the answer is correct or not
    flag=True
    while (a:=input("Enter your answer. in form of 1/2/3/4: ")):
        try:
            user_answer=int(a)
            if user_answer<1 or user_answer>4:
                raise InvalidException()
            if question[5]==user_answer:
                print("Correct Answer.")
                prize+=10
            else:
                print(f"Incorect, the corect answer was option: {question[5]}")
                print("Better Luck next time!")
                flag=False
            break
        except Exception:
            print(f"{a} is not an valid option.Plese chose a vailid option")
    print(f"You Currently own the ${prize}")
    if flag==False:
        break


print("Aswome your all answer are correct!")