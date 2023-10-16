import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Average Calculator")

        self.numbers = []
        self.max_radius = 10

        self.fig = Figure(figsize=(5, 5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_aspect("equal", adjustable="datalim")
        self.ax.set_xlim((-self.max_radius * 1.5, self.max_radius * 1.5))
        self.ax.set_ylim((-self.max_radius * 1.5, self.max_radius * 1.5))

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.entry = tk.Entry(self)
        self.entry.pack(side=tk.LEFT)

        self.add_button = tk.Button(self, text="Add Number", command=self.add_number)
        self.add_button.pack(side=tk.LEFT)

        self.avg_button = tk.Button(
            self, text="Calculate Average!", command=self.calculate_average
        )
        self.avg_button.pack(side=tk.LEFT)

    def draw_slices(self, radius, slice_angle):
        for angle in range(
            0, 360, slice_angle
        ):  # Draw a line every 'slice_angle' degrees
            end_x = radius * math.cos(math.radians(angle))
            end_y = radius * math.sin(math.radians(angle))
            self.ax.plot([0, end_x], [0, end_y], color="grey", linestyle="dashed")

    def add_number(self):
        user_input = self.entry.get()
        try:
            number = float(user_input)
            self.numbers.append(number)
            self.entry.delete(0, "end")

            total = sum(self.numbers)
            average = total / len(self.numbers)
            total_radius = math.sqrt(total / math.pi)
            self.max_radius = max(self.max_radius, total_radius)

            self.ax.clear()
            self.ax.set_xlim((-self.max_radius * 1.5, self.max_radius * 1.5))
            self.ax.set_ylim((-self.max_radius * 1.5, self.max_radius * 1.5))
            circle = self.ax.add_patch(plt.Circle((0, 0), total_radius, color="blue"))
            average_proportion = average / total
            slice_angle = int(
                360 * average_proportion
            )  # Convert average proportion to degrees
            self.draw_slices(total_radius, slice_angle)  # Draw the slices
            self.ax.text(
                0.95,
                0.95,
                f"Total: {total}",
                ha="right",
                va="top",
                transform=self.ax.transAxes,
                color="black",
            )
            self.canvas.draw()

        except ValueError:
            messagebox.showerror("Error", "Invalid input, please enter a number")

    def calculate_average(self):
        if self.numbers:
            total = sum(self.numbers)
            average = total / len(self.numbers)
            average_proportion = average / total

            total_radius = math.sqrt(total / math.pi)
            wedge_theta = (
                360 * average_proportion
            )  # Convert average proportion to degrees
            wedge = self.ax.add_patch(
                Wedge(
                    center=(0, 0),
                    r=total_radius,
                    theta1=0,
                    theta2=wedge_theta,
                    color="red",
                )
            )
            self.ax.text(
                0.95,
                0.90,
                f"Average: {average}",
                ha="right",
                va="top",
                transform=self.ax.transAxes,
                color="black",
            )
            self.canvas.draw()


app = Application()
app.mainloop()
