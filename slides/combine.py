from moviepy.editor import VideoFileClip, concatenate_videoclips
import json 

import os

import glob

# targetPattern = r"./presentation/*.json"
# res = glob.glob(targetPattern)
# print(res)


filePath = './presentation/'
# slideNames = ['TitleSlide']

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


  s_counter = 0
  for s in data['slides']:

    l = [s['start_animation']]
    if l[-1] != s['number']:
      l.append(s['number'])
    if l[-1] != s['end_animation']:
      l.append(s['end_animation'])

    print("combining " + str(l))
    
    videoNames = [filePath + "files/" + slideName + '/' +  str(s) + ".mp4" for s in l]

    videos = [VideoFileClip(s) for s in videoNames]

    final_video = concatenate_videoclips(videos)

    final_video.write_videofile(filePath + "files/" + slideName + '/frame_' + str(s_counter) + ".mp4")

    s_counter += 1

    # start = filePath + "files/" + slideNames + "['start_animation']
