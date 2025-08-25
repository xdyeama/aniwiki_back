from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

JIKAN_BASE_URL = "https://api.jikan.moe/v4"

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# --- Endpoints ---
# List of anime with pagination
@app.get("/anime/")
async def get_anime_list(page: int = 1):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{JIKAN_BASE_URL}/anime", params={"page": page})
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching anime list")
        return response.json()
    
# List of manga with pagination
@app.get("/manga/")
async def get_manga_list(page: int = 1):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{JIKAN_BASE_URL}/manga", params={"page": page})
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching manga list")
        return response.json()
    
# Search anime by keywords with pagination
@app.get("/anime/search/")
async def search_anime(query: str, page: int = 1):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{JIKAN_BASE_URL}/anime", params={"q": query, "page": page})
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error searching anime")
        return response.json()
    
# Search manga by keywords with pagination
@app.get("/manga/search/")
async def search_manga(query: str, page: int = 1):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{JIKAN_BASE_URL}/manga", params={"q": query, "page": page})
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error searching manga")
        return response.json()

# Get anime details by ID
@app.get("/anime/{anime_id}")
async def get_anime_by_id(anime_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{JIKAN_BASE_URL}/anime/{anime_id}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching anime details")
        return response.json()
    
# Get manga details by ID
@app.get("/manga/{manga_id}")
async def get_manga_by_id(manga_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{JIKAN_BASE_URL}/manga/{manga_id}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching manga details")
        return response.json()
    
# Get specific anime characters
@app.get("/anime/{anime_id}/characters")
async def get_anime_characters(anime_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{JIKAN_BASE_URL}/anime/{anime_id}/characters")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching anime characters")
        return response.json()
    
# Get specific manga characters
@app.get("/manga/{manga_id}/characters")
async def get_manga_characters(manga_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{JIKAN_BASE_URL}/manga/{manga_id}/characters")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching manga characters")
        return response.json()
