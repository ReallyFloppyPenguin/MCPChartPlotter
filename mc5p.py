from typing import List
from mcp.server.fastmcp import FastMCP
import matplotlib.pyplot as plt

# Initialize FastMCP server
mcp = FastMCP("plot_chart") # Changed server name

@mcp.tool()
def plot_bar_chart(labels: List[str], values: List[float], title: str = "My Chart", filename: str = "plot.png") -> str:
    """
    Generates a simple bar chart using matplotlib and saves it to a file.

    Args:
        labels: A list of strings for the x-axis labels.
        values: A list of numbers for the y-axis values.
        title: The title of the chart. Defaults to "My Chart".
        filename: The name of the file to save the chart to (e.g., 'my_chart.png'). Defaults to "plot.png".

    Returns:
        A string message indicating where the chart was saved or an error message.
    """
    if not labels or not values:
        return "Error: Labels and values cannot be empty."
    if len(labels) != len(values):
        return "Error: The number of labels must match the number of values."

    try:
        fig, ax = plt.subplots()
        ax.bar(labels, values)
        ax.set_ylabel('Values')
        ax.set_title(title)
        
        # Improve x-axis label display
        ax.set_xticks(range(len(labels)))
        ax.set_xticklabels(labels, rotation=45, ha="right") # Rotate for better readability
        
        plt.tight_layout() # Adjust layout to prevent labels from overlapping
        plt.show()
        plt.savefig(filename)
        plt.close(fig) # Close the figure to free up memory
        return f"Chart '{title}' saved to {filename}"
    except Exception as e:
        # Log the exception for server-side debugging
        print(f"Error generating chart: {e}")
        return f"Error generating chart: {str(e)}"

@mcp.tool()
def plot_line_chart(labels: List[str], values: List[float], title: str = "My Line Chart", filename: str = "line_plot.png") -> str:
    """
    Generates a simple line chart using matplotlib and saves it to a file.

    Args:
        labels: A list of strings for the x-axis labels.
        values: A list of numbers for the y-axis values.
        title: The title of the chart. Defaults to "My Line Chart".
        filename: The name of the file to save the chart to (e.g., 'my_line_chart.png'). Defaults to "line_plot.png".

    Returns:
        A string message indicating where the chart was saved or an error message.
    """
    if not labels or not values:
        return "Error: Labels and values cannot be empty."
    if len(labels) != len(values):
        return "Error: The number of labels must match the number of values."

    try:
        fig, ax = plt.subplots()
        ax.plot(labels, values, marker='o') # Added marker for better visibility of points
        ax.set_ylabel('Values')
        ax.set_xlabel('Labels')
        ax.set_title(title)
        
        ax.set_xticks(range(len(labels)))
        ax.set_xticklabels(labels, rotation=45, ha="right")
        
        plt.tight_layout()
        plt.savefig(filename)
        plt.close(fig)
        return f"Chart '{title}' saved to {filename}"
    except Exception as e:
        print(f"Error generating line chart: {e}")
        return f"Error generating line chart: {str(e)}"

@mcp.tool()
def plot_pie_chart(labels: List[str], sizes: List[float], title: str = "My Pie Chart", filename: str = "pie_plot.png") -> str:
    """
    Generates a simple pie chart using matplotlib and saves it to a file.

    Args:
        labels: A list of strings for the pie chart slices.
        sizes: A list of numbers representing the size of each slice.
        title: The title of the chart. Defaults to "My Pie Chart".
        filename: The name of the file to save the chart to (e.g., 'my_pie_chart.png'). Defaults to "pie_plot.png".

    Returns:
        A string message indicating where the chart was saved or an error message.
    """
    if not labels or not sizes:
        return "Error: Labels and sizes cannot be empty."
    if len(labels) != len(sizes):
        return "Error: The number of labels must match the number of sizes."
    if any(s < 0 for s in sizes):
        return "Error: Sizes for a pie chart cannot be negative."

    try:
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.set_title(title)
        
        plt.tight_layout()
        plt.savefig(filename)
        plt.close(fig)
        return f"Chart '{title}' saved to {filename}"
    except Exception as e:
        print(f"Error generating pie chart: {e}")
        return f"Error generating pie chart: {str(e)}"

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')