country_to_capital={'United Kingdom':'London',
                    'Brazil':'Brasilia',
                    'Morroco':'Rabat',
                    'Sweden':'Stockholm'}

capital_to_country={capital:country for country,capital in country_to_capital.items()}
print(capital_to_country)

from pprint import pprint as pp

pp(capital_to_country)

a= ['hai','hello','fox','hotel','elephant']
b={x[0]:x for x in a}
print(b)