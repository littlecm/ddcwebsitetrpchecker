import streamlit as st
import requests

# Function to check the pages
def check_pages(domain):
    paths = [
        "/inventory/new/chevrolet-blazer.htm",
        "/inventory/new/chevrolet-blazer+ev.htm",
        "/inventory/new/chevrolet-bolt+euv.htm",
        "/inventory/new/chevrolet-bolt+ev.htm",
        "/inventory/new/chevrolet-camaro.htm",
        "/inventory/new/chevrolet-colorado.htm",
        "/inventory/new/chevrolet-corvette.htm",
        "/inventory/new/chevrolet-corvette+stingray.htm",
        "/inventory/new/chevrolet-equinox.htm",
        "/inventory/new/chevrolet-malibu.htm",
        "/inventory/new/chevrolet-silverado+1500.htm",
        "/inventory/new/chevrolet-silverado+2500+hd.htm",
        "/inventory/new/chevrolet-silverado+3500+hd.htm",
        "/inventory/new/chevrolet-suburban.htm",
        "/inventory/new/chevrolet-tahoe.htm",
        "/inventory/new/chevrolet-trailblazer.htm",
        "/inventory/new/chevrolet-traverse.htm",
        "/inventory/new/chevrolet-traverse+limited.htm",
        "/inventory/new/chevrolet-trax.htm"
    ]
    results = []
    for path in paths:
        url = f"{domain.strip('/')}{path}"
        try:
            response = requests.get(url, allow_redirects=True)
            if response.status_code == 200:
                result = {'URL': url, 'Status': 'Page found'}
                if response.history:
                    result['Redirected To'] = response.url
            else:
                result = {'URL': url, 'Status': f'Error {response.status_code}'}
        except requests.exceptions.RequestException as e:
            result = {'URL': url, 'Status': 'Error', 'Message': str(e)}
        results.append(result)
    return results

# Streamlit app UI
st.title('Domain Page Checker')

domain = st.text_input('Enter the primary domain (e.g., "https://www.example.com"):')

if domain:
    with st.spinner('Checking pages...'):
        results = check_pages(domain)
    
    for result in results:
        st.write(result)

