import random
import math
import tkinter as tk
#3
def generate_initial_solution(N):
    "Generates a random initial solution."
    return [random.randint(0, N-1) for _ in range(N)]
#4
def evaluate_solution(solution):
    "Evaluates the current solution."
    conflicts = 0
    N = len(solution)
    for i in range(N):
        for j in range(i + 1, N):
            if solution[i] == solution[j] or abs(solution[i] - solution[j]) == abs(i - j):
                conflicts += 1
    return conflicts
#5
def copy_solution(solution):
    "Copies the solution."
    return solution[:]
#6
def print_solution(solution):
    "Prints the queens' placement on the board."
    N = len(solution)
    print("╔" + "═" * (N*2 - 1) + "╗")
    for row in range(N):
        line = "║"
        for col in range(N):
            if solution[col] == row:
                line += 'Q '
            else:
                line += '. '
        print(line[:-1] + "║")
    print("╚" + "═" * (N*2 - 1) + "╝")

def show_solution_in_window(solution):
    "Displays the queens' placement on the board in a separate window."
    N = len(solution)

    # Create a window
    window = tk.Tk()
    window.title("Queens Placement")

    # Create a canvas for displaying the board
    canvas = tk.Canvas(window, width=N*50, height=N*50, bg='white')
    canvas.pack()

    # Draw the board
    for i in range(N):
        for j in range(N):
            color = 'white' if (i + j) % 2 == 0 else 'gray'
            canvas.create_rectangle(j*50, i*50, (j+1)*50, (i+1)*50, fill=color)
            if solution[j] == i:
                canvas.create_text(j*50 + 25, i*50 + 25, text='♕', font=('Arial', 24))

    window.mainloop()
#7
def simulated_annealing(N, max_iterations, initial_temperature, cooling_rate):
    "Implementation of the simulated annealing algorithm."
    current_solution = generate_initial_solution(N)
    best_solution = copy_solution(current_solution)
    current_energy = evaluate_solution(current_solution)
    best_energy = current_energy

    temperature = initial_temperature

    for iteration in range(max_iterations):
        if best_energy == 0:
            break

        # Randomly change the current solution
        new_solution = copy_solution(current_solution)
        queen_to_move = random.randint(0, N-1)
        new_solution[queen_to_move] = random.randint(0, N-1)

        # Evaluate the new solution
        new_energy = evaluate_solution(new_solution)

        # Accept the new solution or keep the old one
        if new_energy < current_energy or random.random() < math.exp(-(new_energy - current_energy) / temperature):
            current_solution = new_solution
            current_energy = new_energy

        # Update the best solution if necessary
        if current_energy < best_energy:
            best_solution = copy_solution(current_solution)
            best_energy = current_energy

        # Decrease the temperature
        temperature *= cooling_rate

    return best_solution, best_energy

if __name__ == "__main__":
    N = 16  # Board size
    max_iterations = 2000  # Maximum number of iterations
    initial_temperature = 500.0  # Initial temperature
    cooling_rate = 0.95  # Cooling rate

    found_solution = False
    attempts = 0

    while not found_solution:
        attempts += 1
        print(f"Attempt {attempts}...")

        # Run the simulated annealing algorithm
        solution, conflicts = simulated_annealing(N, max_iterations, initial_temperature, cooling_rate)

        # Check for solution
        if conflicts == 0:
            print("Solution found:")
            print_solution(solution)
            show_solution_in_window(solution)  # Display the solution in a window
            found_solution = True
        else:
            print("Solution not found. Number of conflicts:", conflicts)
