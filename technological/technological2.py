from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

@app.get("/api/recepts")
def get_list_of_recepts():
    return

@app.get("/api/recept")
def get_recept_from_list():
    return

@app.post("/api/recepts/favorite")
def add_recept_to_favorite():
    return

@app.get("/api/recepts/favorite")
def get_recept_from_favotite():
    return

@app.get("/api/products")
def get_list_of_products():
    return

@app.get("/api/product")
def get_product_from_list():
    return

@app.post("/api/products/favorite")
def add_poroduct_to_favorite():
    return

@app.get("/api/products/favorite")
def get_product_drom_favorite():
    return

@app.post("/api/review")
def add_review_to_recipe():
    return

@app.post("/api/newslatter")
def subscribe_to_the_newsletter():
    return

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)