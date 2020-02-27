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

    def book_sort_key(b):
        return books[int(b)].score

    libraries = []
    i = 0
    lib_index = 2
    while(i < n_libraries):
        libr_descr = get_tokens(lines[lib_index])
        lib_n_books = int(libr_descr[0])
        sign_up_time = int(libr_descr[1])
        books_per_day = int(libr_descr[2])

        lib_books = get_tokens(lines[lib_index + 1])
        sorted_l_books = sorted(lib_books, key=book_sort_key, reverse=True)
        libraries.append(Library(
            i, sign_up_time, sorted_l_books, books_per_day))

        i += 1
        lib_index += 2


    return Problem(libraries, books, n_days)


def get_tokens(line):
    return line.split('\n')[0].split(" ")

def write_output(solution, output_file):
    file_obj = open(output_file, "w")
    file_obj.write(str(len(solution)) + "\n")
    for s in solution:
        (library, books) = s
        file_obj.write(str(library.l_id) + " " + str(len(books)) + "\n")
        file_obj.write(" ".join([str(b) for b in books]) + "\n")

    file_obj.close()

class ProblemSolver:
    def __init__(self, problem):
        self.problem = problem
        self.currently_signing = -1
        self.last_signed = -1
        self.started_on = None

    def solve(self):
        sorted_libraries = sorted(self.problem.libraries, key=self.sort_key)
        book_scores = [b.score for b in self.problem.books]
        score = 0
        solution = []
        day_index = 0
        for library in sorted_libraries:
            day_index += library.sign_up_time
            if (day_index >= self.problem.n_days):
                break
            days_left = (self.problem.n_days - 1) - day_index
            n_books_possible = days_left * library.books_per_day
            book_count = 0
            books = []
            for b in library.books:
                if (book_count >= n_books_possible):
                    break
                bid = int(b)
                if (book_scores[bid] == 0):
                    continue

                books.append(bid)
                score += book_scores[bid]
                book_scores[bid] = 0
                book_count += 1
            solution.append((library, books))

        return (score, solution)

    def sort_key(self, library):
        return library.sign_up_time
        
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
    def __init__(self, bid, score):
        self.id = bid
        self.score = score

if __name__ == "__main__":
    main()