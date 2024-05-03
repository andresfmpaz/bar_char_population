
import re
import matplotlib.pyplot as plt
#import matplotlib
import sys


def generate_bar_chart():
    labels = ['a', 'b', 'c']
    values = [100, 300 , 344]
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.show()

def generate_bar_chart(labels, values, country):
    fig, ax = plt.subplots()
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'pink', 'cyan', 'yellow']
    bars = ax.bar(labels, values, color = colors)
    ax.bar_label(bars)
    ax.set_title('Population of:  '+ country)
    ax.set_xlabel('Years')  
    ax.set_ylabel('Populations in Millions') 
    plt.show()
 
def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels) 
    ax.axis('equal')
    plt.show()
       
if __name__ == '__main__':
   labels = ['a', 'b', 'c', 'r']
   values = [100, 1000 ,34 , 33]
   generate_bar_chart(labels,values)
   generate_pie_chart(labels,values)
   #print(sys.path)


