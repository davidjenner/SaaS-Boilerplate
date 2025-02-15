import streamlit as st

# Set the title of the app
st.title("My Streamlit App")

# Add a header
st.header("Welcome to my app!")

# Add a subheader
st.subheader("This is a simple Streamlit app template.")

# Add text input
user_input = st.text_input("Enter some text:")

# Add a button
if st.button("Submit"):
    st.write(f"You entered: {user_input}")

    # Add a slider
    slider_value = st.slider("Select a value", 0, 100, 50)
    st.write(f"Slider value: {slider_value}")

    # Add a selectbox
    option = st.selectbox(
        "Choose an option",
            ["Option 1", "Option 2", "Option 3"]
            )
            st.write(f"You selected: {option}")

            # Add a checkbox
            if st.checkbox("Show more"):
                st.write("Here is some more information...")

                # Add a sidebar
                st.sidebar.title("Sidebar")
                st.sidebar.write("This is the sidebar content.")

                # Add a file uploader
                uploaded_file = st.file_uploader("Choose a file")
                if uploaded_file is not None:
                    st.write("File uploaded successfully!")

                    # Add a plot (example with matplotlib)
                    import matplotlib.pyplot as plt
                    import numpy as np

                    x = np.linspace(0, 10, 100)
                    y = np.sin(x)

                    fig, ax = plt.subplots()
                    ax.plot(x, y)
                    st.pyplot(fig)

                    # Add a dataframe (example with pandas)
                    import pandas as pd

                    data = {
                        "Column 1": [1, 2, 3, 4],
                            "Column 2": [10, 20, 30, 40]
                            }
                            df = pd.DataFrame(data)
                            st.write(df)
                            