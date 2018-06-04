import numpy as np 

doors=np.array([[1,0,0],[0,1,0],[0,0,1]]) #all door configs (these were hard-coded in since there are only 3C2=3 of them)
montyschoice=np.array([[1,2],[0,2],[0,1]]) #the doors available for Monty to open 
tallywin=0 #wins if not switching
tallyloss=0 #losses if not switching

for i in range(100000):
  montyssetup=np.random.randint(3) #monty chooses a door configuration
  doorconfig=doors[montyssetup,:]

  contestantchoice=np.random.randint(3) #contestant chooses a door

  index=np.random.randint(2) #monty chooses a door to open
  montyopensdoor=montyschoice[montyssetup,index]
  if montyopensdoor==contestantchoice: #condition in case the door is the same as the contestant's
    montyopensdoor=montyschoice[montyssetup,(index+1)%2]
  if doorconfig[contestantchoice]==1:
    tallywin+=1 #win tally
  else:
    tallyloss+=1 #loss tally
  print("win: {} loss: {}".format(round(tallywin/(tallyloss+tallywin),5),round(tallyloss/(tallyloss+tallywin),5)))
  
  #running this one would get ~60% of the games as losses. i.e. the contestant should always switch if given the choice since it
  #has double the probability of winning
