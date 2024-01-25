def get_students_by_year(data):
    labels = []
    values = []
    for students in data:
        year_label = students['year'][:4]
        year = int(year_label)
        if year >= 2000:
            labels.append(year_label)
            values.append(float(students['students']))
    return labels,values


