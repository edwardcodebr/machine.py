class student:
    count = 0
    def __init__(self) -> None:
        student.count = student.count + 1
        
p1 = student()
p2 = student()
p3 = student()
p4 = student()
p5 = student()

print("o numero de estudantes é igual a", student.count)