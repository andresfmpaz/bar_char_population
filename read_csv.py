import csv


def read_csv(path):
    try:
        with open(path, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter =',')
            for row in reader:
                print("*********** "*5)
                print(row)
    except FileNotFoundError as error:
        print(error)
        

def create_dict_from_csv(path):
    try:
        with open(path, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter =',')
            header = next(reader)
            data = []
            for row in reader:
                iterable = zip(header, row)                
                country_dic = {key: value for key, value in iterable}
                data.append(country_dic)
    except FileNotFoundError as error:
        print(error)
        return None
    return data



if __name__ == '__main__':
    #read_csv('./app/data.csv')
    dic = create_dict('./data.csv')
    print(dic[1])
   