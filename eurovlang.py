
import pandas as pd
import matplotlib.pyplot as plt


# read in the csv file with the language data

df = pd.read_csv('contestants_wlang.csv')
dforig =df 
## print(df)

# calculate how many times a language appears in the dataframe

df['lang_count'] = df.groupby('Language')['Language'].transform('count')


# create new dataframe with last columns

df2 = df[['Language', 'lang_count']]

# show only unique languages, sort by lang_count

df2 = df2.drop_duplicates().sort_values(by='lang_count', ascending=False)

# take top 10 languages

df2.head(10)

# add row numbers to dataframe 

df2.reset_index(inplace=True)

# remove index column

df2.drop('index', axis=1, inplace=True)


# print top 15 from the dataframe.

print(df2.head(15))

# print total number of languages

print("Total languages")
print(df2['Language'].count())


# calculate how many times a language appears in the dataframe in each year

print("LANG count per year")
dforig['lang_count_by_year'] = dforig.groupby(['year', 'Language'])['Language'].transform('count')


langs_per_year = dforig[['year', 'Language', 'lang_count_by_year']] #.drop_duplicates()

print("----------------------")
print(langs_per_year)


# plot the data

# print year 1956
# print(langs_per_year[langs_per_year['year'] == 1956].drop_duplicates())

lpy = langs_per_year.drop_duplicates()



df3 = lpy.pivot(columns='Language', index='year')


# convert missing values  to zeroes
df3 = df3.fillna(0)
df3a = df3 

##df3a.plot(kind='area',figsize=(10,10))
##plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")
# save graph to file
##plt.savefig('lang_count_by_year_all.png')
##plt.show()

#print(df3)

# take data frame columns en fr and fi

# dataframe select columns from another dataframe

tmp1 = df2.head(15)['Language']
print(tmp1)


df4 = df3['lang_count_by_year'].filter(tmp1, axis=1)
print(df4)

# dataframe stacked are legend position and size
#df4.xlabel('vuosi')

# change dataframe axis label
#df4.axes('x').set_label('vuosi')

import seaborn as sns

pal = ["#9b59b6", "#e74c3c", "#34495e", "#2ecc71"]

pal = sns.color_palette("colorblind") + sns.color_palette("pastel")


df4.plot(kind='area',  stacked=True, legend=True, fontsize=10, figsize=(10,10), color=pal)

##plt.stackplot(x,y, labels=['A','B','C'], colors=pal, alpha=0.4 )

# save graph to file

plt.xlabel('vuosi')
plt.legend(loc="upper left", bbox_to_anchor=[0, 1],
           ncol=2, title="Esityskieli", fancybox=True)

plt.savefig('lang_count_by_year_top15.png')

plt.show()





print("----------------------")


# plot stackplot 

#langs_per_year.stackplot( x='year', y='lang_count_by_year', stacked=True)

english = langs_per_year[langs_per_year['Language'] == 'en']




print(dforig['year'].drop_duplicates())

#print(english)

french = langs_per_year[langs_per_year['Language'] == 'fr']
finnish = langs_per_year[langs_per_year['Language'] == 'fi']
print(finnish.tail(10))


allyears = pd.Series(data = range(1956, 2020))
fiyears = finnish['year']
fimisyears = allyears[~allyears.isin(fiyears)]

no_finnish_act = pd.DataFrame({'year':fimisyears,'Language':'fi','lang_count_by_year':0})
pdfi = pd.concat([finnish, no_finnish_act])
pdfi.sort_values(by='year', inplace=True)

fryears = french['year']
frmisyears = allyears[~allyears.isin(fryears)]
no_fr_act = pd.DataFrame({'year':frmisyears,'Language':'fr','lang_count_by_year':0})

#print("No french act?")
#print(no_fr_act)

pdfr = pd.concat([french, no_fr_act])
pdfr.sort_values(by='year', inplace=True)



plt.plot(english['year'], english['lang_count_by_year'], label='englanti')
plt.plot(pdfr['year'], pdfr['lang_count_by_year'], label='ranska')
plt.plot(pdfi['year'], pdfi['lang_count_by_year'], label='suomi')

#plt.stackplot(english, french, finnish, labels=['A','B','C'])
plt.legend(loc="upper left", bbox_to_anchor=[0, 1], ncol=2, title="Esityskieli", fancybox=True)
plt.xlabel('vuosi')
plt.show()

#img.imshow()





