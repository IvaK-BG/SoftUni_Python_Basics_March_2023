period = int(input())
doctors = 7
treated_patients = 0
untreated_patients= 0
new_doctors = 0
for day in range(1, period + 1):
    patients_for_review = int(input())
    if day % 3 == 0 and untreated_patients > treated_patients:
        new_doctors += 1
    if patients_for_review <= (doctors + new_doctors):
        treated_patients += + patients_for_review
    else:
        treated_patients += + (doctors + new_doctors)
        untreated_patients += patients_for_review - (doctors + new_doctors)
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")

