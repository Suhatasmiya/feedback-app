import streamlit as st
import requests
import json

# Replace with your Supabase details
SUPABASE_URL = "https://vwtgxaglfqywgonyetjf.supabase.co"
SUPABASE_KEY = "YOUR_ANON_KEY"

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

st.title("📝 Feedback Collector")

name = st.text_input("Your Name")
message = st.text_area("Your Feedback")

if st.button("Submit"):
    if name and message:
        data = {
            "name": name,
            "message": message
        }
        res = requests.post(f"{SUPABASE_URL}/rest/v1/feedback", headers=headers, data=json.dumps(data))
        if res.status_code == 201:
            st.success("Feedback submitted!")
        else:
            st.error("Failed to submit feedback.")
    else:
        st.warning("Please fill out all fields.")

st.subheader("📋 All Feedback:")
res = requests.get(f"{SUPABASE_URL}/rest/v1/feedback?select=*", headers=headers)

if res.status_code == 200:
    for row in res.json():
        st.markdown(f"**{row['name']}** said: {row['message']}")
else:
    st.error("Error loading feedback")
