"""
Project goals:
Region: which area has the most patients?
Age & Smoking: what is the average age for smokers vs. non-smokers?
Children and Cost: What is the average cost for each number of children a person may or may not have?
"""


# import necessary packages
import csv


# Save dataset via Python variable
patient_age = []
patient_sex = []
patient_bmi = []
num_of_children = []
smoker_vs_non_smoker = []
patient_region = []
patient_charges = []


# Save variables
with open('insurance.csv') as insurance:
    insurance_dict = csv.DictReader(insurance)
    for row in insurance_dict:
        patient_age.append(row['age'])

with open('insurance.csv') as insurance:
    insurance_dict = csv.DictReader(insurance)
    for row in insurance_dict:
        patient_sex.append(row['sex'])

with open('insurance.csv') as insurance:
    insurance_dict = csv.DictReader(insurance)
    for row in insurance_dict:
        patient_bmi.append(row['bmi'])

with open('insurance.csv') as insurance:
    insurance_dict = csv.DictReader(insurance)
    for row in insurance_dict:
        num_of_children.append(row['children'])

with open('insurance.csv') as insurance:
    insurance_dict = csv.DictReader(insurance)
    for row in insurance_dict:
        smoker_vs_non_smoker.append(row['smoker'])

with open('insurance.csv') as insurance:
    insurance_dict = csv.DictReader(insurance)
    for row in insurance_dict:
        patient_region.append(row['region'])

with open('insurance.csv') as insurance:
    insurance_dict = csv.DictReader(insurance)
    for row in insurance_dict:
        patient_charges.append(row['charges'])

print(patient_age)
print(patient_sex)
print(patient_bmi)
print(num_of_children)
print(smoker_vs_non_smoker)
print(patient_region)
print(patient_charges)


# All of the lists contain strings. The lists 'patient_age', 'patient_bmi', 'num_of_children', and 'patient_charges'
# must be transformed into integers.
for i in range(len(patient_age)):
    patient_age[i] = float(patient_age[i])
for i in range(len(patient_bmi)):
    patient_bmi[i] = float(patient_bmi[i])
for i in range(len(num_of_children)):
    num_of_children[i] = float(num_of_children[i])
for i in range(len(patient_charges)):
    patient_charges[i] = float(patient_charges[i])


# Which area has the most patients?
# Create dictionary where each unique region is the key and the number of patients in that region is the value
def patient_counter(lst):
    dictionary = {}
    for item in lst:
        if item in dictionary:
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    return dictionary


region_counts = patient_counter(patient_region)
print(region_counts)


# Then using that dictionary, create a function that pulls the region with the most patients and its value
def most_patients(dictionary):
    region = None
    region_count = 0
    for key, value in dictionary.items():
        if value > region_count:
            region = key
            region_count = value
    return region, region_count


region_most_patients = most_patients(region_counts)
print(region_most_patients)


# What is the average age for smokers vs non-smokers?
# Create list zipping the smoker status and ages together
# zip patient_smoker and patient_age together
smoker_ages = list(zip(smoker_vs_non_smoker, patient_age))
smoker_ages_list = [list(x) for x in smoker_ages]


# Then take the values of that list and return the average
yes_smoker_ages = []
non_smoker_ages = []
for nested in smoker_ages_list:
    if nested[0] == 'yes':
        yes_smoker_ages.append(nested[1])
    else:
        non_smoker_ages.append(nested[1])


for num in range(len(yes_smoker_ages)):
    yes_smoker_ages[num] = yes_smoker_ages[num]
for num in range(len(non_smoker_ages)):
    non_smoker_ages[num] = non_smoker_ages[num]


smoker_avg = round(sum(yes_smoker_ages) / len(yes_smoker_ages), 2)
non_smoker_avg = round(sum(non_smoker_ages) / len(non_smoker_ages), 2)
print("The average age of patients who smoke is " + str(smoker_avg))
print("The average age of patients who do not smoke is " + str(non_smoker_avg))


# What is the average cost for each number of children a person may have?
# What are the unique numbers of children among patients in the dataset?
print(list(set(num_of_children)))


# Each patient has between 0 and 5 children (all-inclusive)
# Iterate through num_of_children and patient_charges to create list of charges per number of children
zero_children_cost = []
one_child_cost = []
two_children_cost = []
three_children_cost = []
four_children_cost = []
five_children_cost = []


for i in range(len(num_of_children)):
    for i in range(len(patient_charges)):
        if num_of_children[i] == 0:
            zero_children_cost.append(patient_charges[i])
        if num_of_children[i] == 1:
            one_child_cost.append(patient_charges[i])
        if num_of_children[i] == 2:
            two_children_cost.append(patient_charges[i])
        if num_of_children[i] == 3:
            three_children_cost.append(patient_charges[i])
        if num_of_children[i] == 4:
            four_children_cost.append(patient_charges[i])
        if num_of_children[i] == 5:
            five_children_cost.append(patient_charges[i])


zero_children_cost_avg = round(sum(zero_children_cost) / len(zero_children_cost), 2)
one_child_cost_avg = round(sum(one_child_cost) / len(one_child_cost), 2)
two_children_cost_avg = round(sum(two_children_cost) / len(two_children_cost), 2)
three_children_cost_avg = round(sum(three_children_cost) / len(three_children_cost), 2)
four_children_cost_avg = round(sum(four_children_cost) / len(four_children_cost), 2)
five_children_cost_avg = round(sum(five_children_cost) / len(five_children_cost), 2)


print("The average insurance charge for patients with no children is $" + str(zero_children_cost_avg) + ".")
print("The average insurance charge for patients with one child is $" + str(one_child_cost_avg) + ".")
print("The average insurance charge for patients with two children is $" + str(two_children_cost_avg) + ".")
print("The average insurance charge for patients with three children is $" + str(three_children_cost_avg) + ".")
print("The average insurance charge for patients with four children is $" + str(four_children_cost_avg) + ".")
print("The average insurance charge for patients with five children is $" + str(five_children_cost_avg) + ".")
