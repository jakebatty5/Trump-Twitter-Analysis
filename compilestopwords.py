file = open('stopwords.txt', 'r')
file = file.read()
file = file.replace(' ','')

print(file)