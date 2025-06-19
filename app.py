import streamlit as st
from supabase import create_client, Client

# Replace with your Supabase project URL and anon key
url = "https://vwtgxaglfqywgonyetjf.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZ3dGd4YWdsZnF5d2dvbnlldGpmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTAyNDQzMTksImV4cCI6MjA2NTgyMDMxOX0.WYZpvz61aVKJxNuOYcVxHu6kxLaQyMfGQwDfMBsrIw4"
supabase: Client = create_client(url, key)

st.title("📝 Feedback Collector")

name = st.text_input("Your Name")
message = st.text_area("Your Feedback")

if st.button("Submit"):
    if name and message:
        data = {"name": name, "message": message}
        supabase.table("feedback").insert(data).execute()
        st.success("Feedback submitted!")
    else:
        st.error("Please fill in all fields.")

st.subheader("📋 All Feedback:")
feedback_data = supabase.table("feedback").select("*").order("inserted_at", desc=True).execute()
for entry in feedback_data.data:
    st.markdown(f"**{entry['name']}** said: {entry['message']}")

