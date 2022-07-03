import pandas as pd

# congress twitter handles from here: https://triagecancer.org/congressional-social-media
twitters = pd.read_csv("congress_twitters.csv")
twitters.dropna(how="any", inplace=True)
twitters['username'] = [str(handle)[1:] for handle in twitters['handle']]

# filter for republicans
user_names = list(twitters.loc[twitters['party'] == 'R']['username'].values)

# append babylon 5 twitter
user_names.append('B5News')
# append JMS twitter
user_names.append('straczynski')
