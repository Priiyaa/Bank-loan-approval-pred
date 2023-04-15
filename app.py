import streamlit as st
import numpy as np
import pickle


model = pickle.load(open('ML_Model1.pkl', 'rb'))

def run():
   
    st.title("Bank Loan Prediction using Machine Learning")


    ## Current loan amount
    curr_loan = st.number_input('Current Loan Amount',value=0)

    ## Credit score
    Credit_score = st.number_input('Credit Score',value=0)

    ## For term
   
    term_display = ('Short term','Long term')
    term_options = list(range(len(term_display)))
    term = st.selectbox("Term",term_options, format_func=lambda x: term_display[x])
    


    ## For Marital Status
    Annual = st.number_input('Annual Income',value=0)
    

    ## No of dependets
    Yr_curr_job=st.number_input('Years in current job',value=0)

    ## For edu
    Home_Own= ('Own Home','Rent')
    Home_opt = list(range(len(Home_Own)))
    Home = st.selectbox("Home Ownership",Home_opt, format_func=lambda x: Home_Own[x])
    
         
 

    ## For emp status
    purpose_display = ('Home Improvements','Debt Consolidations','Buy House','Buy Car','Take a trip','other','Medical bill','Eduacation')
    purpose_opt = list(range(len( purpose_display)))
    Purpose = st.selectbox("Purpose for taking loan",purpose_opt, format_func=lambda x:  purpose_display[x])

    ## For Property status
    Monthly_debt=st.number_input('Monthly debt',value=0)

    Num_open_acc=st.number_input(' Number of Open Accounts',value=0)
    ## For Credit Score
    cred_hist = st.number_input('Years of Credit History',value=0)
    

    ## Applicant Monthly Income
    cred_prob = st.number_input("Number of Credit Problems",value=0)

    ## Co-Applicant Monthly Income
    curr_cred_bal = st.number_input("Current Credit Balance",value=0)

    ## Loan AMount
    max_open_acc = st.number_input("Maximum Open Credit",value=0)

    ## loan duration
    Bankruptcies=st.number_input('Number of Bankruptcies',value=0)
    Tax_Liens=st.number_input('Tax liens',value=0)
     

    if st.button("Submit"):
        
    
        features =np.array([[curr_loan, Credit_score, term, Annual,Num_open_acc,  Yr_curr_job,Home, Purpose, Monthly_debt, cred_hist, cred_prob, curr_cred_bal,max_open_acc,Bankruptcies,Tax_Liens]])
        print(features)
        prediction = model.predict(features)
        print('prediction:',prediction)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.error(
                "Hello! We are sorry to inform you that " +" || "
                
                'According to our Calculations, you will not get the loan from Bank'
            )
        else:
            st.success(
                'Hello! Congratulations!! you will get the loan from Bank'
            )

run()