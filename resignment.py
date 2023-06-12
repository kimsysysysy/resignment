import requests
from bs4 import BeautifulSoup

url = "https://search.musinsa.com/ranking/best?period=now&age=ALL&mainCategory=001&subCategory=&leafCategory=&price=&golf=false&kids=false&newProduct=false&exclusive=false&discount=false&soldOut=false&page=1&viewType=small&includeWomen=false&priceMin=&priceMax="

# 웹 페이지에 HTTP 요청 보내기
response = requests.get(url)

# 응답 받은 HTML 코드 파싱하기
soup = BeautifulSoup(response.content, 'html.parser')

# 상품 리스트 추출하기
product_list = soup.select('.li_box')

# 각 상품 정보 추출하기
for rank, product in enumerate(product_list, 1):
    product_name_elem = product.select_one('.list_info > a')
    product_name = product_name_elem.text.strip() if product_name_elem else "상품명 없음"
    product_price_elem = product.select_one('.price')
    product_price = product_price_elem.text.strip() if product_price_elem else "가격 없음"
    image_url_elem = product.select_one('.lazyload')
    image_url = image_url_elem['data-original'] if image_url_elem else "이미지 없음"
    print("순위:", rank)
    print("상품명:", product_name)
    print("가격:", product_price)
    print("이미지 URL:", image_url)
    print()

