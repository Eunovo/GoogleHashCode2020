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

    for file in input_files[0:1]:
        problem = parse_input(file)
        print("Parsed ", file)
        problem_solver = ProblemSolver(problem)
        problem_solver.solve()
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
        lib_n_books = int(libr_descr[0])
        sign_up_time = int(libr_descr[1])
        books_per_day = int(libr_descr[2])

        lib_books = get_tokens(lines[lib_index + 1])
        libraries.append(Library(
            lib_id, sign_up_time, lib_books, books_per_day))

        i += 2


    return Problem(libraries, books, n_days)


def get_tokens(line):
    return line.split('\n')[0].split(" ")

def write_output(solution, output_file):
    pass

class ProblemSolver:
    def __init__(self, problem):
        self.problem = problem
        self.currently_signing = -1
        self.last_signed = -1
        self.started_on = None

    def solve(self):
        sorted_libraries = sorted(self.problem.libraries, key=self.sort_key)
        # print([l.sign_up_time for l in sorted_libraries])
        signed_libraries = []
        day_index = 0
        while(day_index < self.problem.n_days):
            new_lib = self.handle_signup(day_index, sorted_libraries)
            if (new_lib != None):
                signed_libraries.append(new_lib)
            


            day_index += 1

    def sort_key(self, library):
        return library.sign_up_time

    def handle_signup(self, day, libraries):
        def start_next():
            next_index = self.last_signed + 1
            if (next_index >= len(libraries)):
                return
            self.currently_signing = next_index
            self.started_on = day

        if (self.currently_signing == -1):
            start_next()
            return None

        current_lib = libraries[self.currently_signing]
        if (day - self.started_on == current_lib.sign_up_time):
            self.last_signed = self.currently_signing
            self.currently_signing = -1
            start_next()
            return current_lib
        return None
        
class Problem:
    def __init__(self, libraries, books, n_days):
        self.libraries = libraries
        self.books = books
        self.n_days = n_days

class Library:
    def __init__(self, l_id, sign_up_time, books, books_per_day):
        self.l_id = l_id
        self.sign_up_time = sign_up_time
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