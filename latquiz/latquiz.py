import pandas as pd

class Quiz:
        def run(self,dchart): 
                cases = ['Nominative','Genitive','Dative','Accusative','Ablative']
                number = ['Singular','Plural']
                endings = []
                for y in range(2):
                        num = number[y]
                        for i in range(5):
                                case = cases[i]
                                user_answer = input(case+' '+num+': ')
                                endings.append(user_answer)
                #print(endings)
                sing = endings[:5]
                pl = endings[5:]
                correctsing = dchart['S.']
                correctpl = dchart['Pl.']
                index_sing = 0
                index_pl = 0
                errors_sing = 0
                errors_pl = 0
                for s in range(len(sing)):
                        if sing[s] != correctsing[s]:
                                errors_sing = errors_sing+1
                                
                                        
                        if pl[s] != correctpl[s]:
                                errors_pl = errors_pl+1
                                
              
        
                if errors_sing > 0 or errors_pl > 0:
                        print("You made a total of "+str(errors_sing+errors_pl)+" error(s). Consult the chart below and compare it to "+"\n"+"your answers to see where you went wrong")
                        print(str(errors_sing)+" error(s) in the singular")
                        print(str(errors_pl)+" error(s) in the plural")
                        print("Your answers were: ")
                        print(endings)
                        print(dchart)
                else:
                        print("\n"+ "Correct. You made no mistakes"+"\n")
