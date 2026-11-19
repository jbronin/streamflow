import csv
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


def summarize(dates, flows, sites):
    """Print and save maximum, minimum, and average flow for each gauge."""
    # Excel check for gauge 10163000: max = 131.0 cfs; average = 56.9523611111 cfs.
    header = f"{'Gauge':<10}{'Max (cfs)':>12}   {'Date of max':<19}{'Min (cfs)':>12}{'Avg (cfs)':>12}"
    print(header)

    with open("streamflow_summary.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Gauge", "Max (cfs)", "Date of max", "Min (cfs)", "Avg (cfs)"])

        for column, site in enumerate(sites):
            gauge_flows = flows[:, column]
            max_index = np.argmax(gauge_flows)
            max_flow = np.max(gauge_flows)
            date_of_max = np.datetime_as_string(dates[max_index], unit="m").replace("T", " ")
            min_flow = np.min(gauge_flows)
            avg_flow = np.mean(gauge_flows)

            print(f"{site:<10}{max_flow:12.1f}   {date_of_max:<19}{min_flow:12.1f}{avg_flow:12.1f}")
            writer.writerow([site, f"{max_flow:.1f}", date_of_max, f"{min_flow:.1f}", f"{avg_flow:.1f}"])


# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
summarize(dates, flows, sites)
plot_streamflow(dates, flows, sites)
