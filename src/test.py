with open('..\src\items.csv', 'r', encoding='windows-1251') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        print(row['name'], int(row['price']), int(row['quantity']))