import utils
import read_csv
import charts


def run_chart():
    # Load data into dataframes
    data = read_csv.read_csv('./app/world_population.csv')
    labels, values = utils.get_population_in_world(data)
    charts.generate_pie_chart("World Population", labels, values)
    
        
if __name__ == '__main__':
    run_chart()