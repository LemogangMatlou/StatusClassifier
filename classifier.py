import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title='Job Classifier',layout='wide',initial_sidebar_state='auto')
st.subheader("Please answer this questionnaire honestly")

sex = st.number_input("1.Are you Male or female? 1=Male 2=Female",min_value=1, max_value=2, format=None, key=None)
prov = st.number_input('2. Which Province do you live in? 1=WC 2=EC 3=NC 4=FS 5=KZN 6=NW 7=GAT 8=MP 9=LMP', min_value=1, max_value=9, format=None, key=None)
geoType = st.number_input('3. What kind of area do live in? 1=UrbanFormal 2=UrbanInformal 4=TribalAreas 5=RuralFormal', min_value=1, max_value=5, format=None, key=None)
edu_status = st.number_input('4. What is your education status by far? 1=Not Schooling 2=Less than primary completed 3=Primary completed 4=Secondary not completed 5=Secondary completed 6=Tertiary 7=Other', min_value=1, max_value=7, format=None, key=None)
st.markdown('''
0=Other 1=Agriculture or RenewableNaturalResources 2=Architecture or EnvironmentalDesign 3=ArtsVisual or Performing 
4=Business,Commerce and ManagementStudies 5=Communication 6=ComputerScience 7=Education,Training,Development 8=Engineering or EngineeringTechnology 9=HealthCare 
10=HomeEconomics 11=IndustrialArts,Traders or Technology 12=Literature 13=Law 14=Libraries 15=LifeSciences or PhysicalSciences 16=MathematicalSciences 17=MilitarySciences 18=Philosophy 
19=PhysicalEducation 20=Psychology 21=SocialServices 22=SocialSciences 23=Other 24=Management 25=Marketing 26=IT/CS 27=Finance,Economics and Accounting 28=OfficeAdministration 29=Electrical Infrastructure Construction 30=CivilEngineering 
31=Engineering 232=PrimaryAgriculture 33=Hospitality 34=Tourism 35=SafetyInSociety 36=Mechatronics 37=Education And Development 38=Other
''')
edu_field = st.number_input('5. What is your study field?',min_value=1, max_value=38, format=None, key=None)
st.markdown("""
0=GradeR 1=Grade1 2=Grade2 3=Grade3 4=Grade4 5=Grade5 6=Grade6 7=Grade7 8=Grade8 9=Grade9 10=Grade10 11=Grade=11 12=Grade12 13=NTC l/N1/NIC/(v) Level  14=NTC II/N2/NIC/(v) Level3 15=NTC III/N3/NIC/(v) 
Level4 16=N4/NTC 4 17=N5/NTC 5 18=N6/NTC 6 19=Certificate with less than Grade 12/Std 10 
20=Diploma with less than Grade 12/Std 10 21=Certificate with Grade 12/Std 10 22=Diploma with Grade 12/Std 10 23=HigherDiploma 24=PostHigherDiploma 25=BachelorsDegree 26=BachelorsDegree and PostGraduateDiploma 27=HonoursDegree 28=HigherDegree (Masters/Phd) 29=Other 30=idk 98:NoSchooling
""")
edu_lvl = st.number_input('6. What is your education level?',min_value=0, max_value=98,format=None, key=None)
lf_work = st.number_input('7. Are looking for work? 1=Yes 2=No',min_value=1, max_value=2, format=None, key=None)
neet = st.number_input('8. Not in employment, education and training? 0=NA 1=Yes 2=No', min_value=0, max_value=2, format=None, key=None)

submit = st.button('Submit my answers')

if submit:
    user_input = np.array([sex, prov, geoType, edu_status, edu_field,edu_lvl, lf_work, neet])
    pickle_in = open('./KNN-Emp.pickle' , 'rb')
    clf = pickle.load(pickle_in)
    prediction = clf.predict([user_input])
    Categories = ['Not Sure','Employed','Unemployed','Discouraged job seeker','not economically active']
    st.warning('You are likely to be ' + Categories[int(prediction)])
