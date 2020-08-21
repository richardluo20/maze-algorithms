import time
from implementation import *

# ACCEPT A TXT FILE
# process file, turn into 2D list representing maze spaces
maze = []
fileIn = ""

while fileIn != "/quit":
    maze = []   # reset list after each attempt
    fileIn = input("Enter a file name or /quit. ")
    
    if fileIn == "/quit" or fileIn == "quit":
        # not really necessary, but I don't want an error message to show up
        break
    try:
        with open(fileIn) as file_object:
            lines = file_object.readlines()

        for line in lines:
            maze.append(list(line.rstrip()))

        for i in range(len(maze)):
            print(''.join(maze[i]))
        print()
        

        m = GridWithWeights(len(maze), len(maze[0]))
        m.walls = find_walls(maze)
        m_start = find_start(maze)
        m_end = find_end(maze)
        m.set_spaces()
        m.weights = {i:1 for i in m.spaces}

        parents = breadth_first_search_2(m, m_start)
        draw_grid(m, width=1, point_to=parents, start=m_start)
        print()

        # scan maze using breadth first search
        print("Breadth First Search")
        start = time.time()
        parents, count = breadth_first_search_3(m, m_start, m_end)
        end = time.time()
        print("Time taken:", end-start)
        print("Count:",count)
        draw_grid(m, width=1, point_to=parents, start=m_start, goal=m_end)
        print()

        # scan maze using Dijkstra's algorithm
        print("Dijkstra")
        start = time.time()
        came_from, cost_so_far, count = dijkstra_search(m, m_start, m_end)
        end = time.time()
        print("Time taken:", end-start)
        print("Count:",count)
        draw_grid(m, width=1, point_to=came_from, start=m_start, goal=m_end)
        print()
        draw_grid(m, width=2, number=cost_so_far, start=m_start, goal=m_end)
        print()
        draw_grid(m, width=1,
                  path=reconstruct_path(came_from, start=m_start, goal=m_end),
                  start=m_start, goal=m_end)
        print()

        # scan maze using A-star algorithm
        print("A*")
        start = time.time()
        came_from, cost_so_far, count = a_star_search(m, m_start, m_end)
        end = time.time()
        print("Time taken:", end-start)
        print("Count:",count)
        draw_grid(m, width=1, point_to=came_from, start=m_start, goal=m_end)
        print()
        draw_grid(m, width=2, number=cost_so_far, start=m_start, goal=m_end)
        print()
        draw_grid(m, width=1,
                  path=reconstruct_path(came_from, start=m_start, goal=m_end),
                  start=m_start, goal=m_end)
        print()

    except FileNotFoundError:
        print("Sorry, file not found.")
        print()

    except UnboundLocalError:
        print("The maze is invalid. Either a start or end space is missing.")
        print()

