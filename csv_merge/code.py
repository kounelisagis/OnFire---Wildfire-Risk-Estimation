import pandas as pd
import csv
import os

locations = ["parnitha",
            "neamakri",
            "spata",
            "lavrio",
            "vari"]

path = ""

for location in locations:
    with open("final/" + location + ".csv", 'w') as writeFile:
        writer = csv.writer(writeFile)
        #writeFile.close()

        with open("fires/" + location + ".csv") as firesfile:
            input1 = csv.reader(firesfile, delimiter=',')
            #print(location)
            for row1 in input1:
                date = row1[0].split('/')
                acres = row1[1]
                txtfilename = date[2] + "-" + str(int(date[0])) + ".txt"
                with open(location + "/" + txtfilename) as weatherfile:
                    input2 = csv.reader(weatherfile, delimiter=',')
                    rows = list(input2)
                    #print(len(rows))
                    #print(int(date[1]))
                    writer.writerow(row1+rows[int(date[1])-1])


        
        '''for i in range(0, len(file['start_date'])):

            #file['acres']
            try:
                print(x)
                strings = x.split('/')
                year = strings[2]
                day = int(strings[1])
                month = strings[0]
                # print(type(day))
                # print(year)
                # print(month)
                data = pd.read_csv(path+"text_to_csv_old/"+location+"/"+year+"-"+month+".txt", error_bad_lines=False, header=None)
                writer.writerow(line)

                #print(data)
            except Exception as e:
                print(e)
        '''

