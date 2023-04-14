import streamlit as st
import xlsxwriter
import pandas as pd


def somma(l1:float,l2:float):
    a = l1+l2
    return a 

def main():
    st.text("Ciao questo front-end funziona")
    # slider
    num1 = st.slider('Please inserisci lato1 rettangolo', 0, 100, 25)
    num2 = st.slider('Please inserisci lato2 rettangolo', 0, 100, 35)
    r = somma(num1,num2)

    st.write("la somma è ", r)

    input2 = st.text_input("Inserisci il nome della colonna")

    st.title("Data Transformation")
    st.markdown(":red[**choose a file**]")
    uploaded_file = st.file_uploader("",type={"xlsx"})
    
    
    
    if uploaded_file is not None:
        ###### transformation #####################################
        df = pd.read_excel(uploaded_file)
        st.dataframe(df)

        columns = st.sidebar.multiselect("Enter the variables", df.columns)

        sidebars = {}
        for y in columns:
            ucolumns=list(df[y].unique())
            print (ucolumns)

            sidebars[y]=st.sidebar.multiselect('Filter '+y, ucolumns)   
        
        if st.button('Start Processing', help="Process Dataframe"):
            st.header('Addes Column')
            df['new_col'] = 1
            if input2=="":
                df.fillna(0,inplace=True)
            else:
                df[input2].fillna(0,inplace=True)
            st.dataframe(df)
            st.balloons()
            import io
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                # Write each dataframe to a different worksheet.
                df.to_excel(writer, index=False)
                # Close the Pandas Excel writer and output the Excel file to the buffer
                writer.save()
                st.download_button(
                    label="Download Excel Result",
                    data=buffer,
                    file_name="trasnformed_file.xlsx",
                    mime="application/vnd.ms-excel")
                
if __name__ == "__main__":
    main()