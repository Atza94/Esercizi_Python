import streamlit as st
 
 
st.title("Primo esercizio")
st.header("Idoneità alla guida")

age=st.number_input(label="Inserisci la tua età", max_value=100, min_value=0 )

patente=st.radio(label="Hai la patente?", options=("Si","No"))
    
print(license)

def license (age,patente):
    if age  >= 18 and patente == "Si":
        return("Sei idoneo alla guida")
    else:
        return("Non sei idoneo alla guida")


#def main():
    st.title("Primo esercizio")
    st.header("Idoneità alla guida")

    age=st.number_input(label="Inserisci la tua età", max_value=100, min_value=0 )

    patente=st.radio(label="Hai la patente?", options=("Si","No"))
    


    def license (age,patente):
        if age  >= 18 and patente == "Si":
            st.write("Sei idoneo alla guida")
        else:
            st.write("Non sei idoneo alla guida")





#if __name__ == "__main__":
  # main()
    