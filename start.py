#import website1
#import website2
#import website3
import networkx as nx
from website1 import *
from website2 import *
from website3 import *
#Now i need access to the data of the website...
#print (first_website_total[0])
from matplotlib import pyplot
import numpy as np
import matplotlib.pyplot as plt
# first_website_total,second_website_total & third_website_total
# 0 index contains the total number of Nouns
# 1 index contains total number of Verbs
# 2 Index contains total number of Ajection

def Sort_Tuple(tup): 
  
    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using second element of 
    # sublist lambda has been used 
    tup.sort(key = lambda x: x[1], reverse=True) 
    return tup 


#Pass this function 2 list one the filled list and the other to be filled for top 10
def top_10_noun_extrator(filled_list, empty_list_to_be_filled):
    (sorted(filled_list,key=lambda x:x[1], reverse=True))
    count = 0
    for each in filled_list:
        if count == 10:
            break
        else:
            empty_list_to_be_filled.append(each)
            count = count+1
    print(empty_list_to_be_filled)

top_10_from_graph_list = []
def show_final_website_graph(website_text,max_nouns_in_website):
    
    other_list_=[]
    # making the list of the top apperance
    for each in max_nouns_in_website:
        other_list_.append(each[0])
    G = nx.Graph()
    text = str(website_text)
    text=TextBlob(text)
    
    #Looping for Each Sentence!
    for sentence in text.sentences:
        #Check all the Nouns in the Sentence
        nouns = [n for n, t in text.tags if (
            t == 'NN' or t == 'NNS' or t == 'NNP' or t == 'NNPS')]
        #Check for each of the noun
        for index, elem in enumerate(nouns):
            #Getting all the Nouns next & Previous so we can add them
            if (index+1 < len(nouns) and index - 1 >= 0) and (len(elem) > 4):
                #prev_el = str(nouns[index-1])
                if len(nouns[index+1]) > 4 and nouns[index+1] in other_list_:
                    curr_el = str(elem)
                    next_el = str(nouns[index+1])
                    #Making the nodes of th e
                    G.add_node(curr_el)
                    G.add_node(next_el)
                    #Now adding those Nodes together
                    G.add_edge(curr_el,next_el)
        #print(sentence)


    pos=nx.spring_layout(G, k=0.99 ,iterations=20,scale=2)
    nx.draw(G,pos,with_labels=True,node_color='skyblue',font_size = 4)
    print("Number of Connected Componets is:" + str(nx.number_connected_components(G)))

    sorted(G.degree, key=lambda x: x[1], reverse=True)
    d = list(G.degree)
    print("########### TOP APPEARING IN THE GRAPH #########")
    tup=Sort_Tuple(d)
    count=0
    for each in tup:
        if count == 10:
            break
        else:
            print(each)
            count=count+1
    #print(d)
    #print(top_10_from_graph_list)
    plt.show()
def comparison_graph_display(first_pof,second_pof,third_pof,labels):
    X = ["FAST","NUST","LUMS"]
    nouns = [first_pof,second_pof,third_pof]
    X_axis = np.arange(len(X))
    pyplot.bar(X_axis + 0.0, nouns, 0.4, label = labels)
    pyplot.xticks(X_axis, X)
    pyplot.xlabel(labels)
    pyplot.ylabel("Counting")
    pyplot.title("Comparison of Three Websites " + labels)
    pyplot.legend()
    pyplot.show()



comparison_graph_display(first_website_total[0],second_website_total[0],third_website_total[0],"Nouns")
comparison_graph_display(first_website_total[1],second_website_total[1],third_website_total[1],"Verbs")
comparison_graph_display(first_website_total[2],second_website_total[2],third_website_total[2],"Adjective")

# THIS Function takes 3 values and show the Graph with label for comparison
print("---------------------THE MAXIMUM OCCURANCES OF THE FIRST WEBSITE-------------")
print("[+]   Maximum Ocurring  Nouns   [+] ")
print(first_website_max_nouns_list)
print("[+]   Maximum Ocurring  Adjectives   [+] ")
print(first_website_max_adjective_list)
print("[+]   Maximum Ocurring  Verbs   [+] ")
print(first_website_max_verbs_list)


print("------------THE MAXIMUM OCCURANCES OF THE second WEBSITE------------")
print("[+]   Maximum Ocurring  Nouns   [+] ")
print(second_website_max_nouns_list)
print("[+]   Maximum Ocurring  Adjectives   [+] ")
print(second_website_max_adjective_list)
print("[+]   Maximum Ocurring  Verbs   [+] ")
print(second_website_max_verbs_list)

print("----------------THE MAXIMUM OCCURANCES OF THE third WEBSITE-----------------")
print("[+]   Maximum Ocurring  Nouns   [+] ")
print(third_website_max_nouns_list)
print("[+]   Maximum Ocurring  Adjectives   [+] ")
print(third_website_max_adjective_list)
print("[+]   Maximum Ocurring  Verbs   [+] ")
print(third_website_max_verbs_list)


################################
# Displaying for first website
###################33
first_website_top_10_nouns = []
first_website_top_10_verbs = []
first_website_top_10_adjectives = []
top_10_noun_extrator(first_website_max_nouns_list,first_website_top_10_nouns)
top_10_noun_extrator(first_website_max_verbs_list,first_website_top_10_verbs)
top_10_noun_extrator(first_website_max_adjective_list,first_website_top_10_adjectives)
print("\nTOP 10 Nouns of First Website\n")
print(first_website_top_10_nouns)

print("\nTOP 10 Verbs First Website\n")
print(first_website_top_10_verbs)

print("\nTOP 10 Adjectives First Website\n")
print(first_website_top_10_adjectives)

################################
# Displaying for Second website
###################33
second_website_top_10_nouns = []
second_website_top_10_verbs = []
second_website_top_10_adjectives = []
top_10_noun_extrator(second_website_max_nouns_list,second_website_top_10_nouns)
top_10_noun_extrator(second_website_max_verbs_list,second_website_top_10_verbs)
top_10_noun_extrator(second_website_max_adjective_list,second_website_top_10_adjectives)
print("\nTOP 10 Nouns of second Website\n")
print(second_website_top_10_nouns)

print("\nTOP 10 Verbs Second Website\n")
print(second_website_top_10_verbs)

print("\nTOP 10 Adjectives Second Website\n")
print(second_website_top_10_adjectives)

################################
# Displaying for Third website
###################33
third_website_top_10_nouns = []
third_website_top_10_verbs = []
third_website_top_10_adjectives = []
top_10_noun_extrator(third_website_max_nouns_list,third_website_top_10_nouns)
top_10_noun_extrator(third_website_max_verbs_list,third_website_top_10_verbs)
top_10_noun_extrator(third_website_max_adjective_list,third_website_top_10_adjectives)
print("\nTOP 10 Nouns of second Website\n")
print(third_website_top_10_nouns)

print("\nTOP 10 Verbs Second Website\n")
print(third_website_top_10_verbs)

print("\nTOP 10 Adjectives Second Website\n")
print(third_website_top_10_adjectives)


show_final_website_graph(first_website_text,first_website_max_nouns_list)
show_final_website_graph(second_website_text,second_website_max_nouns_list)
show_final_website_graph(third_website_text,third_website_max_nouns_list)
# 0 index contains the total number of Nouns
# 1 index contains total number of Verbs
# 2 Index contains total number of Ajection
