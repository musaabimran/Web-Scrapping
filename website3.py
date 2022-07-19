from header import *

third_website = ["https://lums.edu.pk/","https://admission.lums.edu.pk/","https://lums.edu.pk/news","https://lums.edu.pk/student-noticeboard","https://admission.lums.edu.pk/admission-policy"]
# Calling the function to go and get the web data
############
third_website_text = [] # Contains the content of the website 
third_website_nouns = [] # Contains the number of nouns in website
third_website_verbs = []  # Contains the verbs of the website
third_website_adj = []  # Contains the adjective of the website
third_website_max_nouns_list = [] # Contains the maximum nouns occurance
third_website_max_verbs_list = [] # Contains the maximum verbs occurance
third_website_max_adjective_list = [] # Contains the maximum adjective occurance
################# Go and show the Graph with Subdomains ################
show_subdomain_graph(third_website_text,third_website_nouns,third_website_verbs,third_website_adj,third_website,third_website_max_nouns_list,third_website_max_verbs_list,third_website_max_adjective_list)
################ Go and count the total number of Parts of speech in doamin ########
third_website_total = []
# 0 index contains the total number of Nouns
# 1 index contains total number of Verbs
# 2 Index contains total number of Ajection
third_website_total.append(count_total(third_website_nouns))
third_website_total.append(count_total(third_website_verbs))
third_website_total.append(count_total(third_website_adj))
################ Show the Final Graph of the Website ###############3
print_graph(third_website_total[1],third_website_total[2],third_website_total[0],"Total For this Domain")

