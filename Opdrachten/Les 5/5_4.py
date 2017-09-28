import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y")

file = open('hardlopers.txt', 'a')


tijd =(input('Wat is de tijd wat je hebt gelopen?:'))
naam =(input('Wat is je naam?:'))

file.write('{}, {}, {}\n'.format(s,tijd,naam))