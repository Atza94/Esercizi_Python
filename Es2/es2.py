# esercizio_due
# Inserendo tre numeri determinare il maggiore dei tre ed il minore
# inserimento con input slider ver0.1
# inserimento con text input ver0.2
import streamlit as st
import numpy as np

def sort(x,y,z):
    lst=[x,y,z]
    lst.sort()
    return lst


    





def main():
    st.header("Secondo esercizio")
st.subheader("sorter automatico")

a=st.slider('seleziona il primo numero', 0.0, 100.0)
b=st.slider('seleziona il secondo numero', 0.0, 100.0)
c=st.slider('seleziona il terzo numero' 0.0,100.0)
    
ordine=sort(a,b,c)
st.text(ordine)   

if __name__=="__main__":
    main()