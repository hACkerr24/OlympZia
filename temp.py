import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from tabulate import tabulate
import winsound
def beep():
    f=600
    d=200
    winsound.Beep(f,d)
def beep1():
    f=800
    d=800
    winsound.Beep(f,d)
def mainmenu():    
    print('\t\t\t\t\t\t-----------------------')
    print('\t\t\t\t\t\t| Welcome To OlympZia |')
    print('\t\t\t\t\t\t-----------------------')
    print("\n\n------------------------------")
    print('|(1) About Olympics          |')
    print('------------------------------')
    print('|(2) Data Analysis           |')
    print('------------------------------')
    print('|(3) Future Prediction       |')
    print('------------------------------')
    print('|(4) Feedback                |')
    print('------------------------------')
    print("")
    print("")
    global choice
    choice= int(input('Enter Your Choice=> '))
def menu():
    print("")
    print("")
    print('-------------------------------------')      
    print('|(1) Top Countries                  |')
    print('-------------------------------------')
    print('|(2) Top Players                    |')
    print('-------------------------------------')
    print('|(3) Participating Countries        |')
    print('-------------------------------------')
    print('|(4) Men Olympic Records            |')
    print('-------------------------------------') 
    print('|(5) Women Olynmpic Records         |')
    print('-------------------------------------')
    print('|(6) World Record vs Olympic Record |')
    print('-------------------------------------') 
    print('|(7) Exit Data Analysis             |')
    print('-------------------------------------')  
    
    print("")
    print("")
    global choice1
    choice1= int(input('Enter Your Choice=> ')) 
def menu1():
    print("")
    print("")
    print('-------------------------------------')      
    print('|(1) Inroduction                    |')
    print('-------------------------------------')
    print('|(2) Origin                         |')
    print('-------------------------------------')
    print('|(3) The Games Transform            |')
    print('-------------------------------------')
    print('|(4) Olympian Motto                 |')
    print('-------------------------------------') 
    print('|(5) Olympian Aspirants and Athlete |')
    print('-------------------------------------')
    print('|(6) Conclusion                     |')
    print('-------------------------------------') 
    print('|(7) Exit About Section             |')
    print('-------------------------------------')  
    print("")
    print("")
    global choice2
    choice2= int(input('Enter Your Choice=> ')) 
    print("")
    print("")
    
def logo():
    print("")
    print("") 

    print("""                                      000     000     000
                                     0   0   0   0   0   0
                                    0     000     000     0
                                     0   0   0   0   0   0
                                      000     000     000
                                         0   0   0   0
                                          000     000""")
    print("")
    print("")  
oly=1
if oly == 1 :
    mainmenu()
    if choice == 1:
      print("____________________")
      beep()
      logo()
      menu1()
      if choice2 == 1:
          beep()
          print("Introduction : ")
          print("The Olympic Games, commonly referred to as the Olympics, are the highest level of athletic competition and reflect the values of world peace and good sportsmanship")
          print("This quadrennial competition, which dates back to ancient Greece, has developed into a magnificent spectacle that unifies nations, honors athletic prowess, and promotes brotherhood among participants from various backgrounds") 
          print("The Olympics have a long history that dates back thousands of years, and they have come to represent friendship, cooperation, and the pursuit of human potential on a global scale")
          print("This article examines the importance, background, and effects of the Olympic Games on both the larger world stage and people's daily lives.")
          print("")
          print("") 
          menu1()
      
      if choice2 == 2:
          beep()
          print("Origin : ")
          print("The first Olympic Games were held in Olympia somewhere in the eighth century BCE in Ancient Greece, which is where the Olympics got their start")
          print("Early Olympics were religious celebrations honoring the Greek god Zeus and featured athletic contests such chariot races, discus throws, sprinting, and wrestling")
          print("The competition was only open to male athletes, and it promoted harmony and cooperation among the frequently at war city-states of ancient Greece.")
          print("")
          print("")
          menu1()
          
      if choice2 == 3:
          beep()
          print("The Games Transform : ")
          print("The magnitude and diversity of the Olympics have substantially increased since its resurgence. Attracting thousands of competitors from almost every nation on earth, the Summer and Winter Olympics are now alternated every two years")
          print("The variety of sports has increased to include both more recent additions like snowboarding, skateboarding, and beach volleyball as well as more established ones like athletics, swimming, and gymnastics.")
          print("")
          print("")
          menu1()
       
      if choice2 == 4:
          beep()
          print("Olympian Motto : ")
          print("The Olympic motto, Citius, Altius, Fortius, which translates to Faster, Higher, Stronger sums up the guiding ideals of the games")
          print("This adage motivates athletes to constantly push the envelope and pursue personal achievement.")
          print("")
          print("")
          menu1()
          
      if choice2 == 5:
          beep()
          print("Motivating Olympian Aspirants and Athletes : ")
          print("For athletes, competing in the Olympics is the pinnacle of their ambitions and the reward for years of effort, discipline, and commitment")
          print("Aspiring Olympians might get inspiration from the event, which inspires them to pursue their passion and succeed in their chosen sport")
          print("Athletes can utilize the Olympics as a platform to promote social concerns and act as role models, using their influence to change the world.")
          print("")
          print("")
          menu1()
          
      if choice2 == 6:
          beep()
          print("Conclusion : ")
          print("The Olympic Games are a celebration of the potential, resiliency, and harmony of humanity rather than just a competition of athletic prowess")
          print("The Olympics continue to inspire and enthrall people all around the world, from its ancient roots to the contemporary spectacular") 
          print("The Games are proof of how effective sport is at building community, mutual respect, and international cooperation")
          print("Every time the Olympics are held, we are reminded that the human spirit is limitless in its capacity for greatness and that the quest of excellence knows no bounds.")
          print("")
          print("")
          menu1()
          
      if choice2 == 7:
          beep()
          mainmenu()
      
      if choice2 > 7:
          beep1()
          print("Invalid Input Enter A Valid Number")
          menu1()
#########################################################################################
    if choice==2: 
      print("____________________")  
      beep()
      menu()
      
      if choice1 == 1:
          print("____________________")
          beep()
          print("")
          print("")
          print('------------------------------------')  
          print('| Graph Of Top 5  Countries So Far |')
          print('------------------------------------')  
          N = 5
          ind = np.arange(N)
          width = 0.1

          xvals = [1180,296,293,258,257]
          bar1 = plt.bar(ind, xvals, width, color = 'gold')

          yvals = [959,320,293,289,224]
          bar2 = plt.bar(ind+width, yvals, width, color='silver')

          zvals = [841,332,306,327,261]
          bar3 = plt.bar(ind+width*2, zvals, width, color = 'brown')

          plt.xlabel("Countires")
          plt.ylabel("Medals")
          plt.title("Overall Standings")

          plt.xticks(ind+width,['US','UK', 'Germany','France', 'Italy'])
          plt.legend( (bar1, bar2, bar3), ('Gold', 'Silver', 'Bronze') )
          plt.show()
          plt.figure()
          print()
          print()
          print("------------------Rest Of The Counties------------------")
          headers=["Country","Gold","Silver","Bronze","Total"]
          df = pd.read_csv("TopCountries.csv")
          df1= df.set_index('ID')
          print(tabulate(df1,headers,tablefmt="pretty"))
          menu()
          
      if choice1 == 2:
          beep()
          print("____________________")
          print("")
          print("")
          print('------------------------')  
          print('| Graph Of Top Players |')
          print('------------------------')  
          N = 5
          ind = np.arange(N)
          width = 0.1

          xvals = [13,9,8,7,8]
          bar1 = plt.bar(ind, xvals, width, color = 'gold')

          yvals = [3,5,4,5,4]
          bar2 = plt.bar(ind+width, yvals, width, color='silver')

          zvals = [2,4,3,1,0]
          bar3 = plt.bar(ind+width*2, zvals, width, color = 'brown')

          plt.xlabel("Players")
          plt.ylabel("Medals")
          plt.title("Overall Standings")
          plt.xticks(ind+width,['MichaelPhelps','LarisaLatynina', 'MaritBjÃ','NikolaiAndrianov', 'PaavoNurmi'])
          plt.legend( (bar1, bar2, bar3), ('Gold', 'Silver', 'Bronze') )
          plt.show()
          print()
          print()
          print("------------------------------------------------Rest Of The Players-------------------------------------------------")
          headers=["Athlete","Nation","Sport","Gender","Gold","Silver","Bronze","Total"]
          df = pd.read_csv("TopPlayers.csv")
          df1= df.set_index('ID')
          print(tabulate(df1,headers,tablefmt="pretty"))
          menu()
     
          
      if choice1 == 3:
          beep()
          print("____________________")
          print("")
          print("")
          print('------------------------------------------')  
          print('| Graph Of No Of Countries Participating | ')
          print('------------------------------------------')  
          N = 29
          ind = np.arange(N)
          width = 0.1

          xvals = [1896,1900,1904,1908,1912,1920,1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2021]
          

          yvals = [14,24,12,22,28,29,44,46,37,49,59,69,72,83,93,112,121,92,80,140,159,169,197,199,201,201,204,207,206]
         
          
          plt.xlabel("Years")
          plt.ylabel("Total No Of Countries")
          plt.bar(xvals,yvals)
          plt.show()
          print()
          print()
          print("---Data Over The Years---")
          headers=["Years","Numbers"]
          df = pd.read_csv("PartiCountries.csv")
          df1= df.set_index('ID')
          print(tabulate(df1,headers,tablefmt="pretty"))
          menu()
          
      if choice1 == 4:
           beep()
           print("____________________")
           print("")
           print("")
           print('                                           --------------------')  
           print( '                                           | Data Categorized | ')
           print('                                           --------------------') 
           print("")
           headers=["Event","Record","Athlete(s)","Nation","Games","Date"]
           df = pd.read_csv("Mens Record.csv")
           df1= df.set_index('ID')
           print(tabulate(df1,headers,tablefmt="pretty")) 
           menu()
           
      if choice1 == 5:
           beep()
           print("____________________")
           print("")
           print("")
           print('                                           --------------------')  
           print( '                                           | Data Categorized | ')
           print('                                           --------------------')  
           print("")
           headers=["Event","Record","Athlete(s)","Nation","Games","Date"]
           df = pd.read_csv("Womens Record.csv")
           df1= df.set_index('ID')
           print(tabulate(df1,headers,tablefmt='pretty'))    
           menu()
      
            
      if choice1 == 6:
           beep()
           print("____________________")
           print("")
           print("")
           print('                                           --------------------')  
           print( '                                           | Data Categorized | ')
           print('                                           --------------------') 
           print("")
           headers = ["Event","Olympic Record (Men)","World Record (Men)","Olympic Record (Women)","World Record (Women)"]
           df = pd.read_csv("Olympic Record vs World.csv")
           df1= df.set_index('ID')
           print(tabulate(df1,headers, tablefmt='pretty'))       
           menu()
        
      

      if choice1 == 7: 
          beep()
          mainmenu()
        
      if choice1  > 7:  
          print("")  
          beep1()
          print("Invalid Input Enter A Valid Number")
          menu()
       


#######################################################################################################
    if choice == 3:
        print("")
        beep()
        print('-------------------------------------------------------------------------')  
        print('| Here Is the Some Prediction Based on the Past Record Of The Countries | ')
        print('-------------------------------------------------------------------------')  
        print("")
        headers=["Rank","Nation","Gold","Silver","Bronze","Total"]
        df = pd.read_csv("Prediction.csv")
        df1= df.set_index('Rank')
        print(tabulate(df1,headers,tablefmt="pretty"))
        mainmenu()
        
###############################################################################################################   
    if choice ==4:
        beep()
        import tkinter as tk
        from tkinter import messagebox

        def submit_feedback():
            name = entry_name.get()
            email = entry_email.get()
            feedback = text_feedback.get("1.0", "end-1c")

            messagebox.showinfo("Feedback Received", f"Name: {name}\nEmail: {email}\nFeedback: {feedback}")

            

            
            entry_name.delete(0, "end")
            entry_email.delete(0, "end")
            text_feedback.delete("1.0", "end")
            root.destroy()
            
        root = tk.Tk()
        root.title("Feedback Form")

        
        label_name = tk.Label(root, text="Name:")
        label_name.grid(row=0, column=0)
        entry_name = tk.Entry(root)
        entry_name.grid(row=0, column=1)

        label_email = tk.Label(root, text="Email:")
        label_email.grid(row=1, column=0)
        entry_email = tk.Entry(root)
        entry_email.grid(row=1, column=1)

        label_feedback = tk.Label(root, text="Feedback:")
        label_feedback.grid(row=2, column=0)
        text_feedback = tk.Text(root, width=30, height=10)
        text_feedback.grid(row=2, column=1)

        submit_button = tk.Button(root, text="Submit", command=submit_feedback)
        submit_button.grid(row=3, column=0, columnspan=2)

        root.mainloop()
        print("")
        print("")
        print('----------------------------------------')
        print("| Thank You For Your Valuable Feedback |")
        print('----------------------------------------')
        print("")
        print("")
        print("------------------------------------------------------------------------")
        print("| We All Need People Who Will Give Us Feedback. That’s How We Improve. | ")   
        print("------------------------------------------------------------------------")
    
    
    if choice  >= 5: 
      print("")  
      print("Invalid Input Enter A Valid Number")
      beep1()
      mainmenu()
      
      
















