input_files = [
    "data/a_example.txt",
    "data/b_read_on.txt",
    "data/c_incunabula.txt",
    "data/d_tough_choices.txt",
    "data/e_so_many_books.txt",
    "data/f_libraries_of_the_world.txt"
]

output_dir = "output"

def main():
    global input_files
    global output_dir

    for file in input_files:
        problem = parse_input(file)
        problem_solver = ProblemSolver(problem)
        (score, solution) = problem_solver.solve()
        output_file = output_dir + "/" \
            + file.split("/")[-1].split(".")[0] + ".out"
        write_output(solution, output_file)
        print("Solved", file, "Scored", score, 
            "Saved to", output_file)
        print()

def parse_input(file):
    pass

def write_output(solution, output_file):
    pass

class ProblemSolver:
    def __init__(self, problem):
        pass

    def solve(self):
        pass


class Library:
    def __init__(self, id, books):
        pass

    def has_book(self, id):
        pass

if __name__ == "__main__":
    main()