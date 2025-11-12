import streamlit as st

def generate_urls(base_url, asin_list):
    """Generate Walmart URLs from a list of Item IDs."""
    return [base_url.format(asin) for asin in asin_list]

# Streamlit App
st.title("Walmart Item Multi-Link Opener")
st.write("Enter Item IDs to open their product pages on Walmart with a single click.")

base_url = "https://www.walmart.com/ip/{}"
asin_input = st.text_area("Enter Item IDs (one per line):")

if st.button("Open All Links"):
    if asin_input.strip():
        asin_list = [x.strip() for x in asin_input.split("\n") if x.strip()]
        urls = generate_urls(base_url, asin_list)
        
        # Generate JavaScript to open all URLs
        js_code = "<script>\n"
        for url in urls:
            js_code += f"window.open('{url}', '_blank');\n"
        js_code += "</script>"

        # Inject JavaScript directly into the browser using st.components
        st.components.v1.html(js_code, height=0)
        st.success(f"Opened {len(urls)} links in new tabs!")
    else:
        st.warning("Please enter at least one Item ID.")
