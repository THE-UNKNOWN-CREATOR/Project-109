import pandas as pd
import plotly.figure_factory as pf
import statistics
import plotly.graph_objects as go

raw_data = pd.read_csv("StudentsPerformance.csv")
marks_data = []

raw_math_score = raw_data["math score"]
raw_reading_score = raw_data["reading score"]
raw_writing_score = raw_data["writing score"]

def raw_to_int(raw):
    i = []

    for val in raw:
        i_v = int(val)
        i.append(i_v)

    return i

math_score = raw_to_int(raw_math_score)
reading_score = raw_to_int(raw_reading_score)
writing_score = raw_to_int(raw_writing_score)

score_len = len(raw_data)

for i in range(0, score_len):
    total_score = math_score[i] + reading_score[i] + writing_score[i]
    marks_data.append( total_score )

mean = sum(marks_data) / len(marks_data)
standard_dev = statistics.stdev(marks_data)
median = statistics.median(marks_data)
mode = statistics.mode(marks_data)

# find first standard deviation
first_std_dev_start, first_std_dev_end = mean - standard_dev, mean + standard_dev
second_std_dev_start, second_std_dev_end = mean - (2 * standard_dev), mean + (2 * standard_dev)
third_std_dev_start, third_std_dev_end = mean - (3 * standard_dev), mean + (3 * standard_dev)


pic = pf.create_distplot([marks_data], ["marks_data"], show_hist=False)
pic.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.04], mode="lines", name="mean"))
pic.add_trace(go.Scatter(x=[first_std_dev_start, first_std_dev_start], y=[0, 0.04], mode="lines", name="standard deviation 1"))
pic.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[0, 0.04], mode="lines", name="standard deviation 1"))
pic.add_trace(go.Scatter(x=[second_std_dev_start, second_std_dev_start], y=[0, 0.04], mode="lines", name="standard deviation 2"))
pic.add_trace(go.Scatter(x=[second_std_dev_end, second_std_dev_end], y=[0, 0.04], mode="lines", name="standard deviation 2"))
pic.add_trace(go.Scatter(x=[third_std_dev_start, third_std_dev_start], y=[0, 0.04], mode="lines", name="standard deviation 3"))
pic.add_trace(go.Scatter(x=[third_std_dev_end, third_std_dev_end], y=[0, 0.04], mode="lines", name="standard deviation 3"))
pic.show()

print("The Mean of the data is {mean}")
print("The Median of the data is {median}")
print("The Mode of the data is {mode}")
print("The Standard Deviation of the data is {standard_dev}")

list_of_data_within_first_std_dev = [result for result in marks_data if result > first_std_dev_start and result < first_std_dev_end]
print("{}% of data within first standard deviation".format(len(list_of_data_within_first_std_dev) * 100 / len(marks_data)))
list_of_data_within_second_std_dev = [result for result in marks_data if result > second_std_dev_start and result < second_std_dev_end]
print("{}% of data within second standard deviation".format(len(list_of_data_within_second_std_dev) * 100 / len(marks_data)))
list_of_data_within_third_std_dev = [result for result in marks_data if result > third_std_dev_start and result < third_std_dev_end]
print("{}% of data within third standard deviation".format(len(list_of_data_within_third_std_dev) * 100 / len(marks_data)))

print(mean, median, mode, standard_dev)
