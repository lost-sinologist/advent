from pathlib import Path

problem_file = Path(__file__).parent / 'ch1.problem'

with open(problem_file) as f:
    problem_lines = f.read().splitlines()
   

def decode_problem(problem: [str]) -> dict:
    decoded = {}
    
    for line in problem[2:len(problem)]:
        key = line[0:3]

        left = line[7:10]
        right = line[12:15]

        decoded[key] = (left, right)
            
    return decoded


def follow(problem: dict, instructions: str, steps: int=0, current_key: str='AAA') -> int:
    
    for instruction in instructions:
        match instruction:
            case 'L':
                index = 0
            case 'R':
                index = 1
            case _:
                continue
        
        current_key = problem[current_key][index]
        steps += 1
        
        if current_key == 'ZZZ':
            return steps
        
    return follow(problem, instructions, steps, current_key)

       
instructions = problem_lines[0]

problem = decode_problem(problem_lines)

print(follow(problem, instructions))
