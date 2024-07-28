# Azure Movie Database

## Overview

Azure Movie Database is a Python project that retrieves movie data from the OMDB API and stores it in an Azure Cosmos DB. Additionally, it saves the movie poster images to an Azure Blob Storage container. This project allows you to efficiently manage and query a movie database using cloud services.

> <sub>To get started, you first need to have a Microsoft Azure account. If you don't have one, you can create a free account [here.](https://azure.microsoft.com/en-us/free/search/?&ef_id=_k_Cj0KCQiA4NWrBhD-ARIsAFCKwWv39zVXs4ww7bj_IGmTJngZol8ZX835NOuvRgv7ygSk_rEe9lnrcGcaAg2vEALw_wcB_k_&OCID=AIDcmm5edswduu_SEM__k_Cj0KCQiA4NWrBhD-ARIsAFCKwWv39zVXs4ww7bj_IGmTJngZol8ZX835NOuvRgv7ygSk_rEe9lnrcGcaAg2vEALw_wcB_k_&gad_source=1&gclid=Cj0KCQiA4NWrBhD-ARIsAFCKwWv39zVXs4ww7bj_IGmTJngZol8ZX835NOuvRgv7ygSk_rEe9lnrcGcaAg2vEALw_wcB)</sub>

## Features

- **Retrieve Movie Data**: Fetch detailed movie information from the OMDB API.
- **Store Data in Azure Cosmos DB**: Save and manage movie data in a scalable NoSQL database.
- **Save Movie Posters to Azure Blob Storage**: Store movie poster images securely in Azure Blob Storage.
- **Case-Insensitive Search**: Perform case-insensitive queries to retrieve movie data.

## Requirements

- Python 3.7+
- Azure Subscription
- OMDB API Key

## Setup

### Prerequisites

1. **Azure Cosmos DB**: Create a Cosmos DB account and obtain the endpoint and key.
2. **Azure Blob Storage**: Create a Blob Storage account and obtain the connection string.
3. **OMDB API Key**: Obtain an API key from [OMDB API](http://www.omdbapi.com/apikey.aspx).

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/MovieDB-Azure.git
   cd MovieDB-Azure
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `creds.py` file in the project root directory and add your credentials or alternatively you can use `.env`.

```python
   # creds.py
   cosmos_endpoint = "your_cosmos_db_endpoint"
   cosmos_key = "your_cosmos_db_key"
   cosmos_database_name = "your_cosmos_db_name"
   cosmos_container_name = "your_cosmos_db_container_name"
   blob_connection_string = "your_blob_storage_connection_string"
   blob_container_name = "your_blob_container_name"
   omdb_api_key = "your_omdb_api_key"
```

## Usage

### Fetch and Store Movie Data

The `fetch_and_store.py` script fetches movie data from the OMDB API, stores it in an Azure Cosmos DB, and saves the movie poster to an Azure Blob Storage container.

## Retrieve and Display Movie Data

The `retrieve_and_display.py` script retrieves movie data from Azure Cosmos DB and displays it in the terminal. If the data is not found, it fetches and stores the data on-demand.

### Acknowledgements

- OMDB API for providing movie data.
- Azure for providing cloud services.
