import re
import yaml



def get(path):
    test_value=path[0]
    print(test_value)
    #print(dictionnaire[test_value]) #cette étape ne fonctionne pas, pourquoi pas comme dico

"""def compare(cont_end,cont_beg)
    intersection = cont_end.intersection(cont_beg)
    if intersection != null :
        return intersection"""

def count_context(dictionnaire):
    n_context=len(yourdict)
    return n_context
##################################################################  LES SPLITS ICI
#string récupérée depuis clé dictionnaire, un contexte
string_travail="{u't-': u'^(.*[fs][iyEe92a])t$'}"
def split_trans_cont(string):
    transformation,contexte=string.split(":")
    return transformation, contexte


#split char à char sur transfo et set à set sur contexte ?  

def split(a):
    liste_trans=list(transfor)
    for i in range (len(liste_trans)):
        if liste_trans[i]=='-' :
            pre_trans=liste_trans[0:i]
            post_trans=liste_trans[i+1:len(liste_trans)]
            print(pre_trans)
            print(post_trans)
            return pre_trans,post_trans


"""        
def apply_trans(transformation, contexte):
    
    

"""
##############################################
def main() :
    #ouverture table yaml
    stream = open('ca.yaml', 'r')
    yaml.dump(yaml.load(stream))
    dictionnaire=stream
    
    #chemin à parcourir
    path=[(u'ii1P', u'pP'), (u'pP', u'is1S'), (u'is1S', u'ii1S'), (u'ii1S', u'ppMP'), (u'ppMP', u'ii1P')]
    print(path[0]) #erreur en 'none'
    #begin
    
    #pathing
    """
    get(path)
    if n_context == 1 :                     #nécessité de considérer différement les
        split(contexte)                     #cas où on a plusieurs contextes pour pouvoir les enregistrer ensemble
        liste_result.append(compare(cont_end,cont_beg))
    elif n_context > 1 :
        context_step_n
        for i in range len(context_step_n):
            split(contexte)
            result_step_n.append(compare(cont_end,cont_beg))
        liste_result.append(result_step_n)
        
    return list
    """
    #split and compare
    
    #end

########################################

if __name__ == "__main__":
    win = None 
    main()

#########################################


"""


#itération dictionnaire
for key, value in d.items():
    if isinstance(value, dict):
          for sub_key, sub_value in value.items():
                     print(key,sub_key,sub_value)
     else:
            print(key,value)


with open("fichier.yaml", 'r') as stream:
    try:
        print(yaml.load(stream))
        yaml.load(stream)
        yaml.dump(yaml.load(stream))

    except yaml.YAMLError as exc:
        print(exc)
print(mes_tuples)

def searchStringInYaml(fichier,string):
    with open(filename, 'r') as stream:
        content = yaml.load(stream)
        if string in content:
            print string
            return 1
        else:
            return 0
    stream.close()

stream = file('fichier.yaml', 'r')
dict = yaml.load(stream)

for key in dict:
    if key in dict == "ai1P":
        print (key), dict[key]
key = 'ai1P'
for key, value in yaml.load(open('fichier.yaml'))[('ai1P', 'ai1S')].iteritems():
    print (key)
    print(value)


y = yaml.load(open("fichier.yaml", "w"))
print(y)


#tentative de set à set
x="(.*[ptkbdgfsSvzZmnJjrwHiyEe926auOoêûâô][ptkbdgfsSvzZmnJjlr])E$"
lx=list(x)
print(lx)
print(len(lx))
liste_organisee=list()
en_tete=list()
liste_organisee.append(en_tete)
for i in range(len(lx)) :
    if i == "[" :
        en_tete.append(i)
        print(en_tete)
def split():
    "variables"
    x="(.*[ptkbdgfsSvzZmnJjrwHiyEe926auOoêûâô][ptkbdgfsSvzZmnJjlr])E$"
    lx=list(x)
    en_tete=list()
    test1=list()
    "==============="
    for i in range(len(lx)) :
       if lx[i]== '(' :
           a1=list()
split()

string_travail="{u't-': u'^(.*[fs][iyEe92a])t$'}"
def split_trans_cont(string):
    transformation, contexte=string.split(":")
    return transformation, contexte
print(split_trans_cont(string_travail))
#print(transformation)
def split_contexte(contexte):
    liste_travail=list(contexte)
    print(liste_travail)


def main():
    string_travail="{u't-': u'^(.*[fs][iyEe92a])t$'}"
    split_trans_cont(string_travail)
    print(split_trans_cont(string_travail))
    print(transformation)
    split_contexte(split_trans_cont(string_travail))"""
