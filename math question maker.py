import random

def generate_problem():
    num1=random.randint(1,10)
    num2=random.randint(1,10)
    operator=random.choice(["*","-","+","/"])

    if operator =="/" and num1% num2!=0:
        num1=num2*random.randint(1,10)
    problem=f"{num1} {operator} {num2}"
    answer=eval(problem)
    return problem,answer
def main():
    print("Welcome to my maths quiz!")
    print("Solve the following arithematic problems")
    score=0
    num_problems=5
    for i in range(num_problems):
        problem,answer=generate_problem()
        user_answer=float(input(f"What is the answer to {problem}"))

        if user_answer==answer:
            print("That's correct!")
            score=score+1
        else:
            print("That's incorrect maybe you will get it next time")
    print(f"your score is {score}/{num_problems}")

if __name__=="__main__":
    main()