import pandas as pd
import latquiz

class csv:
        def main():
                quiz = latquiz.Quiz()
                declensions = {'1':'1st declension fem.','2':'2nd declension masc.','3':'2nd declension n.','4':"3rd declension m/f",'5':'3rd declension n.'}
                for i in range(1,6):
                    print('')
                    print("Decline "+declensions[str(i)]+"\n")
                    chart = str(i)+".csv"
                    dchart = pd.read_csv(chart)
                    quiz.run(dchart)
                        
        main()
        
