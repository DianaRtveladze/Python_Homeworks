import requests

def fetch_product_data():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None

def analyze_product_data(products):
    if not products:
        return

    # ა) შექმენით პროდუქტის ფასების სია და გამოიტანეთ როგორც მაქსიმალური ასევე მინიმალური და სასშუალო ფასები
    prices = [product["price"] for product in products]
    max_price = max(prices)
    min_price = min(prices)
    avg_price = sum(prices) / len(prices)

    print(f"Maximum Price: ${max_price}")
    print(f"Minimum Price: ${min_price}")
    print(f"Average Price: ${avg_price:.2f}\n")

    # ბ) შექმენით კატეგორიების სია (დუბლიკაციების გარეშე) და დაასორტირეთ
    categories = sorted(set(product["category"] for product in products))
    print("Categories:", categories, "\n")

    # გ) შექმენით სია რომელშიც გექნებად პროდუქტის აღწერა (title) და id. დაასორტირეთ შედეგი title-ის მიხედვით
    product_info = sorted([(product["title"], product["id"]) for product in products], key=lambda x: x[0])
    print("Product Information:")
    for title, product_id in product_info:
        print(f"Title: {title}, ID: {product_id}")
    print()

    # გ) შექმენით სია რომელშიც გექნებად პროდუქტის აღწერა (title) და id. დაასორტირეთ შედეგი title-ის მიხედვით
    ratings = sorted(products, key=lambda x: x["rating"]["rate"])
    print("Ratings (Sorted by Rate):")
    for product in ratings:
        print(f"Product: {product['title']}, Rate: {product['rating']['rate']}")
    print()

if __name__ == "__main__":
    products_data = fetch_product_data()

    if products_data:
        analyze_product_data(products_data)
