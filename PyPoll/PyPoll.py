#!/usr/bin/env python
# coding: utf-8

# In[16]:


#PyPoll
#output should be Election Results
  #-------------------------
  #Total Votes: 3521001
  #-------------------------
  #Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
  #-------------------------
 # Winner: Khan

# Dependencies used
import csv
import os

#Files to load and output
file_to_load = os.path.join("election_data.csv")
file_to_output = os.path.join("election_analysis.txt")

#data parameters

total_votes = 0
candidates = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

#read the csv - convert to dictionaries
with open (file_to_load) as election_data:
    reader = csv.reader(election_data)
    
    header = next(reader)
    #print(header)
    #extract first row to avoid appending to net_change_list
    
    for row in reader:
        #total vote count
        total_votes = total_votes + 1
        
        #extract candidate name from each row
        candidate_name = row[2]
        
        #if candidate does not match any other candidate
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            
            #track candidate votes
            candidate_votes[candidate_name] = 0
            
            
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        
with open (file_to_output,"w") as txt_file:
    
    election_results = (
        
        f"\n Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    
     )
    print(election_results, end ="")
    
    #saving final vote count to text file
    txt_file.write(election_results)
    
    #Determine the winnder
    for candidate in candidate_votes:
        
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) *100
        
        if (votes >winning_count):
            winning_count = votes
            winning_candidate = candidate
            
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        
        print(voter_output, end ="")
        
        txt_file.write(voter_output)
        
    winning_candidate_summary = (
        
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )    
    print(winning_candidate_summary)
    
    txt_file.write(winning_candidate_summary)
    

    
    


# In[ ]:





# In[ ]:




