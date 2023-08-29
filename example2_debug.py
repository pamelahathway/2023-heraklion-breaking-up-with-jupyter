import string

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def create_figure(array1, array2, fig_title):
    fig, ax = plt.subplots()
    ax.plot(array1, array2, "-")
    ax.set_title("hello")
    fig.savefig("./figure.png")


def create_df(size):
    data = {
        "col1": np.linspace(0, 10, size),
        "col2": np.linspace(1000, 0, size),
        "col3": list(string.ascii_lowercase)[:size]
    }
    df = pd.DataFrame.from_dict(data=data)
    return df


if __name__ == "__main__":
    x = np.array([1, 2, 3])
    y = np.array([3, 7, 8])
    title = "This is a meaningful title"
    create_figure(x, y, title)

    df = create_df(20)
    print("done")


