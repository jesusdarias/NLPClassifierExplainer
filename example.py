# -*- coding: utf-8 -*-
"""
Created on Tue May 17 09:03:55 2022

@author: Bruno Fleisch
"""


from TelecomNotesRecommender.Recommender import Recommender

recommender = Recommender()
recommender.load_model("models/trained_model.pk")


#query = 'New dropfrom eu to carrier pole unable pu t to drop from carrier to dp as it goes over train tracks. An di cant do this safely.'
#query = 'I cannot complete this task because I have run out of timeithin my scheduled hours. The end customer cannot use the srvice. The work outstanding is Track.'
#expl  = recommender.explain (query)

#query = 'I cannot complete this task because Faulty fibre port ( no s pares ) causing noisy line. Waiting on lums case 184241, spo ke to dcoe,expected to be resolved 5/5/18. Please pass to CS S queue Id Na. The line has been proven good to the PCP. Ear th contact was detected towards the end customer.'

query = "I cannot complete this task because of a hazard owned by Openreach / third party. Dp damaged by fire A1024 13416129 manager informed  is preventing further work. "
print (recommender.predict([query]))

print (recommender.predict_proba([query]))

explanation =  recommender.explain (query)