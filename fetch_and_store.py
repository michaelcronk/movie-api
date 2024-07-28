import requests
import uuid
import creds
from azure.cosmos import exceptions, CosmosClient, PartitionKey
from azure.storage.blob import BlobServiceClient

# OMDB API details
omdb_url = f"http://www.omdbapi.com/?apikey={creds.omdb_api_key}&"
omdb_img_url = f"http://img.omdbapi.com/?apikey={creds.omdb_api_key}&"

# Initialize the Cosmos DB client
cosmos_client = CosmosClient(creds.cosmos_endpoint, creds.cosmos_key)
database = cosmos_client.create_database_if_not_exists(id=creds.cosmos_database_name)
container = database.create_container_if_not_exists(
    id=creds.cosmos_container_name,
    partition_key=PartitionKey(path="/id"),
)

# Initialize Blob Storage client
blob_service_client = BlobServiceClient.from_connection_string(
    creds.blob_connection_string
)
blob_container_client = blob_service_client.get_container_client(
    creds.blob_container_name
)
# Create the container if it does not exist
if not blob_container_client.exists():
    blob_container_client.create_container()


def fetch_movie_data(title):
    response = requests.get(omdb_url, params={"t": title})
    return response.json()


def fetch_image_data(imdb_id):
    response = requests.get(omdb_img_url, params={"i": imdb_id})
    return response.content


def save_image_to_blob(image_url, image_name):
    response = requests.get(image_url)
    blob_client = blob_container_client.get_blob_client(image_name)
    blob_client.upload_blob(response.content, overwrite=True)
    return blob_client.url


def save_movie_data_to_cosmos(movie_data, image_url):
    movie_data["id"] = str(uuid.uuid4())
    movie_data["poster_url"] = image_url
    container.upsert_item(movie_data)


def fetch_and_store_movie_data(movie_title):
    movie_data = fetch_movie_data(movie_title)
    print(f"Fetched movie data: {movie_data}")  # Debugging line

    if movie_data.get("Response") == "True":
        poster_url = movie_data.get("Poster")
        if poster_url and poster_url != "N/A":
            try:
                image_url = save_image_to_blob(
                    poster_url, f"{movie_title.replace(' ', '_')}.jpg"
                )
                save_movie_data_to_cosmos(movie_data, image_url)
                print(f"Movie data for '{movie_title}' saved successfully.")
                return movie_data
            except Exception as e:
                print(f"Error saving movie data or image: {e}")
                return None
        else:
            print(f"No poster available for '{movie_title}'.")
            return None
    else:
        print(f"Movie '{movie_title}' not found.")
        return None
