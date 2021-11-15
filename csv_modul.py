import csv
souc = 0
souc1 = 0
with open("parking.csv", encoding = "utf-8") as parkoviste,\
    open("parking_out.csv", "w", encoding = "utf-8") as parkoviste_out:

    cist = csv.reader(parkoviste, delimiter = ";")
    writer  = csv.writer(parkoviste_out)

    for row in cist:
        if row[0] != "" and row[0] != "name":
            print(f"Jméno: {row[0]}, Kapacita: {row[4]}")
        try:    
            souc = souc + int(row[4])
        except ValueError:
            pass
        try:
            if row[3] == "True":
                writer.writerow([row[0], row[4]])
                souc1 = souc1 + int(row[4])
        except ValueError:
            pass
print(f"Celkový počet parkovacích míst: {souc}")
print(f"Celkový počet parkovacích míst P+R: {souc1}")

            

        