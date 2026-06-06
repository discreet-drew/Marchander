# Marchander

Marchander is a simple price comparison web application that helps users find product prices from different online stores.

The idea behind this project was to learn web scraping, backend development, frontend development, and how real-world price comparison websites work.

Currently, the project supports searching products from Flipkart and displaying their prices in a simple web interface.

---

## Features

* Search for a product
* Find matching products on Flipkart
* Extract product title and price automatically
* Display product information in a clean UI
* Real-time data using Playwright

---

## Technologies Used

### Backend

* Python
* Flask
* Playwright

### Frontend

* HTML
* CSS
* JavaScript

---

## How It Works

1. User enters a product name.
2. The application searches Flipkart for the product.
3. The first matching product link is extracted.
4. The scraper opens the product page.
5. Product details and price are extracted.
6. Results are displayed on the website.

---

## Project Structure

```text
Marchander/

backend/
│
├── app/
│   └── scrapers/
│       ├── flipkart.py
│       └── flipkart_search.py
│
├── server.py
├── requirements.txt
└── test_flipkart.py

frontend/
│
├── index.html
├── style.css
└── script.js
```

---

## Running The Project

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Marchander.git
```

### Create a virtual environment

```bash
python -m venv venv311
```

### Activate the environment

```bash
venv311\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Install Playwright browser

```bash
python -m playwright install chromium
```

### Start the backend

```bash
python server.py
```

### Start the frontend

```bash
cd frontend

python -m http.server 5500
```

Open:

```text
http://localhost:5500
```

---

## Example

Search:

```text
iphone 15
```

Output:

```text
Apple iPhone 15 (Black, 128 GB)

₹59,900

Store: Flipkart
```

---

## Future Improvements

Some features I plan to add in the future:

* Amazon support
* Multi-store price comparison
* Lowest price highlighting
* Price history tracking
* PostgreSQL database
* User accounts and watchlists
* Price drop notifications

---

## Why I Built This

I wanted a project that would help me learn:

* Web scraping
* Browser automation
* Backend APIs
* Frontend development
* Full-stack application development

## Future Scope

Marchander is currently focused on Flipkart product search and price extraction, but it is designed to grow into a complete price comparison platform.

### Multi-Store Price Comparison

* Add Amazon support
* Add Reliance Digital support
* Compare prices across multiple stores simultaneously

### Fashion Category

* Add Myntra integration
* Add Ajio integration
* Add Max Fashion integration
* Compare clothing, footwear, and accessories across fashion retailers

### Product Database

* Store product information in PostgreSQL
* Maintain product records across multiple stores
* Improve matching of similar products with different titles

### Price History Tracking

* Track price changes over time
* Display historical price charts
* Show highest, lowest, and average prices

### User Features

* User registration and login
* Personal watchlists
* Favorite products
* Search history

### Smart Notifications

* Email alerts when prices drop
* Wishlist notifications
* Daily or weekly price summaries

### AI-Powered Features

* Product matching using embeddings
* AI-generated product summaries
* Alternative product recommendations
* Review sentiment analysis

### Deployment & Scalability

* Docker containerization
* AWS deployment
* Background scraping with Celery and Redis
* Automated scheduled price updates

### Mobile Application

* Android application
* iOS application
* Push notifications for price drops

### Long-Term Vision

The long-term goal of Marchander is to become a centralized shopping platform where users can search for any product and instantly compare prices, discounts, ratings, and availability across multiple online stores from a single interface.

---

## Author

Dhruv
Computer Science Student | Software Engineering & AI Enthusiast
