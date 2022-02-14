####################################
# PROYECTO 1 INTRODUCCION A PYTHON #
#        YESENIA CAMPOS            #
####################################

import datetime  # To mmodify dates
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

############   LOGIN  #############

# Declaration of user and password variables

registeredUser = ('LifeStore')
registeredPW = ('password123')
counter = 5
userRegister = False

while userRegister != True and counter > 0:
    counter -= 1
    user = input('User: ')
    passw = input('Password: ')

    # verify credentials
    if user == registeredUser and passw == registeredPW:
        userRegister = True
        print('Welcome ', user)
    else:
        print('ERROR! User is not registered. Try again. Attempts:')
        print(f'Attempts: {counter}')


############   Top sellers and lagging products  #############

# declaration of the variable products sold
productSold = [sale[1] for sale in lifestore_sales]
productSearches = [search[1] for search in lifestore_searches]
counterSold = []
counterSearch = []
# create list with the number of times sold
for sales in lifestore_products:
    listProducts = []
    counterSold.append(listProducts)
    for i in range(1):
        listProducts.append(sales[0])  # ID product
        listProducts.append(sales[1])  # Name product
        listProducts.append(sales[-2])  # Category product
        listProducts.append(productSold.count(sales[0]))  # Times Sold

# Function that sorts the sellers


def greaterSales(counterSold):
    counterSold.sort(key=lambda x: x[3])
    return counterSold


counterSold = greaterSales(counterSold)

# print 5 most and least sold products
print('####  The most sales products:  #####')
for j in [-1, -2, -3, -4, -5]:
    print(
        f' \t Id: {counterSold[j][0]} Name: {counterSold[j][1]} Sales: {counterSold[j][3]}')

print('####  The least sales products:  #####')
for k in range(0, 5):
    print(
        f'\t Id: {counterSold[k][0]} Name: {counterSold[k][1]} Sales: {counterSold[k][3]}')

# create list with the number of times search
for search in lifestore_products:
    listProducts2 = []
    counterSearch.append(listProducts2)
    for i in range(1):
        listProducts2.append(search[0])  # ID product
        listProducts2.append(search[1])  # Name product
        listProducts2.append(search[-2])  # Category product
        listProducts2.append(productSearches.count(search[0]))  # Times Search

counterSearch = greaterSales(counterSearch)

# print 10 most and least searched products
print('####  The most searched products:  #####')
for j in [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]:
    print(
        f' \t Id: {counterSearch[j][0]} Name: {counterSearch[j][1]} Searched: {counterSearch[j][3]}')

print('####  The least searched products:  #####')
for k in range(0, 10):
    print(
        f'\t Id: {counterSearch[k][0]} Name: {counterSearch[k][1]} Searched: {counterSearch[k][3]}')

############   Products per service review  #############

# Generating list of products
bestRated = {}
for idSale, idProduct, rate, date, refund in lifestore_sales:
    if rate not in bestRated.keys():
        bestRated[rate] = [idProduct]
    else:
        bestRated[rate].append(idProduct)

# To each scoreRate, sort idProducts considering rates given and refund
topBestRated = {}
for rate, producstList in bestRated.items():
    topBestRated[rate] = []
    for idProduct in range(len(lifestore_products)):
        if idProduct in producstList:
            topBestRated[rate].append(
                (idProduct, producstList.count(idProduct)))
        else:
            continue

# Sorting using lambda function
for rate, producstList in topBestRated.items():
    topBestRated[rate] = sorted(producstList, key=lambda x: x[1], reverse=True)

# Verifying which products were sold and then returned to the store
refunds = []
totalRefunds = {}

for idSale, idProduct, rate, date, refund in lifestore_sales:
    if refund == 1:
        refunds.append(lifestore_products[idProduct-1][1])
for product in refunds:
    if product not in totalRefunds.keys():
        totalRefunds[product] = refunds.count(product)
    else:
        continue

print("####  Best Reviews:  ####")
count = 1
for idProduct, numRates in topBestRated[5]:
    print(count, "Product:",
          lifestore_products[idProduct-1][1], "Rate:", numRates)
    count += 1
    if count > 5:
        break

print("####  Worst Reviews:  ####")
countW = 1
for rates, lists in list(topBestRated.items())[::-1]:
    for id_product, num_rates in lists:
        print(countW, "Product:",
              lifestore_products[idProduct-1][1], "Rate:", numRates)
        countW += 1
        if countW > 1:
            break

# Getting list of products returned
productsRefunded = sorted(totalRefunds.items(),
                          key=lambda x: x[1], reverse=True)

print("####  Refunds products:  ####")
for productNames, numRefunds in productsRefunded:
    print(f'Product: {productNames}, Refunds:{numRefunds}')


### Total income and average monthly sales,annual total and months with more sales per year #####

# Getting just id of products sold
totalSales = []

for index in range(len(lifestore_sales)):
    totalSales.append(lifestore_sales[index][1])

# Getting incomes per each product
incomes = []

for product in totalSales:
    incomes.append(lifestore_products[product-1][2])


# Total income
totalIncome = sum(incomes)


# Incomes per months and year, generatin list of sales by date
salesDate = []
for id_sales, idProduct, rate, date, refund in lifestore_sales:
    newDate = datetime.datetime.strptime(date, '%d/%m/%Y').date()
    salesDate.append((idProduct, newDate))


# Generating lists of months per year
month2019 = []
month2020 = []
for idProduct, date in salesDate:
    if date.year == 2020:
        month2020.append(date.month)
    elif date.year == 2019:
        month2019.append(date.month)

# Generatin a dict of dicts, to each year, show the quantity of sales by months registered
monthlySales = {}
monthlySales[2019] = {}
monthlySales[2020] = {}
for month in range(1, 13):
    if month in month2019:
        monthlySales[2019][month] = month2019.count(month)
    elif month in month2020:
        monthlySales[2020][month] = month2020.count(month)

monthNames = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
              "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Total incomes per year
incomesPerYear = {}
for year in monthlySales.keys():
    yearIncome = 0
    for months in monthlySales[year].keys():
        for dates, price in zip(salesDate, incomes):
            if dates[1].year == year:
                if dates[1].month == months:
                    yearIncome += price
    incomesPerYear[year] = yearIncome

# Total incomes per month
incomesPerMont = {}
for months in list(monthlySales[2020].keys())+list(monthlySales[2019].keys()):
    countIncome = 0
    for dates, price in zip(salesDate, incomes):
        if dates[1].month == months:
            countIncome += price
        else:
            continue
    incomesPerMont[months] = (monthNames[months-1], countIncome)

# Sort months by the income generated
topMonthIncomes = sorted(list(incomesPerMont.items()),
                         key=lambda x: x[1][1], reverse=True)

print('Annual incomee: $', totalIncome)
print('Average monthly income: $', '%.2f' % (totalIncome/12))
print('Incomes per month:', incomesPerMont)
print('Incomes per year:', incomesPerYear)
