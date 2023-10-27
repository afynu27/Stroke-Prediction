import streamlit as st
import ml_app

def home_display():
    st.image("stroke.jpg", use_column_width=True)

    st.info("Stroke is a medical condition that occurs when there is a sudden disruption in the blood supply to the brain, leading to damage or cell death in the affected area. This can result in various neurological symptoms, such as difficulty speaking, weakness in the limbs, or loss of coordination. Strokes can be caused by a blood clot blocking a blood vessel (ischemic stroke) or by the rupture of a blood vessel (hemorrhagic stroke). Prompt medical attention is crucial to minimize the damage caused by a stroke.")



def main():
    custom_css = """
    <style>
        .title-text {
            font-size: 36px;
            text-align: center;
            background-color: #3498db; 
            color: white;
            padding: 10px;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown('<p class="title-text">Stroke Prediction</p>', unsafe_allow_html=True)

    menu = ['Home','Prediction']

    choice = st.sidebar.selectbox('Home',menu)

    if choice == "Home":
        home_display()
    elif choice == "Prediction":
        st.subheader("Please input your personal information and health history")
        ml_app.get_data()
        

if __name__ == '__main__':
    main()