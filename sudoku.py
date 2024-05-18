from helpers import *


class SudokuGame:
    def __init__(self, board=None):
        if board is None:
            board = initial_state()
        self.board = board
        self.domains = {
            (i, j): list(range(1, 10))
            for i in range(9) for j in range(9) if not board[i][j]
        }

    def enforce_consistency(self):
        """
        Update `self.domains` such that each variable is consistent with
        its row, column, and group
        """

        for i, j in self.domains.keys():
            for num in self.domains[i, j].copy():
                if (num in self.board[i] or num in to_column_major(self.board)[j]
                        or num in to_group_major(self.board)[get_group(i, j)]):
                    self.domains[i, j].remove(num)

    def solve(self):
        self.enforce_consistency()
        assignment = self.backtrack(dict())
        return assignment

    def select_unassigned_variable(self, assignment):
        """
        :param assignment: The current assignment of variables
        :return: The variable to assign a value to based on which variable has the smallest domain
        """

        fields = [var for var in self.domains.keys() if var not in assignment.keys()]
        fields.sort(key=lambda x: (len(self.domains[x])))
        return fields[0] if fields else None

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        Sudoku cell variable); return False otherwise.
        """

        return self.domains.keys() == assignment.keys()

    def create_board_from_assignment(self, assignment):
        b = self.board.copy()
        for i, j in assignment.keys():
            b[i][j] = assignment[i, j]

        return b

    def backtrack(self, assignment):
        print(self.domains.keys(), assignment.keys())
        if self.assignment_complete(assignment) and check_validity(self.create_board_from_assignment(assignment)):
            return assignment

        var = self.select_unassigned_variable(assignment)

        if var is None:
            return None

        for val in self.domains[var]:
            if val not in assignment.values():
                assignment[var] = val

                if not check_validity(self.create_board_from_assignment(assignment)):
                    assignment.pop(var)
                    continue

                result = self.backtrack(assignment)
                if result is not None:
                    return result
                assignment.pop(var)

        return None
