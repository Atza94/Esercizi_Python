import streamlit as st
 
 
st.title("Primo esercizio")
st.header("Idoneità alla guida")

# x=st.number_input(label="Inserisci la tua età", max_value=100, min_value=0, step=1)

# y = st.radio(label="Hai la patente?", options=("Si","No"), index=0)

def idoneità(x,y):
    x=st.number_input(label="Inserisci la tua età", max_value=100, min_value=0, step=1)

    y = st.radio(label="Hai la patente?", options=("Si","No"), index=0)
    if x >= 18 and y == [0]:
        return True
    else:
        return False

if idoneità == True:
     st.write("abilitato alla guida")
else:
     st.write("non abilitato")

st.button('conferma dati', on_click="idoneità()")


        

   


# #def main():
#     st.title("Primo esercizio")
#     st.header("Idoneità alla guida")

#     age=st.number_input(label="Inserisci la tua età", max_value=100, min_value=0 )

#     patente=st.radio(label="Hai la patente?", options=("Si","No"))
    


#     def license (age,patente):
#         if age  >= 18 and patente == "Si":
#             st.write("Sei idoneo alla guida")
#         else:
#             st.write("Non sei idoneo alla guida")





# #if __name__ == "__main__":
#   # main()
    