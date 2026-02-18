import csv

with open('input.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader, None)  # ignorer l'en-tête si présent

    with open('output.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['nom', 'salaire'])

        for row in reader:
            try:
                nom = row[0]
                heures = float(row[1])
                salaire = heures * 15
                writer.writerow([nom, salaire])
            except (ValueError, IndexError):
                continue




