import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel 

movies_data = pd.read_excel("Nlp with images.xlsx")

indexed = pd.Series(data= movies_data.index ,index=movies_data["Movie Title"].str.lower()) # just to find the index number for a movie
tfidf = TfidfVectorizer()

def movies(name):
    try:
        matrixs = tfidf.fit_transform(movies_data["genre"])
        simalar=linear_kernel(matrixs[indexed[name]],matrixs)
        movies_data["similar"] = simalar[0]
        data =  movies_data.sort_values(by="similar",ascending=False).head(10)
        x = zip(data["Movie Title"],data["Ratinng"],data["genre"],data["img"])
        return x
    except:
        return 1



def database():
    x = zip(movies_data["Movie Title"],movies_data["Ratinng"],movies_data["genre"],movies_data["img"])
    return x
    



# res = movies("PK")

# for name,rating,gen,img in res:
#     print(f"this movie {name} is having {rating} and genre {gen}")