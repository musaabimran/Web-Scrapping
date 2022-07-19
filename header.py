import urllib.request as ur
import time
import numpy as np
from textblob import TextBlob
from bs4 import BeautifulSoup
from matplotlib import pyplot



# A simple Function that takes no. of pos and print the graph for it
def print_graph(count_verbs, count_adj, count_nouns, title):
    pof = ('Verb', 'Ajective', 'Nouns')

    rank = [count_verbs, count_adj, count_nouns]
    explode = (0.2, 0, 0)
    colors = ['yellowgreen', 'pink', 'orange']
    pyplot.title(title)

    pyplot.pie(rank, explode=explode, labels=pof, colors=colors,
               autopct='%1.1f%%', shadow=True, startangle=120)
    pyplot.axis('equal')
    pyplot.show()


def create_a_maximum_lists(pos_list, list_to_be_filled_with_max):
    # A function that takes in a list of POS(Any) and fills a second list with maximum's
    pos_copy = pos_list
    #list_to_be_filled_with_max = []
    # For Counting of each element in the list
    
    for each in range(10):
        max_noun = ""
        max_count = 0
        for noun in pos_copy:
            #print("Count of " + str(noun) + " is " + str(pos_copy.count(noun)))
            # I want you to find the maximum
            count = pos_copy.count(noun)
            if ((count > max_count) and (type(noun) != int) and (len(noun) > 2)):
                if not any(value in noun for value in ("+", ".", "/", "-", "$", "\\", "'", "\"")):
                    #max_count = (str( pos_copy.count(noun)) + "->" + noun)
                    max_noun = noun
                    max_count = count

        # Saving this data into a list
        saved_nouns_inside_list = []
        saved_nouns_inside_list.append(max_noun)
        saved_nouns_inside_list.append(max_count)
        # Now am saving the list into another list
        list_to_be_filled_with_max.append(saved_nouns_inside_list)
        #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        #print(list_to_be_filled_with_max)
        pos_copy = list(filter((max_noun).__ne__, pos_copy))
    return list_to_be_filled_with_max
    # print("######################################################")
   # print(saved_nouns_outside_list)

# Pass this function the blob from the final text and get the count of nouns


def return_noun_count(blob, max_nouns_list):
    nouns = [n for n, t in blob.tags if (
        t == 'NN' or t == 'NNS' or t == 'NNP' or t == 'NNPS')]
    print("Nouns In the Website")
    print(nouns)
    create_a_maximum_lists(nouns, max_nouns_list)

    # For counting the Total Number of Nouns
    count_nouns = 0
    for noun in nouns:
        count_nouns = count_nouns+1
    print("Total Number of Nouns: " + str(count_nouns))
    return int(count_nouns)
# Pass this function the blob from the final text and get the count of verbs


def return_verb_count(blob, max_verbs_list):
    verbs = [n for n, t in blob.tags if (
        t == 'VB' or t == 'VBD' or t == 'VBG' or t == 'VBN' or t == 'VBP' or t == 'VBN' or t == 'VBZ')]
    print("Verbs In the Website")
    print(verbs)
    create_a_maximum_lists(verbs, max_verbs_list)
    count_verbs = 0
    for verb in verbs:
        count_verbs = count_verbs+1
    print("Total Number of Verbs: " + str(count_verbs))
    return int(count_verbs)
# Pass this function the blob from the final text and get the count of adjectives


def return_adj_count(blob, max_adj_list):
    adjectives = [n for n, t in blob.tags if (
        t == 'JJ' or t == 'JJR' or t == 'JJS')]
    print("Adjectives In the Website")
    print(adjectives)
    create_a_maximum_lists(adjectives, max_adj_list)
    count_adj = 0
    for adjective in adjectives:
        count_adj = count_adj+1
    print("Total Number of Adjectives: " + str(count_adj))
    return int(count_adj)

# This is the function that takes a URL and return the Final Text from the website


def return_web_text(ori_url):

    # Open the url and save it
    url = ur.urlopen(ori_url).read()
    soup = BeautifulSoup(url, features="html.parser")

    # Remove all the scripts and style tags
    for script in soup(["script"]):
        script.extract()  # Remove them

    for style in soup(["style"]):
        style.extract()  # Remove them

    # get strings
    strings = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = []
    for line in strings.splitlines():
        lines.append(line.strip())

    # break multi-headlines into a line each

    pieces = []
    for line in lines:
        for phrase in line.split("  "):
            pieces.append(phrase.strip())

    # Remove the empty lines
    text = ' ' . join(chunk for chunk in pieces if chunk)
    print("Scrapted Data from the Website..")
    print(text.encode('utf-8'))
    final_text = text.encode('utf-8')
    return final_text
# This function takes the list and fill them and also shows the graph


def show_subdomain_graph(website_text, website_nouns, website_verbs, website_adj, website, max_nouns_list, max_verb_list, max_adj_list):
    counting = 0
    for final in website:
        # Here we have access to all the website names
        # Call the function to get the text
        website_text.append(return_web_text(final))
        # Adding the text to TextBlob library so we can use blob and identify pos
        blob = TextBlob(str(website_text[counting]))
        # Now we need all the Nouns and verbs of the Sites..

        # We can counting the Total number of Nouns
        website_nouns.append(return_noun_count(blob, max_nouns_list))
        website_verbs.append(return_verb_count(blob, max_verb_list))
        website_adj.append(return_adj_count(blob, max_adj_list))
        print_graph(website_verbs[counting], website_adj[counting],
                    website_nouns[counting], website[counting])
        counting = counting + 1

# This function takes an List and return the sum of total in that list


def count_total(website_data):
    sum = 0
    for total in website_data:
        sum = sum + total
    return sum


#####################################################
## *************** Main Function Calling ********* ##
######################################################

# Run for website 1st
#os.system('py website1.py')
#os.system('py website2.py')
# execfile('file.py')

#os.system('py website3.py')
"""
final_text = []
final_text[0] = return_web_text(ori_url[0])
final_text[1] = return_web_text(ori_url[1])
final_text[2] = return_web_text(ori_url[2])
final_text[3] = return_web_text(ori_url[3])
final_text[4] = return_web_text(ori_url[4]
#Adding the text to TextBlob library so we can use blob and identify pos
blob = TextBlob(str(final_text[0]))
blob = TextBlob(str(final_text[1]))
blob = TextBlob(str(final_text[2]))
blob = TextBlob(str(final_text[3]))
blob = TextBlob(str(final_text[4]))
# print(blob.tags)
# Now finding the Noun
(count_nouns) = return_noun_count(blob)
# Finding the verb 
count_verbs = return_verb_count(blob)
# Finding the Adjective 
count_adj = return_adj_count(blob)
# Now let's Print the Graph
print_graph(count_verbs,count_adj,count_nouns,ori_url)

"""
# References
# https://www.geeksforgeeks.org/python-program-to-check-if-a-word-is-a-noun/
# https://matplotlib.org/
