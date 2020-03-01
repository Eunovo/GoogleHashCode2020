import unittest
from solution import Book, Library, Problem, ProblemSolver

class ProblemSolverTest(unittest.TestCase):
    def test_solve_skips_already_scanned_books(self):
        books = [
            Book(0, 5),
            Book(1, 5),
            Book(2, 5),
            Book(3, 5)
        ]
        libraries = [
            Library(0, 2, [0, 1, 2], 1),
            Library(1, 2, [0, 1, 2, 3], 1)
        ]
        problem = Problem(libraries, books, 5)
        solver = ProblemSolver(problem)
        (score, solution) = solver.solve()
        self.assertEqual(score, 20)
        self.assertEqual(len(solution), 2)
        self.assertEqual(solution[0][0].l_id, libraries[0].l_id)
        self.assertEqual(solution[0][1], [0, 1, 2])
        self.assertEqual(solution[1][0].l_id, libraries[1].l_id)
        self.assertEqual(solution[1][1], [3])

if __name__ == "__main__":
    unittest.main()