import streamlit as st
 
 
st.title("Primo esercizio")
st.header("Idoneità alla guida")

x = st.number_input(label="Inserisci la tua età", max_value=100, min_value=0, step=1)

y = st.radio(label="Hai la patente?", options=("Si","No"))

def idoneita_eta(x):
    if x >= "18":
        return True
    else:
        return False

if idoneita_eta == True:
     st.write("abilitato")
else:
     st.write("non abilitato")
   
        

   


# #def main():




# #if __name__ == "__main__":
#   # main()
    