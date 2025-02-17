import streamlit as st
import requests

# Function to fetch financial books from Google Books API
def get_financial_books(query="finance"):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=10"
    response = requests.get(url)
    data = response.json()
    return data.get("items", [])

# Page Configuration
st.set_page_config(page_title="Financial Books", layout="wide")

# Custom CSS for Styling
st.markdown(
    """
    <style>
        .title {
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            color: white;
            text-shadow: 2px 2px 10px orange;
        }
        .book-card {
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 15px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            color: white;
            display: flex;
            align-items: center;
        }
        .book-image {
            width: 100px;
            height: auto;
            border-radius: 8px;
            margin-right: 15px;
        }
        .book-content {
            flex: 1;
        }
        .book-title {
            font-size: 18px;
            font-weight: bold;
        }
        .book-link {
            background: white;
            padding: 5px 10px;
            border-radius: 5px;
            text-decoration: none;
            font-size: 14px;
            font-weight: bold;
            color: black;
            display: inline-block;
            margin-top: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='title'>📚 Financial Literacy Books</div>", unsafe_allow_html=True)

# Search Bar
search_query = st.text_input("🔍 Search for a finance-related book:", "finance")

# Fetch and Display Books
books = get_financial_books(search_query)
if books:
    for book in books:
        info = book.get("volumeInfo", {})
        title = info.get("title", "No Title")
        authors = ", ".join(info.get("authors", ["Unknown Author"]))
        description = info.get("description", "No description available.")
        link = info.get("infoLink", "#")
        image_url = info.get("imageLinks", {}).get("thumbnail", None)

        st.markdown(
            f"""
            <div class='book-card'>
                {'<img class="book-image" src="' + image_url + '">' if image_url else ""}
                <div class='book-content'>
                    <div class='book-title'>{title}</div>
                    <div>👨‍💼 Author(s): {authors}</div>
                    <p>{description[:200]}...</p>
                    <a class='book-link' href='{link}' target='_blank'>🔗 More Info</a>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
else:
    st.warning("No books found! Try a different search term.")

