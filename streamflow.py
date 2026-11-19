import numpy as np
import matplotlib.pyplot as plt


def load_streamflow(filename):
    """Read the streamflow CSV. Return the dates and a 2D array of flows (cfs), one column per gauge."""
    data = np.genfromtxt(filename, delimiter=",", skip_header=1, dtype=str, encoding="utf-8")
    dates = np.array(data[:, 0], dtype="datetime64[m]")
    flows = data[:, 1:].astype(float)
    return dates, flows


def plot_streamflow(dates, flows, sites):
    """Plot the flow at each gauge, with the same title, labels, and formatting as the Matplotlib HW."""
    plt.figure(figsize=(12, 6))
    for column, site in enumerate(sites):
        plt.plot(dates, flows[:, column], label=f"Site {site}")

    plt.title("Provo River Streamflow Data - June 2021")
    plt.xlabel("Day of June")
    plt.ylabel("Streamflow (cfs)")
    plt.grid(True)
    plt.legend(loc="upper right")
    plt.tight_layout()
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")
    plt.show()


# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, flows, sites)
