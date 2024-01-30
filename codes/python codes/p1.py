import matplotlib.pyplot as plt

# Read data from file
with open('data.txt', 'r') as file:
    data = [tuple(map(float, line.split())) for line in file]

# Extract n and y(n) values
n_values, y_values = zip(*data)

# Plot stem plot
plt.stem(n_values, y_values, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.xlabel('n')
plt.ylabel('y(n)')

# Mark y(n) = 200 in a different color
plt.axhline(y=200, color='r', linestyle='--', label='y(n) = 200')

plt.legend()
plt.grid(True)
plt.savefig('f2.png')
plt.show()

