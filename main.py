import pandas as pd
import matplotlib.pyplot as plt

# Get data from csv and clean it for other functions
def clear_the_data(): 
    data = pd.DataFrame(pd.read_csv("netflix_movies.csv"))
    data.fillna({"director": "Anonymous"}, inplace=True)
    data.fillna({"cast": "The cast of the film has not been written yet"},inplace=True)
    data.fillna({"country": "Other"},inplace=True)
    data.fillna({"date_added": "No Date"}, inplace=True)
    data.fillna({"rating":0},inplace=True)
    data.fillna({"duration":0},inplace=True)
    return data

# Percentage of movies and tv series released by year out of all movies and tv series
def show_percentages_on_pie():
    # Get the clean data
    data = clear_the_data()

    # Not all columns. Only release_year data is needed
    # The variable "Other" is for low count years, in this way the pie will look good and clean
    years = data["release_year"].value_counts()
    other = [e for e in years if e < 560]
    sizes = [count for count in years if count > 559]
    labels = list(years.index)[0:7] 
    other_label = ["Other"]

    # The data is ready lets make the pie 
    fig,ax = plt.subplots()
    ax.pie((sizes+[sum(other)]),
           labels=(labels+other_label),
           autopct="%1.1f%%",
           wedgeprops={"edgecolor":"black", 
                        'linewidth': 0.5} )
    plt.legend((sizes+[sum(other)]),title="sizes")
    plt.title("Percentage of movies and tv series released by year out of all movies and tv series")
    fig.savefig("img/image-pie.png")
    plt.show()

# Number of movies and TV series by country (Top 10)
def sort_by_country_in_hbar():

    # Get the clean data
    data = clear_the_data()

    # We just need "country" data, countries[0:10] for top 10 countries
    countries = data["country"].value_counts()
    x = [e for e in countries[0:10]]
    y = list(countries[0:10].index)

    # Horizontal Bar
    plt.barh(y,x)
    plt.ylabel("Countries")
    plt.xlabel("Number of movies and TV series")
    plt.title("Number of movies and TV series by country (Top 10)")
    plt.savefig("img/image-hbar.png")
    plt.show()

def type():
    data = clear_the_data()
    types = data["type"].value_counts()
    sizes = [e for e in types]
    labels = list(types.index)
    fig,ax = plt.subplots()
    ax.bar(labels,sizes)
    ax.set_ylabel("Sizes")
    ax.set_title("TV Show vs Movie")
    fig.savefig("img/image-bar.png")
    plt.show()

# Directors who added the most content (top10)
def directors():
    data = clear_the_data()
    directors = data["director"].value_counts()
    name = list(directors.index)[0:10]
    count = [e for e in directors][0:10]

    for_data_frame = {
        "Directors": name,
        "Number of Movies/Shows" : count
    }
    df = pd.DataFrame(for_data_frame)
    df.index = [e for e in range(1,11)]
    print(df)

def duration_of_the_Movies():

    data = clear_the_data()

    durations_for_films = [e for e in data[data["type"]=="Movie"]["duration"]]
    list_d = []
    for d in durations_for_films:
        try:
            list_d.append(int(d.split()[0]))
        except:
            pass

    plt.hist(list_d)
    plt.ylabel("Number of the Movies")
    plt.xlabel("Duration of the Movies (min)")
    plt.title("Number of movies by duration")
    plt.savefig("img/image-histogram.png")
    plt.show()

if __name__ == "__main__":
    show_percentages_on_pie()
    sort_by_country_in_hbar()
    directors()
    type()
    duration_of_the_Movies()