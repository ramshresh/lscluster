import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as patches
import matplotlib.lines as mlines
from matplotlib.path import Path

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import matplotlib.path as mpath
from matplotlib.legend_handler import HandlerTuple, HandlerLine2D
from matplotlib.dates import DateFormatter, date2num

class DashedLineWithDots:
    def __init__(self, x, y, x_range=None, y_range=None, line_style='--', dot_marker='o', line_color='black', dot_color='black', alpha=1):
        self.x = x
        self.y = y
        self.line_style = line_style
        self.dot_marker = dot_marker
        self.line_color = line_color
        self.dot_color = dot_color
        self.alpha = alpha
        self.x_range = x_range if x_range is not None else min(self.x), max(self.x)
        self.y_range = y_range if y_range is not None else min(self.y), max(self.y)

    def is_valid_datetime(self, string, format='"%Y-%m-%d %H:%M:%S"'):
        try:
            datetime.strptime(string, format)
            return True
        except ValueError:
            return False
        
    def create_patch(self, ax):

        # all_numeric = all(isinstance(v, (int, float)) for v in self.x)
        # x = date2num(self.x)

        if all(isinstance(v, (int, float)) for v in self.x):
            x = self.x
        elif all(isinstance(v, (datetime.date, datetime.datetime)) for v in self.x):
            x = date2num(self.x)
        elif all(isinstance(v, str) for v in self.x) and all(self.is_valid_datetime(v) for v in self.x):
            # Convert dates to numerical format
            x = date2num(self.x) 
        else:
            print([type(v) for v in self.x])
            raise Exception('Unhandled Exception')
            
        y = self.y

        # Create the dashed line patch
        self.line_patch = mpatches.PathPatch(
            mpath.Path([(x[0], y[0])] + list(zip(x[1:], y[1:])), [mpath.Path.MOVETO] + [mpath.Path.LINETO] * (len(x) - 1)),
            edgecolor=self.line_color,
            facecolor='none',
            linestyle=self.line_style,
            alpha=self.alpha
        )

        # Plot the data points as dots
        self.dot_patch = mlines.Line2D(x, y, linestyle='', marker=self.dot_marker, color=self.dot_color, alpha=self.alpha)
        
        # # Set the x-axis and y-axis limits
        # ax.set_xlim(min(x), max(x))
        # ax.set_ylim(min(y), max(y))

        # Add the line and dot patches to the plot
        ax.add_patch(self.line_patch)
        ax.add_line(self.dot_patch)

    def create_legend_patch(self):
        # Create the legend
        # Create the composite legend element
        # Get the proxy artists for the Line2D objects
        line_proxy = mlines.Line2D([5], [5], linestyle=self.line_style, color=self.line_color, alpha=self.alpha)
        dot_proxy = mlines.Line2D([0], [0], linestyle=self.line_style, marker=self.dot_marker, color=self.dot_color, alpha=self.alpha)
        return  (line_proxy, dot_proxy)
    

    def add_to_legend(self, ax, label):
        # Create the legend
        # Create the composite legend element
        # Get the proxy artists for the Line2D objects
        line_proxy = mlines.Line2D([5], [5], linestyle='--', color=self.line_color)
        dot_proxy = mlines.Line2D([5], [5], linestyle='', marker=self.dot_marker, color=self.dot_color)

        patch = self.create_legend_patch()

        # Set the proxy artists for the legend elements
        self.legend_elements = [patch]
        self.legend_labels = [label]

        ax.legend(self.legend_elements, self.legend_labels, handler_map={mlines.Line2D: HandlerLine2D(numpoints=2)}, loc='upper left',  bbox_to_anchor=(1.1, 1))



class LineWithSideBar:
    x1 = None
    x2 = None
    y = None
    data = None
    def __init__(self, data=None, line_color='black',line_width=1, alpha=1, line_style='-') -> None:
        self.data = data
        self.line_color = line_color
        self.line_width = line_width
        self.line_style = line_style
        self.alpha = alpha


    def plot(self, ax, data=None):
        # Separate columns into x, y, z variables
        if data is not None:
            self.x1, self.x2, self.y = zip(*data) 
        elif self.data is not None:
            self.x1, self.x2, self.y = zip(*self.data) 
        else:
            raise Exception("Data not set")
        

        x1 = date2num(self.x1)
        x2 = date2num(self.x2)
        y = self.y

        data_range = max(y) - min(y)

        bar_height = 0.01*data_range 


        data = zip(x1, x2, y)
        for _x1, _x2, _y in data:
            self.hline_patch = mlines.Line2D([_x1, _x2], [_y, _y], color=self.line_color, linewidth=self.line_width, alpha=self.alpha, linestyle=self.line_style)
            self.bar_left_patch = mlines.Line2D([_x1, _x1], [_y+bar_height, _y-bar_height], color=self.line_color, linewidth=self.line_width, alpha=self.alpha)
            self.bar_right_patch = mlines.Line2D([_x2, _x2], [_y+bar_height, _y-bar_height], color=self.line_color, linewidth=self.line_width, alpha=self.alpha)

            ax.add_line(self.hline_patch)
            ax.add_line(self.bar_left_patch)
            ax.add_line(self.bar_right_patch)
            
            self.legend_patch = (
                self.hline_patch, 
                self.bar_left_patch, 
                self.bar_right_patch
                )
            
            
            
            
    def create_legend_patch(self):
        hline_patch = mlines.Line2D([0, 10], [0, 0], color=self.line_color, linewidth=self.line_width, alpha=self.alpha, linestyle=self.line_style)
        bar_left_patch = mlines.Line2D([0, 0], [5, -5], color=self.line_color, linewidth=self.line_width, alpha=self.alpha)
        bar_right_patch = mlines.Line2D([10, 10], [5, -5],color=self.line_color, linewidth=self.line_width, alpha=self.alpha)

        
        
        # return self.legend_patch
        return (hline_patch, bar_left_patch, bar_right_patch)
    
    
class RectSymbol:
    symbolizer = None
    symbol_patch = None
    data_patches = []
    def __init__(self, symbolizer=None) -> None:
        self.symbolizer = symbolizer
    def make_patch(self, pos, width, height):
        patch = patches.Rectangle(pos, width, height, **self.symbolizer)
        return patch
    
    def create_legend_patch(self):
        patch = self.make_patch((1,0), 1, 1)
        return patch
    
    def add_to_legend(self, ax, label):
        patch = self.make_legend_patch()
        ax.legend([patch], [label], handler_map={mlines.Line2D: HandlerLine2D(numpoints=1)}, loc='upper left',  bbox_to_anchor=(1.1, 1))

    def add_data_patch(self, ax, pos, width, height):
        patch = self.make_patch(pos, width, height)
        ax.add_patch(patch)
        self.data_patches.append(patch)

def make_rectangle_patch(pos, width, height, symbolizer):
    # pos = (1,0)
    # width  = 10
    # height = 1
    rect = patches.Rectangle(pos, width, height, **symbolizer)
    return rect

def make_precipitation_symbol(symbolizer):
    """
    Usage:
    legend = ax.legend([patch], ['Composite Patch'], loc='upper right')
    """
    # Create custom composite patch
    vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
    codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
    path = Path(vertices, codes)
    patch = patches.PathPatch(path, **symbolizer)

    return patch

def get_series(min_value, max_value, interval):
    upper_divisible = max_value + (interval - (max_value % interval)) % interval
    i = interval
    a = min_value
    if upper_divisible == max_value:
        b =  max_value  + interval +1
    else:
        b = upper_divisible + 1
    # Generate the series of integers
    series = list(range(a, b, i))
    return series
