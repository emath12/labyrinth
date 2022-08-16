# The Labyrinth

Welcome to the Labyrinth! The Labyrinth exists as demonstration of a data structure I implemented: the sqaurely linked list (SLL). 

Inspired by my data structures class I took at Yale, I wanted to make my own data structure, hence the birth of this project. The data structure I came up
with is a type of linked list, except each node is aware of its previous, right, top and bottom node! 

Think of an SLL as a 2d grid. Each box on the grid would be a node. Execpt, this grid can have some boxes that are missing. Not all pointers in the SLL are
valid, that depends on how it was defined.

To get this MVP out, I designed two functions to go along with my novel implementation: append() and print_by_matrix(). append() allows you to add a node
to the far left, right or front of the SLL, and you have complete control over how deep you append left or right you append it as well. print_by_matrix() 
allows you to print your SLL out in a matrix like form, row by row. Note, this works best when your SLL is a perfect grid.

More functions are in the works for my SLL library, including insert(position, node) and remove(position, node). 

However, the functionality I have now is more than enough for use, so I made a little CLI game with it: The Labyrinth, to desmonstrate exactly how it works.

The goal of the labyrinth is to traverse a randomly generated SLL to find the room that contains the treasure. Nodes become rooms, otherwise, everything
else is the same. You can go to the right, left, forwards or backwards. The game is, admittedly, incredibly unforiging: if you enter an invalid room, you
die and have to restart!

So, enjoy the labyrinth and please keep a look out for more refinement to my SLL and new features that are on the way!
