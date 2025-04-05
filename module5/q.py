import pandas as pd

df = pd.read_csv('student.csv')
avg_cgpa = df['CGPA'].mean()
print("Average CGPA:", avg_cgpa)

high_cgpa = df[df['CGPA'] > 9]
print("Students with CGPA > 9:\n", high_cgpa)

cse_high = df[(df['Branch'] == 'CSE') & (df['CGPA'] > 9)]
print("CSE Students with CGPA > 9:\n", cse_high)

max_cgpa_student = df[df['CGPA'] == df['CGPA'].max()]
print("Student with maximum CGPA:\n", max_cgpa_student)

branch_avg_cgpa = df.groupby('Branch')['CGPA'].mean()
print("Average CGPA of each branch:\n", branch_avg_cgpa)
