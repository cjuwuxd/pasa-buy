import streamlit as st
import requests
import datetime
from datetime import date
st.set_page_config(page_title="Shop App",page_icon="🛒")

st.title("Pasa-Buy")


def confirmOrder():
    url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSf9BawsjXXrZjz7dpXlYHnbhCG1z78sUFb1u03COzGDwy33gw/formResponse"

    data = {
        "entry.1287434678" : nameOfbuyer,
        "entry.1845676056" : order,
        "entry.97520968" : modeOfPayment,
        "entry.979361838_year" : year,
        "entry.979361838_month" : month,
        "entry.979361838_day" : day,
        "entry.1700478353" : desOrder,
        "entry.1452035887" : userContact
    }

    try:
        # st.write(nameOfbuyer)
        # st.write(order)
        # st.write(desOrder)
        # st.write(userContact)
        # st.write(modeOfPayment)
        # st.write(year)
        # st.write(day)
        # st.write(month)
        
        response = requests.post(url, data=data)

        if str(response.status_code) == "200":
            st.success("Your Order has been sent!")
    except requests.exceptions.RequestException as e:
        st.error(e)
        st.error(response.status_code)

def main():
    global nameOfbuyer
    global order
    global desOrder
    global userContact
    global year
    global month
    global day
    global modeOfPayment

    nameOfbuyer = st.text_input("Your Name")
    order = st.text_input("What do you want to order?")
    dateOfOrder = st.date_input("When do you want your order?", datetime.date(2025,7,15))
    modeOfPayment = st.selectbox("Mode of Payment",("Cash on Delivery","GCash"))
    desOrder = st.text_input("Other details of your order?")
    userContact = st.text_input("Contact Information (Email, Phone #)")

    dateOfOrder = str(dateOfOrder)
    dateOfOrder = dateOfOrder.split("-")
    year = dateOfOrder[0]
    day = dateOfOrder[1]
    month = dateOfOrder[2]

    

    if st.button("Submit Order"):
        confirmOrder()

main()
