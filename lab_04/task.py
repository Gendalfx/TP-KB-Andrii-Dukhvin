#Перетворення інфіксного виразу у ЗПЗ
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3} 
    output = []
    stack = []
    
    for token in expression:
        if token.isnumeric():         
            output.append(token)
        elif token == '(':            
            stack.append(token)
        elif token == ')':            
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()                
        else:                           # Якщо символ - оператор
            while (stack and stack[-1] != '(' and
                   precedence.get(token, 0) <= precedence.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(token)
    
    while stack:                     
        output.append(stack.pop())
    
    return output

#Обчислення виразу у ЗПЗ
def evaluate_postfix(postfix):
    stack = []
    
    for token in postfix:
        if token.isnumeric():
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            match token:
                case '+':
                    stack.append(a + b)
                case '-':
                    stack.append(a - b)
                case '*':
                    stack.append(a * b)
                case '/':
                    stack.append(a / b)
                case '^':
                    stack.append(a ** b)
    
    return stack[0]

def main():
    expression = input("Введіть математичний вираз: ")
    tokens = list(expression.replace(" ", ""))  # Розбиваємо вираз на токени
    postfix = infix_to_postfix(tokens)
    print("Зворотний польський запис:", " ".join(postfix))
    result = evaluate_postfix(postfix)
    print("Результат обчислення:", result)


if __name__ == "__main__":
    main()
