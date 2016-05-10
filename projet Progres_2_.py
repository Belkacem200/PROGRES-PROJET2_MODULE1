
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 15:28:54 2016

@author: 3410607
"""
from Tkinter import * #POUR L'interface graphique
import tkFileDialog #POUR l'ouverture d'un fichier
import tkMessageBox #POUR un messageboxe pour quitter le programme
import sys
from socket import inet_aton, inet_ntoa
import matplotlib.pyplot as plt #POUR l'affichage des graphes
import re #regular expr





#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________#-----------#____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________|  PARTIE I |_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________#-----------#__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
def partie1():

    noeuds_set = set()
    connections_noeud = []
    # function for parsing the data
    def data_parser(text):
        p1 = re.compile( r"[ \t]*"
                         r"\n"
                         r"$")

        p2 = re.compile( r"[ \t]*"
                         r"([a-z]+[0-9]*)"   #Routeur1
                         r"[ \t]*"
                         r"([a-z]+[0-9]*)"   #Routeur2
                         r"[ \t]*"
                         r"([0-9]+)"         #Datarate in Kbps
                         r"[ \t]*"
                         r"([0-9]+)"         #Delay in ms
                         r"[ \t]*"
                         r"\n?"
                         r"$",
                         re.IGNORECASE)

        for i in text:
            m = p1.match(i)
            if m:
                continue
            m = p2.match(i)
            if m:
                noeuds_set.add(m.group(1) + " : Source {}")
                noeuds_set.add(m.group(2) + " : Source {}")
                connections_noeud.append(m.group(1) + ".out --> {datarate = " + m.group(3) + "kbps; delay = " + m.group(4) + "ms;} --> " + m.group(2) + ".in;")
            else:
                return False

        return True

    # open input/output files

    inputfile = open('mon_fichier.txt')
    outputfile = open('workfile.ned', 'w')


    my_text = inputfile.readlines()


    b = data_parser(my_text)

    if b:
        outputfile.write("simple Source\n{\n\tgates:\n\t\toutput out;\n\t\tinput in;\n}")
        outputfile.write("\nnetwork Reseau\n{\n\tsubmodules : \n")

        for n in noeuds_set:
            outputfile.write("\t\t" + n + "\n")

        outputfile.write("\tconnections :\n")

        for c in connections_noeud:
            outputfile.write("\t\t" + c + "\n")

        outputfile.write("}")

    else:
        print("Error: File format incorrect")
    Mess=Tk()
    Mess.geometry("470x130+470+10")
    Mess.title("RESULTAT")
    Mess.config(bg='beige')

    Label(Mess,text= "").pack()
    Label(Mess,text= "LA PARTIE I A ETE EXECUTE AVEC SUCCES",font= ("Helvetica", 8, "bold italic"),fg='red', bg='beige').pack()
    Label(Mess,text= "VOUS TROUVEREZ VOTRE FICHIER (Workfil.ned) Dans votre directory Courant",font= ("Helvetica", 8, "bold italic"),fg='red', bg='beige').pack()
    Label(Mess,text= "", bg='beige').pack()
    btt= Button(Mess,text= "   OK   ",font= ("Helvetica", 10, "bold"),fg='black', bg='grey', command=Mess.destroy).pack()
    Label(Mess,text= "").pack()
    Mess.mainloop(3)

    inputfile.close()
    outputfile.close()




#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________#-----------#____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________| PARTIE II |_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________#-----------#__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


#_______________________________________________________________________________________________________________#|
#|###############################################################################################################|
#|###############################################################################################################|
#|################                               DECLARATION DES FONCTIONS                       ################|
#|################                           ----------------------------------                  ################|
#|###############################################################################################################|
#|###############################################################################################################|


def partie2():

  #----------------------------------------------------------------------------------------------------------------|

    #|#######°°°°°°°°°°°#############################***********############################°°°°°°°°°°°#######|
    #|°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°|
    #|###***###                        FONCTION DE PARSING DES @IP ET MAC                            ###***###|
    #|###***###                        ----------------------------------                            ###***###|
    #|#######°°°°°°°°°°°#############################***********############################°°°°°°°°°°°#######|
    #---------------------------------------------------------------------------------------------------------|
    def ip_mac_parser(file1):  #LES @IPs ET @MAC
        MAC_access_point = []
        IP_access_point = []
        MAC=[]
        IP=[]
        ip_mac_adress = re.compile( r"ns3::ArpHeader "
                         r"\(reply source mac: "
                         r"([^ ]*) " #@MAC source (AP)
                         r"source ipv4: "
                         r"([^ ]*) " #@IP source
                         r"dest mac: "
                         r"([^ ]*) " #@MAC dest (AP)
                         r"dest ipv4: "
                         r"(.*)\) " #@IP dest
                         ,re.IGNORECASE)
        for i in file1:
            a = ip_mac_adress.search(i)
            if not a:
                continue
            if(a.group(1)):
                MAC_access_point.append(a.group(1)) #@MAC de l'AP
            if(a.group(2)):
                IP_access_point.append(a.group(2)) #@ip source
            if(a.group(3)):
                MAC.append(a.group(3)) #@MAC dest
            if(a.group(3)):
                IP.append(a.group(4)) #@ip dest
        print("          _________________PARSING DONE_________________")
        print("")
        return IP, MAC, IP_access_point, MAC_access_point

    #|#######°°°°°°°°°°°#############################***********############################°°°°°°°°°°°#######|
    #|°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°|
    #|###***###                           FONCTION De SUPPRESSION DE DOUBLONS D'@ IP/MAC              ###**###|
    #|###***###                                 ----------------------------------                   ###***###|
    #|#######°°°°°°°°°°°#############################***********############################°°°°°°°°°°°#######|
    #|--------------------------------------------------------------------------------------------------------|

    def remove_duplicates(list, idfun=None):
       if idfun is None:
           def idfun(x): return x
       seen = {}
       result = []
       for item in list:
           marker = idfun(item)
           if marker in seen: continue
           seen[marker] = 1
           result.append(item)
       return result

    #|#######°°°°°°°°°°°#############################***********############################°°°°°°°°°°°#######|
    #|°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°|
    #|###***###                              FONCTION RELEVANT LA TAILLE DES PATQUETS                ###***###|
    #|###***###                                  ----------------------------------                  ###***###|
    #|#######°°°°°°°°°°°#############################***********############################°°°°°°°°°°°#######|
    #---------------------------------------------------------------------------------------------------------|

    def taille_paquet(file1): #TAILLE PAQUETS
        taille_paq = re.compile( r"ns3::UdpHeader \(length: "
                        r"([^ ]*) ",re.IGNORECASE)
        for i in file1:
            a = taille_paq.search(i)
            if not a:
                continue
            if(a.group(1)):
                paq=str(a.group(1))
                break
        return paq

    #|#######°°°°°°°°°°°#############################***********############################°°°°°°°°°°°#######|
    #|°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°|
    #|###***###                              FONCTION RELEVANT LA TAILLE DES PATQUETS UTILE          ###***###|
    #|###***###                                      ----------------------------------              ###***###|
    #|#######°°°°°°°°°°°#############################***********############################°°°°°°°°°°°#######|
    #---------------------------------------------------------------------------------------------------------|

    def taille_paquet_utile(file1):  #TAILLE PAQUETS UTILE
        paq=""
        taille_paq_ut = re.compile( r"Payload \(size="
                        r"([0-9]*)\) "
                        ,re.IGNORECASE)
        for i in file1:
            a = taille_paq_ut.search(i)
            if not a:
                continue
            if(a.group(1)):
                paq=str(a.group(1))
                break #Il nous suffit de trouver une fois la taille des paquets et on sort de la boucle
        return paq #taille des paquets

    #|#######°°°°°°°°°°°#############################***********############################°°°°°°°°°°°#######|
    #|°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°|
    #|###***###                                     FONCTION RELEVANT LE DEBIT                       ###***###|
    #|###***###                                  ----------------------------------                  ###***###|
    #|#######°°°°°°°°°°°#############################***********############################°°°°°°°°°°°#######|
    #---------------------------------------------------------------------------------------------------------|

    def debit(file1, ip_address):  #TAILLE PAQUETS UTILE
        time = 1.0
        taille_paquets = 0
        ENS_TEMPS =[]
        DEBIT= []
        reg_exp = re.compile( r"^[rt] "
                        r"([^ ]*) " #POUR le temps t1
                        r".* length: ([^ ]*) " #Pour la longueur (sera utilisé pour le calcul du débit)
                        r"([^ ]*) " #L'@ip src
                        ,re.IGNORECASE)
        for i in file1:
            ip_time_longueur = reg_exp.match(i) #Variable des groupes du REGEX
            if not ip_time_longueur: #ON BOUCLE JUSQU'A CE QU'ON TROUVE L'expr reguliere
                continue
            if ip_time_longueur.group(3) == ip_address: #si ça match l'@ ip
                if (float(ip_time_longueur.group(1))<=time):
                    taille_paquets+=float(ip_time_longueur.group(2))+36
                    continue
                ENS_TEMPS.append(time)  #ENSEMBLE TEMPS
                DEBIT.append(taille_paquets/(1024*1024)) #ENSEMBLE DEBIT UTIL
                time+=1
                taille_paquets=float(ip_time_longueur.group(2))+36
        ENS_TEMPS.append(time)  #ENSEMBLE TEMPS
        DEBIT.append(taille_paquets/(1024*1024)) #ENSEMBLE DEBIT UTIL
        return ENS_TEMPS, DEBIT

    #|#######°°°°°°°°°°°#############################***********############################°°°°°°°°°°°#######|
    #|°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°|
    #|###***###                            FONCTION RELEVANT LE DEBIT UTILE                          ###***###|
    #|###***###                           ----------------------------------                         ###***###|
    #|#######°°°°°°°°°°°#############################***********############################°°°°°°°°°°°#######|
    #---------------------------------------------------------------------------------------------------------|

    def debit_util(file1, ip_address):  #TAILLE PAQUETS UTILE
        time = 1.0
        taille_paquets = 0
        ENS_TEMPS_util =[]
        DEBIT_UTIL =[]
        reg_exp = re.compile( r"^[rt] "
                        r"([^ ]*)" #POUR le temps t1 _________________________1
                        r".* Retry=([0-9]*)," #Pour verifier les retry _________2
                        r".* length: [^ ]* "
                        r"([^ ]*)" #L'@ip src__________________________________3
                        r".* Payload \(size=([^)]*)\) "#Taille utile_________4
                        ,re.IGNORECASE)
        for i in file1:
            ip_time_longueur = reg_exp.match(i) #Variable des groupes du REGEX
            if not ip_time_longueur: #ON BOUCLE JUSQU'A CE QU'ON TROUVE L'expr reguliere
                continue
            if ip_address==ip_time_longueur.group(3):  #si ça match l'@ ip
                if (float(ip_time_longueur.group(1))<=time):
                    taille_paquets+=float(ip_time_longueur.group(4))
                    continue
                ENS_TEMPS_util.append(time)  #ENSEMBLE TEMPS
                DEBIT_UTIL.append(taille_paquets/(1024*1024)) #ENSEMBLE DEBIT UTIL
                time+=1
                taille_paquets=float(ip_time_longueur.group(4))
        ENS_TEMPS_util.append(time)  #ENSEMBLE TEMPS
        DEBIT_UTIL.append(taille_paquets/(1024*1024)) #ENSEMBLE DEBIT UTIL
        return  ENS_TEMPS_util,DEBIT_UTIL

    #|#######°°°°°°°°°°°#############################***********############################°°°°°°°°°°°#######|
    #|°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°|
    #|###***###                           FONCTION RELEVANT LE DEBIT UTILE CUMULE                    ###***###|
    #|###***###                             ----------------------------------                       ###***###|
    #|#######°°°°°°°°°°°#############################***********############################°°°°°°°°°°°#######|
    #---------------------------------------------------------------------------------------------------------|

    def debit_util_cumulatif(file1, ip_address):  #TAILLE PAQUETS UTILE
        time = 1.0
        taille_paquets = 0
        ENS_TEMPS_util =[]
        DEBIT_UTIL_cumul=[]
        reg_exp = re.compile( r"^[rt] "
                        r"([^ ]*)" #POUR le temps t1 _________________________1
                        r".* Retry=([01])," #Pour verifier les retry _________2
                        r".* length: [^ ]* [^ ]* > ([^\)]*)\)" #L'@ip dst_____3
                        r".* Payload \(size=([0-9]*)\) "#Taille utile_________4
                        ,re.IGNORECASE)
        for i in file1:
            ip_time_longueur = reg_exp.match(i) #Variable des groupes du REGEX
            if not ip_time_longueur: #ON BOUCLE JUSQU'A CE QU'ON TROUVE L'expr reguliere
                continue
            if ip_address==ip_time_longueur.group(3):  #si ça match l'@ ip
                if (float(ip_time_longueur.group(1))<=time):
                    taille_paquets+=float(ip_time_longueur.group(4))
                    continue
                ENS_TEMPS_util.append(time)  #ENSEMBLE TEMPS
                DEBIT_UTIL_cumul.append(taille_paquets/(1024*1024)) #ENSEMBLE DEBIT UTIL
                time+=1
                taille_paquets=float(ip_time_longueur.group(4))
        ENS_TEMPS_util.append(time)  #ENSEMBLE TEMPS
        DEBIT_UTIL_cumul.append(taille_paquets/(1024*1024)) #ENSEMBLE DEBIT UTIL
        return  ENS_TEMPS_util,DEBIT_UTIL_cumul

    #|#######°°°°°°°°°°°#############################***********############################°°°°°°°°°°°#######|
    #|°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°|
    #|###***###                    FONCTION Du NOMBRE DE COLLISION AU FIL DU TEMPS                   ###***###|
    #|###***###                             ----------------------------------                       ###***###|
    #|#######°°°°°°°°°°°#############################***********############################°°°°°°°°°°°#######|
    #---------------------------------------------------------------------------------------------------------|

    def collisions(file1, ip_address):  #TAILLE PAQUETS UTILE
        c=0
        time=1.0
        ENS_TEMPS_colision = []
        COLLISION =[]
        reg_exp = re.compile( r"^[rt] "
                        r"([^ ]*)" #POUR le temps t1 _________________________1
                        r".* Retry=([01])," #Pour verifier les retry _________2
                        r".* length: [^ ]* "
                        r"([^ ]*)" #L'@ip src__________________________________3
                        ,re.IGNORECASE)
        for i in file1:
            ip_time_longueur = reg_exp.match(i) #Variable des groupes du REGEX
            if not ip_time_longueur: #ON BOUCLE JUSQU'A CE QU'ON TROUVE L'expr reguliere
                continue
            if ip_address==ip_time_longueur.group(3):  #si ça match l'@ ip
                if ip_time_longueur.group(2) == '1': #SI nous avons un RETRY on ignore et on reboucle
                    if (float(ip_time_longueur.group(1))<=time):
                        #temps = float(ip_time_longueur.group(1)) #x= Le temps (utilisée dans le graphe (débit par rapport au temps))
                        c+=1                  #incrémentation des
                        continue
                    ENS_TEMPS_colision.append(time) #ENSEMBLE DES TEMPS
                    COLLISION.append(c) #ENSEMBLE DES COLLISIONS
                    time+=1
        ENS_TEMPS_colision.append(time) #ENSEMBLE DES TEMPS
        COLLISION.append(c) #ENSEMBLE DES COLLISIONS
        #print(temps, " ", c) #affichage évolution du débit par rapport au temps
        return ENS_TEMPS_colision, COLLISION

    #|#######°°°°°°°°°°°#############################***********############################°°°°°°°°°°°#######|
    #|°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°|
    #|###***###         FONCTION LE NOMBRE D'EVOLUTION DES TRANSMISSION AU FIL DU TEMPS              ###***###|
    #|###***###                                  ----------------------------------                  ###***###|
    #|#######°°°°°°°°°°°#############################***********############################°°°°°°°°°°°#######|
    #---------------------------------------------------------------------------------------------------------|

    def transmissions(file1):  #TAILLE PAQUETS UTILE
        #tr=0.0
        ENS_TEMPS = []
        TRANSMISSION =[]
        #a=1.0
        reg_exp = re.compile( r"^[rt] "
                        r"([^ ]*)" #POUR le temps t1 _________________________1
                        r".* Retry=([01])," #Pour verifier les retry _________2
                        r".* length: [^ ]* "
                        r"([^ ]*) " #L'@ip src__________________________________3
                        r"(>[^\)]*)\) " #L'@ip DST__________________________________4
                        ,re.IGNORECASE)
         
        reg_exp1 = re.compile( r"^[rt] "
                        r"([^ ]*)" #POUR le temps t1 _________________________1
                        r".*CTL_ACK" #Pour verifier les ACK _________2
                        ,re.IGNORECASE)
                        
                        

        for i in file1:
            ip_time_longueur = reg_exp.match(i) #Variable des groupes du REGEX*
            ip_ack = reg_exp1.match(i)
            if not ip_time_longueur:
                if not ip_ack:
                    continue

            if(ip_time_longueur):
                ENS_TEMPS.append(float(ip_time_longueur.group(1)))
                if len(ip_time_longueur.group(3))==9:
                    ip_id=float(ip_time_longueur.group(3)[-2:])
                else:
                    ip_id=float(ip_time_longueur.group(3)[-1:])

            else:
                ENS_TEMPS.append(float(ip_ack.group(1)))
                ip_id=1
            TRANSMISSION.append(ip_id)

        return ENS_TEMPS, TRANSMISSION


    #_______________________________________________________________________________________________________________#|
    #|###############################################################################################################|
    #|###############################################################################################################|
    #|################                                                  FONCTIONS D'APPEL            ################|
    #|################                                              -------------------------------- ################|
    #|###############################################################################################################|
    #|###############################################################################################################|
    #----------------------------------------------------------------------------------------------------------------|

    #taille_paquet(files)                                              #Fonction taille_paquet
    #taille_paquet_utile(files)                                        #Fonction taille_paquet_utile

    #___________________________________________________________________________________________________________________________
    #|°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°|
    #|###***###                                               OUVERTURE DU FICHIER EN LECTURE                               ###***###|
    #|###***###                                                     ----------------------------------                              ###***###|
    #|°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°|

    fenetre= Tk() #INTERFACE GRAPHIQUE
    def ouvrir_fich():
        fich = tkFileDialog.askopenfile(parent=fenetre,initialdir="/Vrac/Progres_proj/",title='CHOISIR UN FICHIER TR')
        files = fich.readlines() #lecture fichier d'entrée
        return files

    def parser_reduce():
        files = ouvrir_fich()
        IP, MAC, IP_access_point, MAC_access_point = ip_mac_parser(files)
        ip_mac_parser(files)                                                            #FONCTION DE PARSING DES @IP/MAC
        IP = remove_duplicates(IP)                                                      #FONCTION DE SUPPRESSION DES DOUBLONS DE LA LISTE DES @IP
        IP_access_point= remove_duplicates(IP_access_point)                             #FONCTION DE SUPPRESSION DES DOUBLONS DE LA LISTE DES @IP DE L'ACCES POINT
        MAC_access_point=remove_duplicates(MAC_access_point)
        MAC = remove_duplicates(MAC)
        a=0
        affichage=Tk()
        affichage.title("@IP et @MAC")
        affichage.geometry("220x320+335+165")
        affichage.config(bg='orange')
        label = Label(affichage, text="", bg='orange').pack()
        label = Label(affichage, text="@IPs et @MACs des PCs",fg='white', bg='red').pack()
        for i in IP:
            label = Label(affichage, text=i+"-->"+MAC[a],fg='black', bg='orange').pack()
            a+=1
        label = Label(affichage, text="", fg='white', bg='orange').pack()
        label = Label(affichage, text="@IP et @MAC de l'access point", fg='white', bg='red').pack()
        label = Label(affichage, text=str(IP_access_point)+"-->"+str(MAC_access_point)+"\n",fg='black', bg='orange').pack()
        return IP,IP_access_point,files

    label = Label(fenetre, text="").pack()
    label = Label(fenetre, text="Fenetre des choix",fg='white', bg='black').pack()
    Label(fenetre,text= "").pack()
    ouvrir = Button(fenetre, text = "@IPs et MACs ",width=15,height=1,command = parser_reduce, bg='orange' ).pack()


    #FONCTION DEBIT
    def exec_debit():
        IP,IP_AP,files=parser_reduce()
        plt.figure('GRAPHE_DE_DEBIT')
        for i in IP:                                                                     #Pour tout @ip dans la liste IP FAIRE
            ENS_TEMPS, DEBIT = debit(files,i) #Fonction debit
            plt.plot(ENS_TEMPS, DEBIT, label="Debit de: "+i)
        ENS_TEMPS_util,DEBIT_UTIL_cumul = debit_util_cumulatif(files,'10.1.3.1')
        plt.plot(ENS_TEMPS_util, DEBIT_UTIL_cumul,color='brown', label="Debit Util Cumulatif: 10.1.3.1")
        plt.legend(loc='best',prop={'size':10})
        plt.xlabel('Temps (s)')
        plt.ylabel('Debit (MB/s)')
        plt.grid(True)
        plt.title('GRAPHE_DE_DEBIT')
        plt.show()
    #___________________________________________________________________________________________________________________________

    #FONCTION DEBIT UTILE
    def exec_debit_utile():
        IP,IP_AP,files=parser_reduce()
        plt.figure('GRAPHE_DE_DEBIT')
        for i in IP:                                                                     #Pour tout @ip dans la liste IP FAIRE
            ENS_TEMPS, DEBIT = debit_util(files,i) #Fonction debit
            plt.plot(ENS_TEMPS, DEBIT, label="Debit utile de: "+i)
        ENS_TEMPS_util,DEBIT_UTIL_cumul = debit_util_cumulatif(files,'10.1.3.1')
        plt.plot(ENS_TEMPS_util, DEBIT_UTIL_cumul,color='brown', label="Debit Util Cumulatif: 10.1.3.1")
        plt.legend(loc='best',prop={'size':10})
        plt.xlabel('Temps (s)')
        plt.ylabel('Debit_utile (MB/s)')
        plt.grid(True)
        plt.title('GRAPHE_DE_DEBIT_UTILE')
        plt.show()
    #___________________________________________________________________________________________________________________________




    #_________________________________________________________________________________________________________________________


    #FONCTION COLLISIONS
    def exec_collisions():
        IP,IP_AP,files=parser_reduce()
        plt.figure('GRAPHE_D_EVOLUTION_DES_COLLISIONS')
        for i in IP:                                                                   #Pour tout @ip dans la liste IP FAIRE
            ENS_TEMPS_colision, COLLISION = collisions(files,i)
            plt.plot(ENS_TEMPS_colision, COLLISION,label="Nb_Cols de: "+i)
        plt.legend(loc='best',prop={'size':10})
        plt.xlabel('Temps (s)')
        plt.ylabel('Nb Collisions (Collisions/s)')
        plt.grid(True)
        plt.title("GRAPHE_D'EVOLUTION_DES_COLLISIONS")
        plt.show()



    #___________________________________________________________________________________________________________________________


    #FONCTION D'EVOLUTION DES TRANSMISSIONS

    def exec_transmissions():
        IP,IP_AP,files=parser_reduce()
        plt.figure("GRAPHE_D'EVOLUTION_DES_TRANSMISSIONS")
        ENS_TEMPS_, TRANSMISSION_ = transmissions(files)
        plt.plot(ENS_TEMPS_, TRANSMISSION_,"r.", label="Transmissions: ")

        lot = map(inet_aton, IP)
        lot.sort()
        iplist1 = map(inet_ntoa, lot)

        for i in iplist1: #ici j'affiche les annotations et vérifie si j'ai des @ip de longueur 9 ou 8 pour connaitre la taille de la fenetre du graphe
                if len(i)==9:
                    maxim_=i[-2:] #Sera utilisé pour la taille de la fenetre du graphe
                    plt.annotate('   Machine: '+ i ,horizontalalignment='left', xy=(1, float(i[-2:])), xytext=(1, float(i[-2:])-0.4),arrowprops=dict(facecolor='black', shrink=0.05),)
                else:
                    maxim_=i[-1:] #Sera utilisé pour la taille de la fenetre du graphe
                    plt.annotate('   Machine: '+ i ,horizontalalignment='left', xy=(1, float(i[7])), xytext=(1, float(i[7])-0.4),arrowprops=dict(facecolor='black', shrink=0.05),)
        for i in IP_AP: #ACCESS POINT ( cas spécial )
            if i[-2:]:
                plt.annotate('   access point: '+ i , xy=(1, i[7]), xytext=(1, float(i[7])-0.4),arrowprops=dict(facecolor='black', shrink=0.05),)

        plt.ylim(0, (float(maxim_))+1) #C'est à ça que sert le tri
        plt.xlim(1, 1.1)
        plt.legend(loc='best',prop={'size':10})
        plt.xlabel('Temps (s)')
        plt.ylabel('IP machines transmettrices')
        plt.grid(True)
        plt.title("GRAPHE_D'EVOLUTION_DES_TRANSMISSIONS")
        plt.legend(loc='best')
        plt.show()


    def exec_taille_paquet():
        IP,IP_AP,files=parser_reduce()
        paq=taille_paquet(files)
        paqu=Tk()
        paqu.geometry("220x80+335+50")
        paqu.title("Taille des Paquets")
        paqu.config(bg='medium sea green')
        label = Label(paqu, text="", bg='medium sea green').pack()
        label = Label(paqu, text="     Taille des paquets: "+paq+"     ",font='bold', fg='white', bg='medium sea green').pack()
        label = Label(paqu, text="",fg='white', bg='medium sea green').pack()

    def exec_taille_paquet_utile():
        IP,IP_AP,files=parser_reduce()
        paq=taille_paquet_utile(files)
        paqu=Tk()
        paqu.title("Taille des Paquets utile")
        paqu.geometry("220x80+335+50")
        paqu.config(bg='medium sea green')
        label = Label(paqu, text="", bg='medium sea green').pack()
        label = Label(paqu, text="     Taille des paquets: "+paq+"     ",font='bold', fg='white', bg='medium sea green').pack()
        label = Label(paqu, text="",fg='white', bg='medium sea green').pack()


    #Tkinter

    fenetre.geometry("300x345+20+50")
    fenetre.title("FENETRE DE CHOIX")
    fenetre.config(bg='black')
    fenetre.geometry()


    b1 = Button(fenetre, text ="     Taille Paquets    ",width=15,height=1, relief=GROOVE, command=exec_taille_paquet, bg='medium sea green').pack()
    b2 = Button(fenetre, text ="Taille Paquets Utile",width=15,height=1, relief=GROOVE, command=exec_taille_paquet_utile, bg='medium sea green').pack()
    b3 = Button(fenetre, text ="Graphe Collisions ",width=15,height=1, relief=GROOVE, command=exec_collisions, bg='chartreuse').pack()
    b4 = Button(fenetre, text ="Graphe Des Trans ",width=15,height=1, relief=GROOVE, command=exec_transmissions, bg='chartreuse').pack()
    b5 = Button(fenetre, text ="Graphe Débit",width=15,height=1, relief=GROOVE, command= exec_debit, bg='chartreuse').pack()
    b6 = Button(fenetre, text ="Graphe Débit Utile",width=15,height=1, relief=GROOVE, command= exec_debit_utile, bg='chartreuse').pack()
    b7 = Button(fenetre, text ="       QUITTER         ",width=15,height=1, relief=GROOVE, command=quitter_prog,fg='white', bg='red').pack()
    Label(fenetre,text= "").pack()
    label = Label(fenetre, text="Projet PROGRES",fg='white', bg='black').pack()
    Label(fenetre,text= "").pack()

    fenetre.mainloop()

    #file.close()

    print("        ")
    print("*****__________________________THE END_________________________*****")  #UNE LIGNE INDIQUANT LA FIN DE L'EXECUTION



def quitter_prog(): #FONCTION POUR QUITTER LE PROGRAMME
        result = tkMessageBox.askquestion("Quitter Le projet PROGRES", "Voulez-vous vraiment quitter le programme?", icon='warning')
        if result=='yes':
            sys.exit(0)

Choix_partie=Tk()
Choix_partie.geometry("300x345+560+180")
Choix_partie.title("FENETRE DE CHOIX DES PARTIES")
Choix_partie.config(bg='black')

Label(Choix_partie,text= "").pack()
Label(Choix_partie,text= "Veillez Choisir la partie à executer executer",font= ("Helvetica", 8, "bold italic"),fg='red', bg='black').pack()
Label(Choix_partie,text= "").pack()

Label(Choix_partie,text= "").pack()
Label(Choix_partie,text= "KAID Belkacem",fg='white', bg='black').pack()
Label(Choix_partie,text= "").pack()
b1 = Button(Choix_partie, text ="     PARTIE I    ",width=15,height=1, relief=GROOVE, command=partie1, bg='wheat').pack()
b2 = Button(Choix_partie, text ="     PARTIE II   ",width=15,height=1, relief=GROOVE, command=partie2, bg='wheat').pack()
b6 = Button(Choix_partie, text ="       QUITTER         ",width=15,height=1, relief=GROOVE, command=quitter_prog,fg='white', bg='red').pack()
Label(Choix_partie,text= "").pack()
label = Label(Choix_partie, text="Projet PROGRES",fg='white', bg='black').pack()
Label(Choix_partie,text= "").pack()

Choix_partie.mainloop()

