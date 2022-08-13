import random

class Room:
    def __init__(self, id, prev, treasure=False):
        self.id = id
        self.left: Room = None
        self.right: Room = None
        self.next: Room = None
        self.prev: Room = prev
        self.treasure = treasure

    def print_by_row(self):
        rows = []
        b_index = 0
        room = self

        while room:

            rows.append([])
            columns = rows[b_index]

            columns.append(room.id)

            if room.left:
                left = room.left
                while left:
                    columns.insert(0, left.id)
                    left = left.left

            if room.right:
                right = room.right
                while right:
                    columns.append(right.id)
                    right = right.right

            room = room.next

            b_index += 1

        for row in rows:
            print(row)


class Location:
    def __init__(self, far_left: bool, far_right: bool, far_front: bool, rows_deep: int):

        """

        Instruction passed to append to notate where it should go.

        :param far_left: bool
        :param far_right: bool
        :param far_front: bool
        :param rows_deep: int
        """

        if (far_left and far_right) or (far_left and far_front) or (far_right and far_front) or (far_right and far_front and far_left):
            print("invalid instruction")

        if far_left:
            self.location = "far_left"
        elif far_right:
            self.location = "far_right"
        elif far_front:
            self.location = "far_front"

        if rows_deep < 0:
            print("invalid rows_deep call")
        else:
            self.rows_deep = rows_deep

class GridLink:

    def __init__(self):
        self.head: Room = None
        self.total_rooms = 0

    def append_room(self, loc: Location, treasure: bool):
        """
        Append a room to the edges of the grid. Far left indicates that you want it appended to the far left
        of the indicated row. Far right indicates the same but vice versa. Far_front indicates
        that you want it appended to the tip of the indicated row.
        :param loc: A location struct
        :param treasure: boolean for whether or not the appended room should contain treasure
        :return: void
        """
        if self.head is None:
            self.head = Room(id=0, prev=None, treasure=treasure)
        else:
            cur_room = self.head
            rows_deep = loc.rows_deep

            while rows_deep != 0:
                if not cur_room:
                    print("you entered an invalid row_deep value")
                    return

                cur_room = cur_room.next

                rows_deep -= 1

            the_last_room = None

            if loc.location == "far_left":
                while cur_room:
                    the_last_room = cur_room
                    cur_room = cur_room.left

                new_room = Room(id=self.total_rooms, prev=the_last_room, treasure=treasure)
                the_last_room.left = new_room

            elif loc.location == "far_right":
                while cur_room:
                    the_last_room = cur_room
                    cur_room = cur_room.right

                new_room = Room(id=self.total_rooms, prev=the_last_room, treasure=treasure)
                the_last_room.right = new_room

            elif loc.location == "far_front":
                while cur_room:
                    the_last_room = cur_room
                    cur_room = cur_room.next

                new_room = Room(id=self.total_rooms, prev=the_last_room, treasure=treasure)
                the_last_room.next = new_room

            else:
                print("invalid instruction")

        self.total_rooms += 1

    def generate_labyrinth(self, room_amt):
        """
        Generates a random connected grid of rooms for the labyrinth demonstrative game.
        :param room_amt: int
        :return: none
        """

        if room_amt < 5:
            print("maze too small! boo!")

        contains_treasure = False

        generated_rooms = 1
        valid_row_deep = 0
        direction = ["far_left", "far_right", "far_front"]
        self.append_room(Location(False, False, True, 0), contains_treasure)

        while generated_rooms != room_amt:
            pick = direction[random.randint(0, 2)]

            if generated_rooms >= room_amt and not contains_treasure:
                if random.randint(0, 1) == 0:
                    contains_treasure = True

            if pick == "far_front":
                insert_row = random.randint(0, valid_row_deep)
                self.append_room(Location(False, False, True, insert_row), contains_treasure)
                valid_row_deep += 1

            elif pick == "far_left":
                insert_row = random.randint(0, valid_row_deep)
                self.append_room(Location(False, True, False, insert_row), contains_treasure)

            else:
                insert_row = random.randint(0, valid_row_deep)
                self.append_room(Location(True, False, False, insert_row), contains_treasure)

            generated_rooms += 1

    def print_as_matrix(self):
        """
        Prints the existing grid as a matrix. Note: if the number of cols and rows and uneven,
        the print will reflect such. Prints the id to indicate which room is which.
        :return: none
        """
        if self.head is None:
            print("S")
        else:
            self.head.print_by_row()



