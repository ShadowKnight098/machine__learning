import pandas as pd 
from statistics import mean, median, mode, StatisticsError 
from typing import List 
 
def compute_mean(values: List[float]) -> float: 
    return mean(values) 
 
def compute_median(values: List[float]) -> float: 
    return median(values) 
 
def compute_mode(values: List[float]): 
    try: 
        return mode(values) 
    except StatisticsError: 
        return "No unique mode found (data is multimodal)." 
 
def compute_variance(values: List[float]) -> float:
    n = len(values) 
    mean_value = compute_mean(values) 
    squared_diff_sum = sum((x - mean_value) ** 2 for x in values) 
    return squared_diff_sum / (n - 1) 
 
def compute_standard_deviation(values: List[float]) -> float: 
    variance_value = compute_variance(values) 
    return variance_value ** 0.5 
 
def main(): 
    csv_file_path = "books.csv" 
    data_frame = pd.read_csv(csv_file_path) 
 
    numeric_values = data_frame["values"].tolist() 
 
    print("Values from CSV:", numeric_values) 
    print("-" * 50) 
 
    print("Mean:", compute_mean(numeric_values)) 
    print("Median:", compute_median(numeric_values)) 
    print("Mode:", compute_mode(numeric_values)) 
    print("Variance:", compute_variance(numeric_values)) 
    print("Standard Deviation:", compute_standard_deviation(numeric_values)) 
 
if __name__ == "__main__": 
    main()