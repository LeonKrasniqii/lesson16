import streamlit as st

def main():
    st.title("Hello World !!")

if __name__=="__main__":
    main()


if st.button("Click Me"):
    st.write("Button Clicked")

if st.checkbox("Check Me"):
    st.write("The check box has been checked")

user_input = st.text_input("Enter Text","Sample Text")

st.write("You enterd", user_input)

age = st.number_input("Enter your age", min_value=0 , max_value = 100)
st.write(f"Your age is:{age}")

message = st.text_area("Enter a message")
st.write(f"Your message is:{message}")