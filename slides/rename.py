import os

import json

filePath = './presentation/'
slideNames = ['BackgroundSlide_CBFs',
              'BackgroundSlide_Genenral',
              'FormalConstruction',
              'FormalConstructionRemarks',
              'FormalProblemStatement',
              'MotivatingIdea_1',
              'MotivatingIdea_2',
              'OutlineSlide_Sims',
              'OutlineSlide_Idea',
              'OutlineSlide_Background',
              'OutlineSlide_FormalConstruction',
              'TitleSlide']

for slideName in slideNames:
  
  # Opening JSON file
  f = open(filePath + slideName + '.json',)
  
  # returns JSON object as
  # a dictionary
  data = json.load(f)

  # Closing file
  f.close()

  for i in range(len(data['files'])):
    old_name = data['files'][i]
    new_name = filePath + "files/" + slideName + "/" + str(i) + ".mp4"

    print("RENAMING: " + old_name + " TO " + new_name)

    os.rename(old_name, new_name)
    data['files'][i] = new_name



  with open(filePath + slideName + '.json', "w") as outfile:
      json.dump(data, outfile)
