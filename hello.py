from flask import Flask, jsonify, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def fetch_personal_info(url):
    headers = {'Referer': url}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        return {"error": str(e)}

    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        personal_info = {
            "Country": soup.find('th', text="Country").find_next_sibling('td').text.strip(),
            "Name": soup.find('th', text="Name").find_next_sibling('td').text.strip(),
            "Address": soup.find('th', text="Address").find_next_sibling('td').text.strip(),
            "City": soup.find('th', text="City").find_next_sibling('td').text.strip(),
            "Postcode": soup.find('th', text="Postcode").find_next_sibling('td').text.strip(),
            "Gender": soup.find('th', text="Gender").find_next_sibling('td').text.strip(),
            "Date Of Birth": soup.find('th', text="Date Of Birth").find_next_sibling('td').text.strip(),
            "Phone": soup.find('th', text="Phone").find_next_sibling('td').text.strip(),
            "Age (Years)": soup.find('th', text="Age (Years)").find_next_sibling('td').text.strip(),
            "IBAN": soup.find('th', text="IBAN").find_next_sibling('td').text.strip(),
            "Bank Name": soup.find('th', text="Bank Name").find_next_sibling('td').text.strip(),
            "Bank Code": soup.find('th', text="Bank Code").find_next_sibling('td').text.strip(),
            "BIC": soup.find('th', text="BIC").find_next_sibling('td').text.strip(),
            "Account Number": soup.find('th', text="Account Number").find_next_sibling('td').text.strip(),
        }
    except AttributeError as e:
        return {"error": "Failed to parse HTML: " + str(e)}

    return personal_info

@app.route('/fake_de', methods=['GET'])
def scrape_fake_de():
    url = 'https://fakeit.receivefreesms.co.uk/c/de/'
    personal_info = fetch_personal_info(url)
    return jsonify(personal_info)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)