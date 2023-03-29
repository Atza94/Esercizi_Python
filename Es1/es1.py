import streamlit as st
 
 
def idoneita_eta(age,patente):
    if age >= 18 and patente == "Si":
        stato = "abilitato"
        return stato
    elif age >= 18 and patente =="No":
        stato = "non abilitato"
        return stato
    elif age <= 18 and age >= 0:
        stato = "non puoi ancora guidare"
        return stato

   
        

   


def main():

    st.title("Primo esercizio")
    st.header("Idoneità alla guida")
    x = st.number_input(label="Inserisci la tua età", max_value=100, min_value=0, step=1)
    y = st.radio(label="Hai la patente?", options=("Si","No"))

    caso = idoneita_eta(x,y)

    st.text(caso)



if __name__ == "__main__":
  main()
    