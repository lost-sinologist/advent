def main():
    with open("ch1.problem") as f:
        problem = f.read().split("\n")
        
    solution = 0
    
    for line in problem:
        solution += solve_line(line)
        
    print(solution)
    print(len(problem))
    

def solve_line(line: str):
    d1 = iterate_line(line)
    d2 = iterate_line(reversed(line))
    
    return int(d1 + d2)

def iterate_line(line):
    for letter in line:
        if letter.isdigit():
            print(letter + ' is digit!!')
            return letter
        
    return 0

if __name__ == "__main__":
    main()