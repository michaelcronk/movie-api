from azure.cosmos import CosmosClient, exceptions
from fetch_and_store import (
    fetch_and_store_movie_data,
    container,
)
import creds

# Azure Cosmos DB details (reusing the container initialized in fetch_and_store for simplicity)
cosmos_client = CosmosClient(creds.cosmos_endpoint, creds.cosmos_key)
database = cosmos_client.get_database_client(creds.cosmos_database_name)


def retrieve_movie_data(movie_title):
    try:
        query = "SELECT * FROM c WHERE LOWER(c.Title) = @title"
        parameters = [{"name": "@title", "value": movie_title.lower()}]
        items = list(
            container.query_items(
                query=query, parameters=parameters, enable_cross_partition_query=True
            )
        )
        return items if items else None
    except exceptions.CosmosResourceNotFoundError:
        print(f"No data found for movie: {movie_title}")
        return None
    except exceptions.CosmosHttpResponseError as e:
        print(f"An error occurred: {e}")
        return None


def display_movie_data(movie_data):
    if not movie_data:
        print("No movie data to display.")
        return

    for item in movie_data:
        print(f"Title: {item.get('Title')}")
        print(f"Year: {item.get('Year')}")
        print(f"Rated: {item.get('Rated')}")
        print(f"Released: {item.get('Released')}")
        print(f"Runtime: {item.get('Runtime')}")
        print(f"Genre: {item.get('Genre')}")
        print(f"Director: {item.get('Director')}")
        print(f"Writer: {item.get('Writer')}")
        print(f"Actors: {item.get('Actors')}")
        print(f"Plot: {item.get('Plot')}")
        print(f"Language: {item.get('Language')}")
        print(f"Country: {item.get('Country')}")
        print(f"Awards: {item.get('Awards')}")
        print(f"Poster URL: {item.get('poster_url')}")
        print("------------------------------------------------------------")


def main():
    movie_title = input("What movie would you like to know about: ")
    movie_data = retrieve_movie_data(movie_title)

    if not movie_data:
        # Fetch and store data on-demand if not found in database
        movie_data = fetch_and_store_movie_data(movie_title)
        if movie_data:
            movie_data = [movie_data]

    display_movie_data(movie_data)


if __name__ == "__main__":
    main()
