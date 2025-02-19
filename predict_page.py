import pickle
import streamlit as st

model = pickle.load(open('forestc.pkl', 'rb'))

def predict_return(Final_Quantity, Total_Revenue, Price_Reductions, Sales_Tax):
    Final_Revenue = Total_Revenue
    Overall_Revenue = Final_Revenue + Sales_Tax
    Purchased_Item_Count = Final_Quantity
    prediction = model.predict([[Final_Quantity, Total_Revenue, Price_Reductions, Final_Revenue, Sales_Tax, Overall_Revenue, Purchased_Item_Count]])
    return prediction

def main():
    st.title("Product Return Prediction")
    st.write("Enter the details below to predict product return.")

    Final_Quantity = st.number_input('Enter the number of products ordered:', min_value=0, step=1)
    Total_Revenue = st.number_input('Enter the Product cost without tax included:', min_value=0.0, step=0.01)
    Price_Reductions = st.number_input('Enter the Discount price:', min_value=0.0, step=0.01)
    Sales_Tax = st.number_input('Enter the cost of Sales Tax:', min_value=0.0, step=0.01)

    if st.button("Predict"):
        result = predict_return(Final_Quantity, Total_Revenue, Price_Reductions, Sales_Tax)
        if Final_Quantity == 0:
            st.success('Enter the number of products ordered')
        if Total_Revenue - Price_Reductions <= Sales_Tax*3:
            st.success('Product will predicted to be return')
        elif result == 1:
            st.success('Product will predicted to be return')
        elif result == 0:
            st.success('Product will predicted not to be return')
        else:
            st.success('Product will predicted not to be return')

if __name__ == "__main__":
    main()
