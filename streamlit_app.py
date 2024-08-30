import streamlit as st
import math

# Title of the app
st.title("Reinforced Concrete Design (Eurocode 2)")

# Input section
st.header("Input Parameters")

# Section dimensions
width = st.number_input("Width (m)", min_value=0, format="%d", value=1000)
height = st.number_input("Height (m)", min_value=0, format="%d", value=1200)

# Rebar arrangement
st.subheader("Rebar Arrangement")
cover = st.number_input("Cover (mm)", min_value=0, format="%d", value=65)
s12 = st.number_input("Distance between 2 layers", min_value=0, format="%d", value=70)

st.subheader("Layer 1")
n1 = st.number_input("Number of rebars in Layer 1", min_value=0, format="%d", value=6)
d1 = st.number_input("Diameter of rebars in Layer 1 (mm)", min_value=0, format="%d", value=20)

st.subheader("Layer 2")
n2 = st.number_input("Number of rebars in Layer 2", min_value=0, format="%d", value=2)
d2 = st.number_input("Diameter of rebars in Layer 2 (mm)", min_value=0, format="%d", value=20)

st.subheader("Shear Link")
dlink = st.number_input("Diameter of shear link", min_value=0, format="%d", value=16)


# Material properties
st.subheader("Material Properties")
fck = st.number_input("Concrete strength (fck) (MPa)", min_value=0.0, format="%.1f", value=35.0)
fyk = st.number_input("Steel yield strength (fyk) (MPa)", min_value=0.0, format="%.1f", value=500.0)

# Internal force
st.subheader("Internal Force")
M = st.number_input("Bending moment (kN.m)", min_value=0.0, format="%.2f", value=1000.0)

if st.button("Calculate"):
    # Calculation section


    # Placeholder for calculations
    as_required = 0.0  # Placeholder for required reinforcement area
    as_provided = 0.0  # Placeholder for provided reinforcement area
    utilization = 0.0  # Placeholder for utilization ratio
    conclusion = "Not OK"  # Placeholder for conclusion

    b = width
    h = height
    A = b * h  # Cross-sectional area
    y1 = cover + dlink + d1 / 2
    y2 = y1 + s12
    As1 = math.pi * (d1 / 2)**2 * n1  # Area of steel in Layer 1
    As2 = math.pi * (d2 / 2)**2 * n2  # Area of steel in Layer 2
    As = As1 + As2  # Total area of steel
    y = (y1 * As1 + y2 * As2) / (As1 + As2)
    d = h - y  # Effective depth


    alpha_cc = 0.85  # Partial safety factor for concrete
    gamma_c = 1.5  # Partial safety factor for concrete
    fcd = alpha_cc * fck / gamma_c  # Design concrete strength
    Ec = 22000 * math.sqrt(fck)  # Modulus of elasticity of concrete
    alpha_e = 1  # Factor for calculating effective modulus of elasticity
    Es = 200000  # Modulus of elasticity of steel
    Ecd = Ec / alpha_e  # Effective modulus of elasticity of concrete

    # Steel Properties


    gamma_s = 1.15  # Partial safety factor for steel
    fyd = fyk / gamma_s  # Design steel strength

    # Perform calculations (dummy example)
    K = M * 1000000 / (b * d * d * fck)
    z = min(d / 2 * (1 + (1 - 3.53 * K)), 0.95 * d)
    as_required = M  * 1000000 / (fyd * z)
    as_provided = As
    utilization = as_required / as_provided
    conclusion = "OK" if utilization <= 1 else "Not OK"
    # Display results
    st.header("Calculation")
    st.write(f"The value of the design compressive strength fcd: {fcd:.2f} MPa")
    st.write(f"Design yield strength of reinforcement fyd: {fyd:.2f} MPa") 
    st.write(f"Distance from tension fiber to centroid of tension bars y: {y:.2f} mm")
    st.write(f"Effective depth d: {d:.2f} mm")
    st.write(f"Lever arm of internal forces z: {z:.2f} mm")
    st.write(f"K: {K:.3f} ")
    
    st.header("Results")
    if utilization > 1:
        st.write(f"As required: {as_required:.2f} mm²")
        st.write(f"As provided: {as_provided:.2f} mm²")
        st.error(f"Utilization: {utilization:.2%}")
        st.error(f"Conclusion: {conclusion}")   
    else:
        st.write(f"As required: {as_required:.2f} mm²")
        st.write(f"As provided: {as_provided:.2f} mm²")
        st.success(f"Utilization: {utilization:.2%}")
        st.success(f"Conclusion: {conclusion}")    
