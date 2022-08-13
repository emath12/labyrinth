class Brain():
    def __init__(self):
        self.moves = []

    def push(self, move):
        """
        Adds an move to a brain store
        """
        self.moves.append(move)

    def pop(self):
        """
        Removes the top item off the stack
        :return:
        """
        return self.moves.pop()

    def retrieve_moves(self):
        """
        :return: The entire stack
        """
        return self.moves

    def is_empty(self):
        """
        :return: Boolean value, true if the stack is empty, false if it is not.
        """
        return self.moves == []

    def peek(self):
        """
        :return: the value on the top of the stack
        """
        if not self.is_empty():
            self.moves[-1]
