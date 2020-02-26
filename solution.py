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
        print("Parsed ", file)
        # problem_solver = ProblemSolver(problem)
        # (score, solution) = problem_solver.solve()
        # output_file = output_dir + "/" \
        #     + file.split("/")[-1].split(".")[0] + ".out"
        # write_output(solution, output_file)
        # print("Solved", file, "Scored", score, 
        #     "Saved to", output_file)
        # print()

def parse_input(file):
    file_obj = open(file, "r")
    lines = file_obj.readlines()
    file_obj.close()
    first_line = get_tokens(lines[0])
    if (len(first_line) != 3):
        raise Error('Problem parameter line is invalid')
    n_books = int(first_line[0])
    n_libraries = int(first_line[1])
    n_days = int(first_line[2])

    second_line = get_tokens(lines[1])
    if (len(second_line) != n_books):
        raise ValueError('Number of books do not match')
    books = [Book(t, int(second_line[t])) for t in range(n_books)]

    libraries = []
    start_index = 2
    i = 0
    while(i < (n_libraries * 2)):
        lib_index = i + start_index
        libr_descr = get_tokens(lines[lib_index])
        lib_id = i
        lib_n_books = libr_descr[0]
        sign_up_time = libr_descr[1]
        books_per_day = libr_descr[2]

        lib_books = get_tokens(lines[lib_index + 1])
        libraries.append(Library(lib_id, lib_books, books_per_day))

        i += 2


    return Problem(libraries, books, n_days)


def get_tokens(line):
    return line.split('\n')[0].split(" ")

def write_output(solution, output_file):
    pass

class ProblemSolver:
    def __init__(self, problem):
        pass

    def solve(self):
        pass

class Problem:
    def __init__(self, libraries, books, n_days):
        self.libraries = libraries
        self.books = books
        self.n_days = n_days

class Library:
    def __init__(self, l_id, books, books_per_day):
        self.l_id = l_id
        self.books = books
        self.books_per_day = books_per_day
        

    def has_book(self, id):
        pass

class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score

if __name__ == "__main__":
    main()