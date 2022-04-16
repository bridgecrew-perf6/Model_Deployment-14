import streamlit as st
import pickle
import pandas as pd
import base64
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.neighbors import KNeighborsClassifier




st.markdown(
			"<h1 style='font-size:250%;\
						font-family:courier;\
						text-align:center;\
						background-color:;\
						color:#c5d04f;'>Predict Whether Your Employee Will Leave Your Company\
			</h1>", unsafe_allow_html=True
			)




st.markdown("""
			<div style="background-color:#c5d04f;\
						border-radius: 10px;\
						padding:15px">
			<h2 style="color:white;\
					   text-align:center;\
					   font-family:courier;">Churn Prediction Machine Learning App with Streamlit\
			</h2>
			</div>
			""", unsafe_allow_html=True
			)

st.write('\n')

st.markdown(
    		f"""
    		<div>
        	<img class="churn2.png" 
				 src="https://www.retainable.ai/upload/blog/employee_churn__hr_from_a_business_intelligence_point_of_view.jpg" 
				 width="704">
			</img>
    		</div>
    		""", unsafe_allow_html=True
			)


st.write('\n')

st.markdown("""
			<center>
			<p style='font-size:200%;\
						background-color:#c5d04f;\
						border-radius: 10px;\
						color:white;'>Select Your Machine Learning Model\
			</p>
			</center>
			""", unsafe_allow_html=True
			)

st.markdown("""
			<style>
    		[data-baseweb="select"] {
        							margin-top: -50px;
    								}
    		</style>
    		""", unsafe_allow_html=True,
			)
st.sidebar.markdown(
			"<h1 style='text-align:center;\
						background-color:#c5d04f;color:white;border-radius: 10px;font-family:courier;font-size:100%;'><b>Will Your Employee Run Away?</b><br>\
							Let's Have a Look.<br>Please Fill the Following Fields.\
			</h1>", unsafe_allow_html=True
			)
st.sidebar.write('\n')

st.sidebar.markdown(
    		f"""
    		<div>
        	<img class="churn1.png" 
				src="https://blog.entelo.com/hs-fs/hub/202646/file-2029121037-png/Screen_Shot_2014-11-04_at_11.26.48_AM.png" 
				width="300">
			</img>
    		</div>
    		""", unsafe_allow_html=True
			)
#<img class="churn1.png" 
				 #src="data:image/png;base64,{base64.b64encode(open("churn1.png", "rb").read()).decode()}" width="300">
			#</img>

st.sidebar.write('\n')

st.sidebar.markdown("""
			<p style='text-align:center;\
						color: white; background-color:#c5d04f;'>Please Slide\
			</p>
			""", unsafe_allow_html=True
			)

satisfaction_level = st.sidebar.slider(label = "Satisfaction Level Score", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
last_evaluation = st.sidebar.slider(label="Performance Evaluation Score", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
average_monthly_hours = st.sidebar.slider("Average working hours per month", min_value=80, value=200, max_value=320)
st.sidebar.write('\n')

st.sidebar.markdown("""
			<p style='text-align:center;\
						color: white; background-color:#c5d04f;'>Please Choose\
			</p>
			""", unsafe_allow_html=True
			)

Work_accident = st.sidebar.radio("Has your employee had a work accident?", ("Yes", "No"))
if Work_accident=="Yes":
    Work_accident=1
else:
    Work_accident=0	
	
promotion_last_5years = st.sidebar.radio("Has your employee been promoted in the past five years?", ("Yes", "No"))
if promotion_last_5years=="Yes":
    promotion_last_5years=1
else:
    promotion_last_5years=0	

st.sidebar.write('\n')

st.sidebar.markdown("""
			<p style='text-align:center;\
						color: white; background-color:#c5d04f;'>Please Enter Values\
			</p>
			""", unsafe_allow_html=True
			)

number_project = st.sidebar.number_input(label="How many projects does he/she take part in?", min_value=1, max_value=10, value=5)
time_spend_company = st.sidebar.number_input("Time Spent in Company", min_value=0, max_value=15, value=5)
st.sidebar.write('\n')

st.sidebar.markdown("""
			<p style='text-align:center;\
						color: white; background-color:#c5d04f;'>Please Select From List\
			</p>
			""", unsafe_allow_html=True
			)


st.sidebar.markdown("""<p style='text-align:left;color:black;font-size:90%;'>Departments</p>""", unsafe_allow_html=True)
st.sidebar.write('\n')
department = st.sidebar.selectbox("Department", ['RandD', 'accounting', 'hr', 'management', 'marketing', 'product_mng',  'sales', 'support', 'technical', 'IT'])
#("Department", ['R&D', 'Accounting', 'Human Resources', 'Management', 'Marketing', 'Production',  'Sales', 'Support Services', 'Technical', 'IT'])
# if "Department"=="R&D":
#     department="RandD"
# elif  "Department"=="Accounting":
# 	department="accounting"
# elif  "Department"=="Human Resources":
# 	department="hr"
# elif  "Department"=="Management":
# 	department="management"
# elif  "Department"=="Marketing":
# 	department="marketing"
# elif  "Department"=="Production":
# 	department="product_mng"
# elif  "Department"=="Sales":
# 	department="sales"
# elif  "Department"=="Support Services":
# 	department="support"
# elif  "Department"=="Technical":
# 	department="technical"
# else:
# 	department="IT"


st.sidebar.markdown("""<p style='text-align:left;color:black;font-size:90%;'>Salary</p>""", unsafe_allow_html=True)
st.sidebar.write('\n')
salary = st.sidebar.selectbox("Salary", ['low', 'medium', 'high'])

#if "Salary"=="Low":
    #salary="low"
#elif  "Salary"=="Moderate":
	#salary="medium"
#else:
	#salary="high"

coll_dict = {'satisfaction_level':satisfaction_level, 'last_evaluation':last_evaluation, 'number_project':number_project, 'average_montly_hours':average_monthly_hours,\
			'time_spend_company':time_spend_company, 'Work_accident':Work_accident, 'promotion_last_5years':promotion_last_5years,'departments': department, 'salary':salary}
columns = ['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours', 'time_spend_company',\
            'departments_RandD', 'departments_accounting', 'departments_hr', 'departments_management', 'departments_marketing',\
			'departments_product_mng', 'departments_sales', 'departments_support', 'departments_technical', 'departments_IT', 'salary_low', 'salary_medium', 'salary_high']

df_coll = pd.DataFrame.from_dict([coll_dict])
user_inputs = pd.get_dummies(df_coll).reindex(columns=columns, fill_value=0)



df_input = pd.DataFrame.from_dict([coll_dict])
scaler= pickle.load(open("scaler.pkl", 'rb'))
user_inputs_dumy = pd.get_dummies(df_input).reindex(columns=columns, fill_value=0)
user_inputs_transformed = scaler.transform(user_inputs_dumy)


loaded_enc = pickle.load(open("encoder.pkl", 'rb'))
new_df = pd.DataFrame(df_input, index=[0])
new_df.salary = new_df.salary.map({"low":1, "medium" : 2, "high" : 3})

cat = new_df.select_dtypes("object").columns
new_df[cat] = loaded_enc.transform(new_df[cat])


selection = st.selectbox("",["Gradient Boost", "Random Forest", "KNN"])

if selection =="Gradient Boost":
	st.markdown("<p style='text-align:center; color:black; font-size:110%; background-color:#F2F3F4 ;'>\
				You selected \
				<span style='color:tomato;font-weight:bold'>\
				'Gradient Boost'\
				</span> model!\
				</p>", unsafe_allow_html=True
				)
	model = pickle.load(open('gradient_boosting_model.pkl', 'rb'))
	prediction= model.predict(new_df)
elif selection =="Random Forest":
	st.markdown("<p style='text-align:center; color:black; font-size:110%; background-color:#F2F3F4 ;'>\
				You selected \
				<span style='color:tomato;font-weight:bold'>\
				'Random Forest'\
				</span> model!\
				</p>", unsafe_allow_html=True
				)
	model = pickle.load(open('rf_grid_model.pkl', 'rb'))
	prediction= model.predict(new_df)

else:
	st.markdown("<p style='text-align:center; color:black; font-size:110%; background-color:#F2F3F4 ;'>\
				You selected \
				<span style='color:tomato;font-weight:bold'>\
				'KNN'\
				</span> model!\
				</p>", unsafe_allow_html=True
				)
	model = pickle.load(open('knn_final_pickle.pkl', 'rb'))
	prediction = model.predict(user_inputs_transformed)



st.markdown("""
			<center>
			<h1 style='font-size:150%;\
						background-color:#c5d04f;\
						border-radius: 10px;\
						color:white;'>You can check the values you entered about your employee\
			</h1>
			</center>
			""", unsafe_allow_html=True
			)

st.write('\n')

st.dataframe(df_coll)

st.markdown("""
			<center>
			<p style='font-size:100%;\
						font-family:courier;\
						background-color:#c5d04f;\
						border-radius: 10px;\
						color:white;'> Click PREDICT if you filled related fields on the left side\
			</p>
			</center>
			""", unsafe_allow_html=True
			)

#agree = st.checkbox(label="Are the values OK?")
#if agree:
	#st.write("Click PREDICT if you filled related fields on the left side")
col1, col2, = st.columns([1, 1.5])
if col2.button("PREDICT"):
	if prediction[0]==0:
		#st.success(prediction[0])
		st.success(f'Congragulations most probably your employee will stay in your company.')
		#st.write(user_inputs)
		#st.balloons()
	elif prediction[0]==1:
		#st.warning(prediction[0])
		st.warning(f'Unfortunately most probably your employee will leave your company.')
		#st.snow()