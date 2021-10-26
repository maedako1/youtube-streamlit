import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Streamlit 超入門")

st.write("Display Image")

img = Image.open("images.png")
st.image(img, caption="sample", use_column_width=True)

# st.write("DataFrame")

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=["lat", "lon"]
# )

# st.dataframe(df.style.highlight_max(axis=0), width=600, height=300)

# st.map(df)



