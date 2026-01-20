import csv

roles = []
skills = []
salaries = []

with open("data/jobs_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        roles.append(row["Role"])
        skills.append(row["Skill"])
        salaries.append(int(row["Salary"]))

average_salary = sum(salaries) / len(salaries)

print("Total Jobs Analyzed:", len(roles))
print("Average Salary (€):", average_salary)

print("\nTop Skills Demand:")
for skill in set(skills):
    print(skill, ":", skills.count(skill))
