from flask import Flask,render_template, request
from datetime import date

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():

     # data recovery from the data base 
     with open("bdd/bdd.txt", 'r') as data:
          lines = data.readlines()

     # dictionary list creation for the best handling
     data = []
     for line in lines:
          element = line.split(";")
          dico = {}
          dico['names'] = element[0]
          dico['date'] =element[3].rstrip('\n') +"/"+element[2].strip()+"/"+element[1] .strip()
          data.append(dico)

     if request.method=='POST':     
           nom = request.form['search'].strip()
          doc =  {}
          for line in data:
               if nom == line['names']:
                    doc = dict(line)
                    break

          return render_template('result.html',title='result page',line=doc) 
        
     else:
          return render_template('home.html', title='Home page',lines=data)
  
          
""" 

this route sorts the database to return the oldest on the list

"""
@app.route('/plus_age',methods=['GET'])
def plus_age():

     with open("bdd/bdd.txt", 'r') as data:
          lines = data.readlines()
     data = []

     year = date.today().year
     agesup = 1
     for line in lines:

          element = line.split(";")
          dico = {}
          dico['names'] = element[0]
          dico['annee'] =element[1].strip()
          dico['age'] = year - int(element[1].strip())
          age = year - int(element[1].strip())

          data.append(dico)

          #sort to retain the oldest age
          if age >= agesup:
               agesup =age 



     olderdata =  {}
     for part in data:
         
          if agesup == part['age']:
               olderdata = dict(part)
               break
     app.logger.debug(olderdata)

     return render_template('age.html',titrepage='Informations du plus agé',line=olderdata)

""" 
this route sorts the database to return the younger on the list

"""
@app.route('/plus_jeune',methods=['GET'])
def plus_jeune():
     with open("bdd/bdd.txt", 'r') as data:
          lines = data.readlines()
     data =[]
     year = date.today().year
     
     listeage = []
     
     for line in lines:
     
          element = line.split(";")
          dico = {}
          dico['names'] = element[0]
          dico['annee'] =element[1].strip()
          dico['age'] = year - int(element[1].strip())
          age = year - int(element[1].strip())

          listeage.append(age)

          data.append(dico)

     ageinf = min(listeage)
     

     youngerdata =  {}
     for part in data:
         
          if ageinf == part['age']:
              
               youngerdata = dict(part)
               break
    

     return render_template('age.html',titrepage='Informations du plus agé',line=youngerdata)
     

""" 
this route sorts the database to return the upcoming birthday

"""
@app.route('/a_venir',methods=['GET'])
def a_venir():

     with open("bdd/bdd.txt", 'r') as data:
          lines = data.readlines()
     data =[]
     year = date.today().year
     
     listedelta = []
     # app.logger.debug(year)
     for line in lines:
               # print(line)
          element = line.split(";")
          dico = {}
          dico['names'] = element[0]
          dico['annee'] =element[1].strip()
          dico['date'] =element[3].rstrip('\n') +"/"+element[2].strip()+"/"+element[1] .strip()
          dico['age'] = year - int(element[1].strip())
          dico['delta'] = int(str(date(  date.today().year, int(element[2].strip()), int(element[3].strip())  ) - date.today()).split(" ")[0] )
          

          listedelta.append(dico['delta'])

          data.append(dico)

     listedeltapositif = []
     for delta in listedelta:
          if (delta >=0 ):
               listedeltapositif.append(delta)
               
     deltamin = min(listedeltapositif)

     near_birth_data =  {}
     for part in data:
         
          if  deltamin == part['delta']:
               
               near_birth_data = dict(part)
               break
 
     return render_template('age.html',titrepage='Information concernant l\'anniversaire la plus proche',line=near_birth_data)
     
