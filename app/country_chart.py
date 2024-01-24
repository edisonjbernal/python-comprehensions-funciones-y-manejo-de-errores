import utils
import read_csv
import charts


def run_chart():
    # Load data into dataframes
    data = read_csv.read_csv('./app/world_population.csv')
    country_name = input('Type country => ')
    result = utils.population_by_country(data, country_name)
    print(result)
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population_by_country(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)
        
if __name__ == '__main__':
    run_chart()