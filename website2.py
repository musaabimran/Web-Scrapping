from header import *

second_website = ["https://nust.edu.pk/","https://nust.edu.pk/admissions/","https://nust.edu.pk/academics/","https://nio.nust.edu.pk/","https://campuslife.nust.edu.pk/"]
# Calling the function to go and get the web data
############
second_website_text = [] # Contains the content of the website 
second_website_nouns = [] # Contains the number of nouns in website
second_website_verbs = []  # Contains the verbs of the website
second_website_adj = []  # Contains the adjective of the website
second_website_max_nouns_list = [] # Contains the maximum nouns occurance
second_website_max_verbs_list = [] # Contains the maximum verbs occurance
second_website_max_adjective_list = [] # Contains the maximum adjective occurance
################# Go and show the Graph with Subdomains ################
show_subdomain_graph(second_website_text,second_website_nouns,second_website_verbs,second_website_adj,second_website,second_website_max_nouns_list,second_website_max_verbs_list,second_website_max_adjective_list)
################ Go and count the total number of Parts of speech in doamin ########
second_website_total = []
# 0 index contains the total number of Nouns
# 1 index contains total number of Verbs
# 2 Index contains total number of Ajection
second_website_total.append(count_total(second_website_nouns))
second_website_total.append(count_total(second_website_verbs))
second_website_total.append(count_total(second_website_adj))
################ Show the Final Graph of the Website ###############3
print_graph(second_website_total[1],second_website_total[2],second_website_total[0],"Total For this Domain")

