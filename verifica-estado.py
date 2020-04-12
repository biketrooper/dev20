import csv
import sys
from datetime import datetime

params = sys.argv
print("Dados na ordem brasil.io: "+params[1]+".csv")
print("Verifica dados: "+params[2]+".csv")

cidades = []
cidadesF = []

with open(params[2]+".csv", "r") as csv_data:
    data_reader = csv.reader(csv_data, delimiter=",")
    next(data_reader)
    dados = list(data_reader)

with open(params[1]+".csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    for lines in csv_reader:
        cidade = "-"
        with open(params[2]+".csv", "r") as csv_data:
            data_reader = csv.reader(csv_data, delimiter=",")
            next(data_reader)
            confirmados = ""
            obitos = ""
            for row in dados:
                if row[0] == str(lines[4]):
                    cidade = row[0]
                    obitos = row[2]
                    if (obitos != ""):
                        obitos = int(row[2],10)

                    confirmados = row[1]
                    #print(cidade+" - "+confirmados)
                    if (confirmados != ""):
                        confirmados = int(row[1],10)
                        if (confirmados > 0 and obitos == ""):
                            obitos = 0
                    
                    print(lines[4]+" - "+str(confirmados))
            if (cidade == "-"):
                cidadesF.append(lines[4]+"/"+lines[3])
                cidade = lines[4]
        g = [str(lines[0]),str(lines[3]),cidade,confirmados,obitos]
        cidades.append(g)

#print("Cidades não listadas:")
#print(cidadesF)

formato = '%Y-%m-%d-%H-%M'
with open("verificado-"+datetime.now().strftime(formato)+".csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(cidades)