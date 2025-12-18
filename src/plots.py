import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class TextPlots:
    """
    A class for visualizing text data.
    Methods:
        plot_top_k: Plots top-k words as a bar chart.
        compare_top_k: Plots top-k words for two datasets side by side.
        plot_categories: Plots category word frequencies for two datasets side by side.
    """

    def plot_top_k(self, sorted_items, k, title):
        """
        Plots a bar chart of the top-k words in a single dataset.
        Args:
            sorted_items (list of tuples): Word counts sorted by frequency
            k (int): Number of top words to display
            title (str): Title for the chart
        """
        top_k = dict(sorted_items[:k])
        fig = px.bar(
            x=list(top_k.keys()),    # words on x-axis
            y=list(top_k.values()),  # counts on y-axis
            title=f"Top {k} Words in {title}"
        )
        fig.show()

    def compare_top_k(self, sorted1, sorted2, k, name1, name2):
        """
        Plots two side-by-side bar charts of top-k words for comparison.
        Args:
            sorted1, sorted2 (list of tuples): Word counts sorted by frequency
            k (int): Number of top words to display
            name1, name2 (str): Titles for the two charts
        """
        top1 = dict(sorted1[:k])
        top2 = dict(sorted2[:k])

        fig = make_subplots(rows=1, cols=2,
                            subplot_titles=(name1, name2))

        # add bar chart for first dataset
        fig.add_trace(go.Bar(x=list(top1.keys()), y=list(top1.values())), row=1, col=1)
        # add bar chart for second dataset
        fig.add_trace(go.Bar(x=list(top2.keys()), y=list(top2.values())), row=1, col=2)

        # layout settings
        fig.update_layout(
            title=f"Top {k} Words Comparison",
            height=500, width=1000,
            showlegend=False
        )
        fig.show()

    def plot_categories(self, cat1, cat2, name1, name2):
        """
        Plots two side-by-side bar charts of category word frequencies.
        Args:
            cat1, cat2 (dict): Category counts for two datasets
            name1, name2 (str): Titles for the two charts
        """
        fig = make_subplots(rows=1, cols=2,
                            subplot_titles=(name1, name2))

        # add bar chart for first dataset categories
        fig.add_trace(go.Bar(
            x=list(cat1.keys()),
            y=list(cat1.values()),
        ), row=1, col=1)

        # add bar chart for second dataset categories
        fig.add_trace(go.Bar(
            x=list(cat2.keys()),
            y=list(cat2.values()),
        ), row=1, col=2)

        # layout settings
        fig.update_layout(
            title="Category Word Frequency Comparison",
            height=500, width=1000,
            showlegend=False
        )
        fig.show()
