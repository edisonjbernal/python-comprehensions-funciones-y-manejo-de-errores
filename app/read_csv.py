import csv

#https://www.kaggle.com/

def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        data = []
        for row in reader:
            #print('---' * 10)
            iterable = zip(headers, row)
            #print(list(iterable))
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
            #print(row)
        return data



if __name__ == '__main__':
   data = read_csv('./app/world_population.csv')
   print(data)