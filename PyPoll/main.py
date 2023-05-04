#Import Dependencies
import csv
with open ('PyPoll/election_data.csv') as csvfile:

    csvreader=csv.reader(csvfile, delimiter=',') 
    header=next(csvreader) 

    #variables
    voterids=[] 
    counties=[] 
    candidates=[] 
    candidatenames=[] 
    totaleachcan=[] 
    resultprintcan=[] 
    totaleachcanperc=[] 

    #Start conditions
    line_count=0
    winnervotes=0
    loservotes=0
    loop1=0
    loop2=0
    loop3=0
    loop4=0
    
#Create lists 
    for row in csvreader:
        voterid=row[0] 
        county=row[1] 
        candidate=row[2] 
        voterids.append(voterid) 
        counties.append(county)
        candidates.append(candidate) 
    
 #total no of votes in Voter ID
line_count= len(voterids)
    
#analysis

candidatenames.append(candidates[0])

#Loop 1 - list of candidates to determine candidates voted for 
for loop1 in range (line_count-1):
    if candidates[loop1+1] != candidates[loop1] and candidates[loop1+1] not in candidatenames:
        candidatenames.append(candidates[loop1+1])

n=len(candidatenames)


#Loop 2 - loop index counter
for loop2 in range (n): 
    totaleachcan.append(candidates.count(candidatenames[loop2])) 



#Third loop variable loop3 as loop index counter

loservotes=line_count 

#Loop 3 -how many candidates were found
for loop3 in range(n):
    totaleachcanperc.append(f'{round((totaleachcan[loop3]/line_count*100), 4)}%') 
    
#Highest vote count    
    if totaleachcan[loop3]>winnervotes: 
        winner=candidatenames[loop3]
        winnervotes=totaleachcan[loop3]
#Lowest vote count
    if totaleachcan[loop3]<loservotes: 
        loser=candidatenames[loop3]
        loservotes=totaleachcan[loop3]

#Loop 4 -
for loop4 in range(n):
    resultprintcan.append(f'{candidatenames[loop4]}: {totaleachcanperc[loop4]} ({totaleachcan[loop4]})') 

resultlines='\n'.join(resultprintcan)

#analysis

analysis=f'\
Election Results\n\
----------------------------\n\
Total Votes: {line_count}\n\
----------------------------\n\
{resultlines}\n\
----------------------------\n\
Winner: {winner} :)\n\
Last: {loser} :(\n\
----------------------------\n'

print(analysis)