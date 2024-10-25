import turtle

def draw_pythagoras_tree(t, branch_length, level):
    if level > 0:
        # Рисуем ствол
        t.forward(branch_length)
        
        # Рисуем левую ветку
        t.left(45)
        draw_pythagoras_tree(t, branch_length * 0.6, level - 1)

        # Возвращаемся к исходной позиции
        t.right(90)
        
        # Рисуем правую ветку
        draw_pythagoras_tree(t, branch_length * 0.6, level - 1)

        # Возвращаемся к исходной позиции
        t.left(45)
        t.backward(branch_length)

def draw_tree(level, size=100):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90) 
    t.penup()
    t.goto(0, -250)
    t.pendown()

    draw_pythagoras_tree(t, size, level)

    window.mainloop()
    
# Оптимальное значение 3-5
user_input = input("Введите уровень рекурсии для дерева Пифагора: ")

draw_tree(int(user_input))
