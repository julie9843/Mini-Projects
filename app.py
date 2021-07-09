import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Gender, Married, ApplicantIncome,CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,Dependents, Education, Self_Employed, Property_Area):   
 
    # Pre-processing user input    
    if Gender == "Male":
        Gender = 0
    else:
        Gender = 1
 
    if Married == "Unmarried":
        Married = 0
    else:
        Married = 1
 
    if Credit_History == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1  
    ApplicantIncome = ApplicantIncome /1000
    Coapplicantincome = CoapplicantIncome /1000
    LoanAmount = LoanAmount / 1000
    Loan_Amount_Term =Loan_Amount_Term
    
    if Dependents == '0':
        Dependents = 0
    elif Dependents =='1':
        Dependents = 1
    elif Dependents =='2':
        Dependents = 2
    else: 
        Dependents = 3
    
    if Education == 'Graduate': 
        Education = 0
    else: 
        Education = 1
    
    if Self_Employed == 'No':
        Self_Employed = 0
    else: 
        Self_Employed = 1
        
    if Property_Area == "Urban":
        Property_Area = 0
    elif Property_Area == 'Rural':
        Property_Area = 1
    else:
        Property_Area = 2
        
    # Making predictions 
    prediction = classifier.predict( 
        [[Gender, Married, ApplicantIncome,CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,Dependents, Education, Self_Employed, Property_Area]])
     
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred

    
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:lightblue;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Loan Application</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    Gender = st.selectbox('Gender',("Male","Female"))
    Married = st.selectbox('Marital Status',("Unmarried","Married")) 
    ApplicantIncome = st.number_input("Applicants monthly income") 
    CoapplicantIncome = st.number_input("Coapplicants monthly income") 
    LoanAmount = st.number_input("Total loan amount")
    Loan_Amount_Term = st.number_input("Total loan term")
    Credit_History = st.selectbox('Credit_History',("Unclear Debts","No Unclear Debts"))
    Property_Area = st.selectbox('Property',("Urban","Rural","SemiUrban"))
    Education = st.selectbox('Education',("Graduate","Not Graduate"))
    Dependents = st.selectbox('No. of dependents',("0","1","2","3+"))
    Self_Employed = st.selectbox('Employment',("Y","N"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Gender, Married, ApplicantIncome,CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,Dependents, Education, Self_Employed, Property_Area) 
        st.success('Your loan is {}'.format(result))
        print(LoanAmount)
     
if __name__=='__main__': 
    main()