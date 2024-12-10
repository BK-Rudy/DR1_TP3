def q1():
    import os

    def find_path(path):
        try:
            items = os.listdir(path)
        except PermissionError:
            print(f"Permissão negada para acessar o diretório: {path}")
            return
        except FileNotFoundError:
            print(f"O diretório não foi encontrado: {path}")
            return

        for item in items:
            path_with_file = os.path.join(path, item)
            
            if os.path.isdir(path_with_file):
                print(f"Diretório: {path_with_file}")
                find_path(path_with_file)
            else:
                print(f"Arquivo: {path_with_file}")

    if __name__ == "__main__":
        path = input("Digite o caminho do diretório que deseja listar: ")
        find_path(path)

def q3():
    def hanoi(n, origin, destiny, aux):
        if n == 1:
            print(f"Mover disco 1 de {origin} para {destiny}")
            return
        hanoi(n - 1, origin, origin, destiny)
        
        print(f"Mover disco {n} de {origin} para {destiny}")
        
        hanoi(n - 1, origin, destiny, origin)

    if __name__ == "__main__":
        total_disk = 3 
        hanoi(total_disk, 'A', 'C', 'B')

def q4():
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        return n * fatorial(n - 1)
 
def q5():
    list = [5, 2, 9, 1, 7, 3]

    def quicksort(list):
        if len(list) <= 1:
            return list
        pivot = list[len(list) // 2]
        left = [x for x in list if x < pivot]
        middle = [x for x in list if x == pivot]
        right = [x for x in list if x > pivot]
        return quicksort(left) + middle + quicksort(right)

    
    ordered_list = quicksort(list)
    print(ordered_list)

def q7():
    def quickselect(list, k):
        if (len(list) == 1):
            return list[0]
        
        pivot = list[-1]

        minors = [x for x in list if x < pivot]
        equals = [x for x in list if x == pivot]
        bigger = [x for x in list if x > pivot]
        
        position = len(minors) + 1

        if k < position:  
            return quickselect(minors, k)
        elif k > position: 
            return quickselect(bigger, k - position)
        else:  
            return pivot

def q8():
    def fibonacci(n, memo={}):
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        return memo[n]

    print(fibonacci(10))

def q9():
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def in_order_traversal(root):
        
        result = []
        
        def traverse(node):
            if node is not None:
                traverse(node.left)
                result.append(node.value)
                traverse(node.right)
        
        traverse(root)
        return result

    if __name__ == "__main__":
        root = Node(4)
        root.left = Node(2)
        root.right = Node(6)
        root.left.left = Node(1)
        root.left.right = Node(3)
        root.right.left = Node(5)
        root.right.right = Node(7)

        result = in_order_traversal(root)
        print("Valores dos nós em ordem:", result)

def q11():
    def recursive(num):
        if num == 0 or num == 1:
            return 1
        
        return num * recursive(num - 1)

    def iterative(num):
        if num == 0 or num == 1:
            return 1
        
        factorial = 1
        for n in range(2, num+1):
            factorial *= n
        
        return factorial

    print(iterative(1100))

def q12():
    list = [17,20,1,100,2,66,77,88,99,10]

    def sum(list):
        if not list:
            return 0

        return list[0] + sum(list[1:])

    print(sum(list))

def q13():
    def is_palindrome(word):
        if len(word) <= 1:
            return True
        if word[0] != word[-1]:
            return False
        return is_palindrome(word[1:-1])

    if __name__ == "__main__":
        list = ["tp3", "level", "python", "carro", "arara"]
        for word in list:
            bool = is_palindrome(word)
            print(f"A palavra '{word}' é um palíndromo? {bool}")

def q14():
    list = [1, 2, 3, 4]

    def sum(list):
    
        if not list:
            return 0

        return list[0] + sum(list[1:])

    print(sum(list))

def q15():
    def repeated(word, letter):
        if len(word) == 0:
            return 0
        
        return (1 if word[0] == letter else 0) + repeated(word[1:],letter)

    print(repeated("jabuticaba", "a"))

def q16():
    def reverse(string):
        if len(string) == 0:
            return ""

        return string[-1] + reverse(string[:-1])

    print(reverse("recursao"))
    print(reverse("brasil"))
    print(reverse("argentina"))

#Execução
if __name__ == "__main__":
    print("Escolha a questão para executar:")
    print("1 - Questão 1")
    print("3 - Questão 3")
    print("4 - Questão 4")
    print("5 - Questão 5")
    print("7 - Questão 7")
    print("8 - Questão 8")
    print("9 - Questão 9")
    print("11 - Questão 11")
    print("12 - Questão 12")
    print("13 - Questão 13")
    print("14 - Questão 14")
    print("15 - Questão 15")
    print("16 - Questão 16")

    selected = input("Digite o número da questão: ")

    functions = {
        "1": q1,
        "3": q3,
        "4": q4,
        "5": q5,
        "7": q7,
        "8": q8,
        "9": q9,
        "11": q11,
        "12": q12,
        "13": q13,
        "14": q14,
        "15": q15,
        "16": q16,
    }

    if selected in functions:
        functions[selected]()
    else:
        print("Opção inválida!")
