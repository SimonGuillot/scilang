"""string_travail="{u't-': u'^(.*[fs][iyEe92a])t$'}"
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


transfor="u't-'"
transfor2="O.je-o"

def split(a):
    liste_trans=list(transfor)
    for i in range (len(liste_trans)):
        if liste_trans[i]=='-' :
            pre_trans=liste_trans[0:i]
            post_trans=liste_trans[i+1:len(liste_trans)]
            print(pre_trans)
            print(post_trans)
            return pre_trans,post_trans
split(transfor)
#on veut passer de u't à vide ou de O.je à o => check contexte


def opération_sur_contexte(pre_trans,post_trans,contexte):
    string_travail=u'^(.*[fs][iyEe92a])t$'}
    liste_contexte=list.string_travail
    liste_contexte_alignée=list(reversed(liste_contexte))
    pre_trans_alignée=list(reversed(pre_trans))
    post_trans_alignée=list(reversed(post_trans))
    for i in range(len(liste_contexte_alignée)):  #alignement normal du contexte et de cont pré trans mais post ?
        for i in range(len(pre_trans_alignée)):
            for j in range(len(post_trans_alignée)):
                
        
    
