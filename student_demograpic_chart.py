import student_demografic_app.utils_students as utils_students
import app.read_csv
import app.charts as charts

# Run chart

def run_chart():
    # Load data into dataframes
    data = app.read_csv.read_csv('./student_demografic_app/academic.csv')
    labels, values = utils_students.get_students_by_year(data)
    charts.generate_pie_chart("Students Demographical By Year", labels, values)
    
        
if __name__ == '__main__':
    run_chart()