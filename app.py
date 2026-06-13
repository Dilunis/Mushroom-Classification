import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os

#load Model & Encoder  
model = joblib.load("Mushroom_prediction.pkl")
pca = joblib.load("pca_model.pkl")
encoders = joblib.load("encoders.pkl")

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>🍄 Mushroom Edibility Predictor</h1>", unsafe_allow_html=True)

#show the Structure image  
if os.path.exists("structure.png"):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("structure.png", caption="Detailed Structure and Parts of a Mushroom")

st.markdown("---")

# Feature Configuration (include images and tips)
feature_config = {
    "CAP DETAILS": {
        'cap-shape': {'img': 'cap_shape.png', 'tip': 'b=bell, c=conical, x=convex, f=flat, k=knobbed, s=sunken'},
        'cap-surface': {'img': 'cap_surface.png', 'tip': 'f=fibrous, g=grooves, y=scaly, s=smooth'},
        'cap-color': {'img': None, 'tip': 'n=brown, b=buff, c=cinnamon, g=gray, r=green, p=pink, u=purple, e=red, w=white, y=yellow'}
    },
    "GILL DETAILS": {
        'gill-attachment': {'img': 'gill_sttachment.jpeg', 'tip': 'a=attached, d=descending, f=free, n=notched'},
        'gill-spacing': {'img': None, 'tip': 'c=close, w=crowded, d=distant'},
        'gill-size': {'img': None, 'tip': 'b=broad, n=narrow'},
        'gill-color': {'img': None, 'tip': 'k=black, n=brown, b=buff, h=chocolate, g=gray, r=green, o=orange, p=pink, u=purple, e=red, w=white, y=yellow'}
    },
    "STALK DETAILS": {
        'stalk-shape': {'img': 'stalk_shape.png', 'tip': 'e=enlarging, t=tapering'},
        'stalk-root': {'img': None, 'tip': 'b=bulbous, c=club, u=cup, e=equal, z=rhizomorphs, r=rooted, ?=missing'},
        'stalk-surface-above-ring': {'img': None, 'tip': 'f=fibrous, y=scaly, k=silky, s=smooth'},
        'stalk-surface-below-ring': {'img': None, 'tip': 'f=fibrous, y=scaly, k=silky, s=smooth'},
        'stalk-color-above-ring': {'img': None, 'tip': 'n=brown, b=buff, c=cinnamon, g=gray, o=orange, p=pink, e=red, w=white, y=yellow'},
        'stalk-color-below-ring': {'img': None, 'tip': 'n=brown, b=buff, c=cinnamon, g=gray, o=orange, p=pink, e=red, w=white, y=yellow'}
    },
    "OTHER DETAILS": {
        'bruises': {'img': None, 'tip': 't=bruises, f=no'},
        'odor': {'img': None, 'tip': 'a=almond, l=anise, c=creosote, y=fishy, f=foul, m=musty, n=none, p=pungent, s=spicy'},
        'veil-type': {'img': 'veil_type.png', 'tip': 'p=partial, u=universal'},
        'veil-color': {'img': None, 'tip': 'n=brown, o=orange, w=white, y=yellow'},
        'ring-number': {'img': None, 'tip': 'n=none, o=one, t=two'},
        'ring-type': {'img': 'ring_type.jpeg', 'tip': 'c=cobwebby, e=evanescent, f=flaring, l=large, n=none, p=pendant, s=sheathing, z=zone'},
        'spore-print-color': {'img': 'spore_color.jpeg', 'tip': 'k=black, n=brown, b=buff, h=chocolate, r=green, o=orange, u=purple, w=white, y=yellow'},
        'population': {'img': None, 'tip': 'a=abundant, c=clustered, n=numerous, s=scattered, v=several, y=solitary'},
        'habitat': {'img': None, 'tip': 'g=grasses, l=leaves, m=meadows, p=paths, u=urban, w=waste, d=woods'}
    }
}

input_data = {}

# UI Generation
for group_name, features in feature_config.items():
    with st.expander(f"📦 {group_name}", expanded=True):
        for col, data in features.items():
            if col in encoders:
                c1, c2 = st.columns([1, 2])
                with c1:
                    if data['img'] and os.path.exists(data['img']):
                        st.image(data['img'], use_container_width=True)
                with c2:
                    st.caption(f"ℹ️ {data['tip']}")
                    input_data[col] = st.selectbox(f"Select {col.replace('-', ' ').upper()}:", encoders[col].classes_, key=col)
                st.markdown("---")

# Prediction
if st.button("Predict Mushroom Edibility", type="primary", use_container_width=True):
    ordered_keys = [k for k in encoders.keys() if k != 'class']
    try:
        encoded_vals = [encoders[col].transform([input_data[col]])[0] for col in ordered_keys]
        prediction = model.predict(pca.transform(np.array(encoded_vals).reshape(1, -1)))
        
        if prediction[0] == 1:
            st.error("### Result: The Mushroom is Poisonous! ☠️")
        else:
            st.success("### Result: The Mushroom is Edible! 🍽️")
    except Exception as e:
        st.error(f"Error: {e}")