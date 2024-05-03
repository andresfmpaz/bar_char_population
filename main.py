import utils
import read_csv
import charts




def run():
    data = read_csv.create_dict_from_csv('./data.csv')
    print('data len ',len(data))
   
    country = input(" Type the Country ->")
    result = utils.get_population_by_country(data,country)
    print('Result', result)
    if len(result) > 0:
        print('Country found -> ',country)
        labels, values = utils.get_population(result[0])
        charts.generate_bar_chart(labels, values, country)        
    else:
        print('Country not found!! ')
   
   

if __name__ == '__main__' :
    run()