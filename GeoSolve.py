#Import packages
import streamlit as st
import math
from PIL import Image
from streamlit_option_menu import option_menu

#Import logos
logo = Image.open('Images/Logo.png')
logo2 = Image.open('Images/GeoSolve Tools.png')

#Set page configuration
st.set_page_config(page_title='GeoSolve', page_icon=':gear:', layout='wide')

#Define Functions
def Home():
    #Display website title
    st.subheader('Welcome to GeoSolve! :wave:')
    st.title('A Digital Toolbox For Geotechnical Engineers')
    #Space
    st.write('---')
    #Set left and right columns
    left_column, right_column = st.columns(2)
    with left_column:
        #Display mission, vision and goals
        st.header('Mission')
        st.subheader('GeoSolve is dedicated to empowering geotechnical engineers throughout the world by utilizing innovative technologies. Our mission is to provide a comprehensive digital toolkit that improves the efficiency, precision, and creativity of geotechnical engineering methods. Through user-friendly tools and innovative solutions, our aim is to transform the industry, ensuring the development of safer and more sustainable infrastructure worldwide.')
        st.header('Vision')
        st.subheader('GeoSolve strives to be the leading force in advancing geotechnical engineering approaches through its cutting-edge digital toolkit. We envision a future in which geotechnical engineers may use advanced tools, real-time data analysis, and collaboration platforms with ease. Our mission is to redefine the field of geotechnical engineering, making it more intelligent, connected, and capable of responding to future difficulties by cultivating a community of competent professionals and embracing the power of technology.')
        st.header('Goals')
        st.subheader('1. Efficiency: Streamline the process of performing complex geotechnical calculations by automating repetitive tasks and reducing the time required for manual calculations.')
        st.subheader('2. Accuracy: Provide accurate results by implementing standardized and validated geotechnical engineering formulas and methods.')
        st.subheader('3. Accessibility: Make geotechnical calculations accessible to a wide range of users, from experienced professionals to students and entry-level engineers.')
        st.subheader('4. User-Friendly Interface: Create an intuitive and user-friendly interface that enables users to input data easily and interpret results effectively.')
        st.subheader('5. Data Management: Provide features for saving, storing, and retrieving input data and analysis results, facilitating record-keeping and future reference.')
        st.subheader('6. Error Handling: Provide clear and informative error messages to guide users in cases of invalid input or when a calculation is not applicable to the given conditions.')
        st.subheader('7. Educational Tool: Serve as an educational resource, helping students and junior engineers understand and learn geotechnical concepts and calculations.')
        st.subheader('8. Cross-Platform Compatibility: Make the calculator available as a web-based application or mobile app, ensuring that geotechnical professionals can access it in the field or the office.')
        st.subheader('9. Data Export: Allow users to export analysis results and reports in various formats (e.g., PDF, Excel) for inclusion in project documentation.')
        st.subheader('10. Safety and Reliability: Assist in making informed decisions regarding the safety and stability of geotechnical structures and foundations.')
    with right_column:
        #Display tools and tagline
        st.image(logo)
        st.markdown("<h1 style='text-align: center; color: white;'>Precision Beneath Your Fingertips: GeoSolve — Your Online Geotechnical Toolbox</h1>",unsafe_allow_html=True)
        st.write('---')
        st.markdown("<h1 style='text-align: center; color: white;'>What We Offer:</h1>", unsafe_allow_html=True)
        st.image(logo2)

def tool1():
    #Function to calculate bearing capacity
    def calculate_bearing_capacity(c, gamma, Nc, Nq, N_gamma, Ac, Aq, A_gamma):
        settlement = c * Nc * Ac + gamma * Nq * Aq + 0.5 * gamma * N_gamma * A_gamma
        return settlement
    #Display tool title
    st.title('Bearing Capacity (Hansen)')
    #User inputs
    c_hansen = st.number_input("Enter the Cohesion of the Soil (kN/m^2): ", value=0.01)
    gamma_hansen = st.number_input("Enter the Unit Weight of the Soil (kN/m^3): ", value=0.01)
    Nc_hansen = st.number_input("Enter the Bearing Capacity Factor Nc (dimensionless): ", value=0.01)
    Nq_hansen = st.number_input("Enter Bearing Capacity Factor Nq (dimensionless): ", value=0.01)
    N_gamma_hansen = st.number_input("Enter the Bearing Capacity Factor N_gamma (dimensionless): ", value=0.01)
    Ac_hansen = st.number_input("Enter the Shape Factor Ac (dimensionless): ", value=0.01)
    Aq_hansen = st.number_input("Enter the Shape Factor Aq (dimensionless): ", value=0.01)
    A_gamma_hansen = st.number_input("Enter the Shape Factor A_gamma (dimensionless):", value=0.01)
    # Calculate ultimate bearing capacity using the Hansen equation
    settlement_hansen = calculate_bearing_capacity(c_hansen, gamma_hansen, Nc_hansen, Nq_hansen, N_gamma_hansen, Ac_hansen, Aq_hansen, A_gamma_hansen)
    result = str(settlement_hansen)
    result_text = f"Input Values:\nCohesion of the Soil (kN/m^2): {c_hansen}\nUnit Weight of the Soil (kN/m^3): {gamma_hansen}\nBearing Capacity Factor Nc (dimensionless): {Nc_hansen}\nBearing Capacity Factor Nq (dimensionless): {Nq_hansen}\nBearing Capacity Factor N_gamma (dimensionless): {N_gamma_hansen}\nShape Factor Ac (dimensionless): {Ac_hansen}\nShape Factor Aq (dimensionless): {Aq_hansen}\nShape Factor A_gamma (dimensionless): {A_gamma_hansen}\n\nBearing Capacity: {result}"
    #Display the result
    if st.button('Calculate'):
        st.write("Bearing Capacity: ", result)
    #Downlaod the result
    st.download_button(label='Download Result',data=result_text,file_name='Result.txt')

def tool2():
    # Function to calculate bearing capacity
    def calculate_bearing_capacity(c, Nc, Nq, A, gamma, Df, B, L):
        settlement = c * Nc * A + gamma * Nq * Df * B * L
        return settlement
    #Display tool title.
    st.title('Bearing Capacity (Meyerhof)')
    #User inputs
    c_meyerhof = st.number_input("Enter the Cohesion of the Soil (kN/m^2) (usually 0 for cohesionless soils): ",value=0.01)
    Nc_meyerhof = st.number_input("Enter the Bearing Capacity Factor Nc (dimensionless): ", value=0.01)
    Nq_meyerhof = st.number_input("Enter the Bearing Capacity Factor Nq (dimensionless): ", value=0.01)
    A_meyerhof = st.number_input("Enter the Area of the Foundation (square meters): ", value=0.01)
    gamma_meyerhof = st.number_input("Enter the Unit Weight of the Soil (kN/m^3): ", value=0.01)
    Df_meyerhof = st.number_input("Enter the Depth of the Foundation (meters): ", value=0.01)
    B_meyerhof = st.number_input("Enter the Width of the Foundation (meters): ", value=0.01)
    L_meyerhof = st.number_input("Enter the Length of the Foundation (meters): ", value=0.01)
    #Calculate ultimate bearing capacity using the Meyerhof equation
    settlement_meyerhof = calculate_bearing_capacity(c_meyerhof, Nc_meyerhof, Nq_meyerhof, A_meyerhof, gamma_meyerhof, Df_meyerhof, B_meyerhof, L_meyerhof)
    result = str(settlement_meyerhof)
    result_text = f"Input values:\nCohesion of the Soil (kN/m^2) (usually 0 for cohesionless soils): {c_meyerhof}\nBearing Capacity Factor Nc (dimensionless): {Nc_meyerhof}\nEnter the Bearing Capacity Factor Nq (dimensionless): {Nq_meyerhof}\nArea of the Foundation (square meters): {A_meyerhof}\nUnit Weight of the Soil (kN/m^3): {gamma_meyerhof}\nDepth of the Foundation (meters): {Df_meyerhof}\nWidth of the Foundation (meters): {B_meyerhof}\nLength of the Foundation (meters): {L_meyerhof}\n\nBearing capacity: {result}"
    #Display the result
    if st.button('Calculate'):
        st.write("Bearing capacity:", result)
    #Download the result
    st.download_button(label='Download Result', data=result_text, file_name='Result.txt')

def tool3():
    #Function to calculate settlement
    def calculate_settlement(q, e, B, sigma_v, sigma_vc):
        settlement = (q / (1 + e)) * B * (1 - sigma_v / sigma_vc)
        return settlement
    def calculate_bearing_capacity(c, Nc, Nq, A, gamma, Df, B, L):
        settlement = c * Nc * A + gamma * Nq * Df * B * L
        return settlement
    #Display tool title.
    st.title('Bearing Capacity (Terzaghi)')
    #User inputs
    q_terzaghi = st.number_input("Enter the Applied Load on the Foundation (kN/m^2): ", value=0.01)
    e_terzaghi = st.number_input("Enter the  Void Ratio of the Soil: ", value=0.01)
    B_terzaghi = st.number_input("Enter the Width of the Foundation (meters): ", value=0.01)
    sigma_v = st.number_input("Enter the Effective Vertical Stress at Depth (kN/m^2): ", value=0.01)
    sigma_vc = st.number_input("Enter the Critical Effective Vertical Stress of the Soil (kN/m^2): ", value=0.01)
    #Calculate settlement using Terzaghi's equation.
    settlement_terzaghi = calculate_settlement(q_terzaghi, e_terzaghi, B_terzaghi, sigma_v, sigma_vc)
    result = str(settlement_terzaghi)
    result_text =f"Input values:\nApplied Load on the Foundation (kN/m^2): {q_terzaghi}\nVoid Ratio of the Soil: {e_terzaghi}\nWidth of the Foundation (meters): {B_terzaghi}\nEffective Vertical Stress at Depth (kN/m^2): {sigma_v}\nCritical Effective Vertical Stress of the Soil (kN/m^2): {sigma_vc}\n\nBearing capacity: {result}"
    #Display the result
    if st.button('Calculate'):
        st.write("Bearing capacity: ", result)
    #Download the result
    st.download_button(label='Download Result', data=result_text, file_name='Result.txt')

def tool4():
    #Function to classify soil.
    def classify_soil(gravel, sand, fine, cc, cu):
        if gravel < sand:
            if fine <= 5:
                if cu > 6 and 1 < cc < 3:
                    return 'Well-graded sand (SW)'
                else:
                    return 'Poorly-graded sand (SP)'
            elif 5 < fine <= 12:
                if cu > 6 and 1 < cc < 3:
                    return 'Dual Classification: Well-graded sand with silt (SW-SM) or Well-graded sand with clay (SW-SC)'
                else:
                    return 'Dual Classification: Poorly-graded sand with silt (SP-SM) or Poorly-graded sand with clay (SP-SC)'
            else:
                return 'Error. Fines should be 0% - 12%'
        elif gravel > sand:
            if fine <= 5:
                if cu > 4 and 1 < cc < 3:
                    return 'Well-graded gravel (GW)'
                else:
                    return 'Poorly-graded gravel (GP)'
            elif 5 < fine <= 12:
                if cu > 4 and 1 < cc < 3:
                    return 'Dual Classification: Well-graded gravel with silt (GW-GM) or Well-graded gravel with clay (GW-GC)'
                else:
                    return 'Dual Classification: Poorly-graded gravel with silt (GP-GM) or Poorly-graded gravel with clay (GP-GC)'
            else:
                return 'Error. Fines should be 0% - 12%'
        else:
            return 'Cannot classify.'
    #Display tool title.
    st.title('Soil Classification (Nonplastic Soil)')
    #User inputs
    gravel1 = st.number_input('Enter Quantity of Gravel (%): ')
    sand1 = st.number_input('Enter Quantity of Sand (%): ')
    fine1 = st.number_input('Enter Quantity of Fines (%): ')
    cc1 = st.number_input('Enter Coefficient of Curvature: ')
    cu1 = st.number_input('Enter Coefficient of Uniformity: ')
    # Calculate soil classification
    result_classification = classify_soil(gravel1, sand1, fine1, cc1, cu1)
    input_result_text_classification = f"Input values:\nQuantity of Gravel: {gravel1}%\nQuantity of Sand: {sand1}%\nQuantity of Fines: {fine1}%\nCoefficient of Curvature: {cc1}\nCoefficient of Uniformity: {cu1}\n\nSoil Classification: {result_classification}"
    #Display the result
    if st.button('Classify'):
        st.write('Soil Classification:', result_classification)
    #Download the result
    st.download_button(label='Download Result',data=input_result_text_classification,file_name='Result.txt')

def tool5():
    #Function to classify soil
    def classify_plastic_soil(gravel, sand, fine, ll, pl):
        #Compute Plastic Index
        pi = ll - pl

        if gravel < sand:
            if fine <= 5 or (5 < fine <= 12):
                return 'Error. Fines should be 13% - 50%'
            else:
                if pi > 0.73 * (ll - 20):
                    return 'Clayey Sand (SC)'
                else:
                    return 'Silty Sand (SM)'
        elif gravel > sand:
            if fine <= 5 or (5 < fine <= 12):
                return 'Error. Fines should be 13% - 50%'
            else:
                if pi > 0.73 * (ll - 20):
                    return 'Clayey Gravel (GC)'
                else:
                    return 'Silty Gravel (GM)'
        else:
            return 'Cannot classify.'
    #Display tool title
    st.title('Soil Classification (Plastic Soil)')
    #User inputs
    gravel1 = st.number_input('Enter Quantity of Gravel (%): ')
    sand1 = st.number_input('Enter Quantity of Sand (%): ')
    fine1 = st.number_input('Enter Quantity of Fines (%): ')
    ll1 = st.number_input('Enter Liquid Limit: ')
    pl1 = st.number_input('Enter Plastic Limit: ')
    #Classify plastic soil
    result_classification_plastic_soil = classify_plastic_soil(gravel1, sand1, fine1, ll1, pl1)
    input_result_text_classification_plastic_soil = f"Input values:\nQuantity of Gravel: {gravel1}%\nQuantity of Sand: {sand1}%\nQuantity of Fines: {fine1}%\nLiquid Limit: {ll1}\nPlastic Limit: {pl1}\n\nSoil Classification: {result_classification_plastic_soil}"
    #Display the result
    if st.button('Classify'):
        st.write('Soil Classification:', result_classification_plastic_soil)
    #Download the result
    st.download_button(label='Download Result', data=input_result_text_classification_plastic_soil, file_name='Result.txt')

def tool6():
    #Function to calculate settlement
    def calculate_settlement(q, dr, br, ec, em, ips, a):
        diameter_rock = ips / (br * em)
        socket_concrete = dr / (a * ec)
        settlement_displacement_rock = q * (diameter_rock + socket_concrete)
        return settlement_displacement_rock
    #Display tool title
    st.title('Settlement Analysis')
    #User inputs
    q = st.number_input("Enter the Total Axial Compression Load Applied to Shaft Butt (MN):", value=0.01)
    dr = st.number_input("Enter the Length of Socket (m):", value=0.01)
    br = st.number_input("Enter the Socket Diameter (m):", value=0.01)
    ec = st.number_input("Enter the Elastic Modulus of Concrete Shaft or Reinforced Shaft (MPa):", value=0.01)
    em = st.number_input("Enter the Elastic Modulus of Rock Mass (MPa):", value=0.01)
    ips = st.number_input("Enter the Displacement Influence Factor for Rock-Socket Shafts Loaded in Compression: ",value=0.01)
    a = st.number_input("Enter the Socket Area:", value=0.01)
    #Calculate settlement
    settlement_displacement_rock = calculate_settlement(q, dr, br, ec, em, ips, a)
    result = str(settlement_displacement_rock)
    result_text = f"Input values:\nTotal Axial Compression Load Applied to Shaft Butt (MN): {q} MN\nLength of Socket (m): {dr} m\nSocket Diameter (m): {br} m\nElastic Modulus of Concrete Shaft or Reinforced Shaft (MPa): {ec} MPa\nElastic Modulus of Rock Mass (MPa): {em} MPa\nDisplacement Influence Factor for Rock-Socket Shafts Loaded in Compression: {ips}\nSocket Area: {a}\n\nImmediate Settlement Analysis of Pile Foundations in Rock: {result}"
    #Display result
    if st.button('Calculate'):
        st.write("Immediate Settlement Analysis of Pile Foundations in Rock: ", result)
    #Download result
    st.download_button(label='Download Result', data=result_text, file_name='Result.txt')


def tool7():
    #Function to calculate slope stability
    def calculate_slope_stability(cohesion, friction_angle, unit_weight, height, slope_angle_deg, height_slice):
        #Convert slope angle to radians
        slope_angle_rad = math.radians(slope_angle_deg)

        #Calculate driving force for Bishop Method
        driving_force = unit_weight * height * math.cos(slope_angle_rad)
        #Calculate resisting force
        resisting_force = cohesion * height + unit_weight * height * math.sin(slope_angle_rad) * math.cos(
            math.radians(friction_angle))
        #Calculate the Factor of Safety (FS) using the Bishop method
        FS_Bishop = resisting_force / driving_force

        #Calculate the normal and shear forces on the slice
        normal_force = height_slice * unit_weight
        shear_force = normal_force * math.tan(math.radians(friction_angle))
        #Calculate the driving force for Ordinary Method of Slices
        driving_force_ordinary = shear_force * math.cos(slope_angle_rad)
        #Update the total resisting force
        total_resisting_force = shear_force * math.sin(slope_angle_rad)
        #Calculate the Factor of Safety using the Ordinary Method of Slices
        FS_ordinary = total_resisting_force / (cohesion * height * unit_weight * math.cos(slope_angle_rad))

        return FS_Bishop, FS_ordinary
    #Display tool title
    st.title('Slope Stability')
    #User inputs
    cohesion = st.number_input("Enter cohesion in kPa: ", value=0.01)
    friction_angle = st.number_input("Enter friction angle in degrees: ", value=0.01)
    unit_weight = st.number_input("Enter unit weight in kN/m^3: ", value=0.01)
    height = st.number_input("Enter height in meters: ", value=0.01)
    slope_angle_deg = st.number_input("Enter slope angle in degrees: ", value=0.01)
    height_slice = st.number_input("Enter height of each slice in meters: ", value=0.01)
    #Calculate slope stability
    result_FS_Bishop, result_FS_ordinary = calculate_slope_stability(cohesion, friction_angle, unit_weight, height, slope_angle_deg, height_slice)
    input_result_text_slope_stability = f"Input values:\nCohesion: {cohesion} kPa\nFriction Angle: {friction_angle} degrees\nUnit Weight: {unit_weight} kN/m^3\nHeight: {height} meters\nSlope Angle: {slope_angle_deg} degrees\nHeight of Each Slice: {height_slice} meters\n\nFactor of Safety Using Bishop Method: {result_FS_Bishop}\nFactor of Safety Using Ordinary Method of Slices: {result_FS_ordinary}"
    #Display the results
    if st.button('Calculate'):
        st.write("Factor of Safety Using Bishop Method:", str(result_FS_Bishop))
        st.write("Factor of Safety Using Ordinary Method of Slices:", str(result_FS_ordinary))
        #Compare the two methods
        if result_FS_Bishop > result_FS_ordinary:
            st.write("Bishop Method has a higher Factor of Safety.")
        elif result_FS_Bishop < result_FS_ordinary:
            st.write("Ordinary Method of Slices has a higher Factor of Safety.")
        else:
            st.write("Both methods have the same Factor of Safety.")
    #Download the results
    st.download_button(label='Download Result', data=input_result_text_slope_stability, file_name='Result.txt')

def Rate_Us():
    st.title('Tell Us Your Experience :sparkles:')
    rating = st.slider('', 1, 5)
    if st.button('Submit'):
        st.write('Your review was submitted. Thank you very much!')

#Set sidebar
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=['Home', 'Bearing Capacity (Hansen)', 'Bearing Capacity (Meyerhof)', 'Bearing Capacity (Terzaghi)', 'Nonplastic Soil Classification', 'Plastic Soil Classification', 'Settlement Analysis', 'Slope Stability'],
        icons=['house', 'gear', 'gear', 'gear', 'gear', 'gear', 'gear', 'gear'])
    st.sidebar.title('FAQs')
    st.subheader('1. What is Geosolve, and what does it offer?')
    st.write(
        'GeoSolve is a digital toolbox designed to provide geotechnical engineers with a comprehensive set of tools and resources for their projects. It offers a variety of geotechnical solutions, calculations, and support materials.')
    st.subheader('2. What types of calculations and solutions are available on GeoSolve?')
    st.write(
        'GeoSolve offers a wide array of calculations, including soil bearing capacity, settlement analysis, and slope stability analysis.')
    st.subheader('3. Is GeoSolve suitable for both beginners and experienced geotechnical engineers?')
    st.write(
        'Yes, GeoSolve is designed to be accessible and valuable for engineers at any skill level. It provides tools and resources that cater to both beginners looking for guidance and experienced professionals seeking efficient solutions.')
    st.subheader('4. How can Geosolve benefit geotechnical engineers')
    st.write(
        'GeoSolve simplifies complex geotechnical calculations and analyses, saving time and reducing the potential for errors. It provides a user-friendly platform to access a variety of tools and resources, making geotechnical work more efficient and accurate.')
    st.subheader('5. Is GeoSolve easy to navigate and user-friendly')
    st.write(
        'Yes, GeoSolve is designed with a user-friendly interface and intuitive navigation. The tools and resources are organized to ensure ease of use and quick access to the necessary calculations and information.')
    st.subheader('6. Are the results obtained from GeoSolve accurate and reliable for professional use?')
    st.write(
        'Yes, GeoSolve provides accurate results based on established geotechnical engineering principles and formulas. It is a trustworthy resource for geotechnical professionals, but it is important to verify and validate results in accordance with site-specific conditions.')
    st.sidebar.title('Get In Touch With Us! :envelope:')
    st.sidebar.text_input('Your Name')
    st.sidebar.text_input('Your Email')
    st.sidebar.text_input('Your Message')
    if st.sidebar.button('Send'):
        st.sidebar.write('Your message was sent.')
    Rate_Us()
    st.sidebar.title('Contact Us!')
    st.subheader(':envelope: GeoSolve.tech@gmail.com')
    st.subheader(':telephone_receiver: +639876543210')
    st.subheader(':phone: 412-3456')
    st.subheader(':globe_with_meridians: GeoSolve')
#Determine conditions
if selected == 'Home':
    Home()
elif selected == 'Bearing Capacity (Hansen)':
    tool1()
elif selected =='Bearing Capacity (Meyerhof)':
    tool2()
elif selected == 'Bearing Capacity (Terzaghi)':
    tool3()
elif selected =='Nonplastic Soil Classification':
    tool4()
elif selected == 'Plastic Soil Classification':
    tool5()
elif selected == 'Settlement Analysis':
    tool6()
elif selected == 'Slope Stability':
    tool7()
