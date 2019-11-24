import requests


base_url = "http://meteosearch.meteo.gr/data/"

locations = ["parnitha",
            "neamakri",
            "spata",
            "lavrio",
            "vari"]


url = ""

for location in locations:
    for year in range(2012, 2019):
        for month in range(1, 13):
            if month < 10:
                url = base_url + location + '/' + str(year) + '-0' + str(month) + '.txt'
            else:
                url = base_url + location + '/' + str(year) + '-' + str(month) + '.txt'

            r = requests.get(url) # create HTTP response object
            f = open(location+'/'+str(year)+'-'+str(month)+".txt", "w")
            f.write(r.content)
            f.close()
