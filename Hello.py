# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd 
import os
import warnings
warnings.filterwarnings('ignore')



st.set_page_config(page_title="Dashboards", page_icon=":bar_chart:", layout="wide")
st.title(" :bar_chart: Dashboards")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

fl = st.file_uploader(":file_folder: Upload a data file", type=(["csv", "xlsx", "xls"]))

if fl is not None:
    filename = fl.name
    st.write(filename)
    #df = pd.read_excel(filename)
    df = pd.read_excel(io='FamilyOfficeEntityDataSampleV1.1.xlsx',
                      engine='openpyxl',
                       sheet_name='Client Profile' )
    
    #print(df)

    col1, col2 = st.columns((2))
    df["Date of Birth"] = pd.to_datetime(df["Date of Birth"])
    startDate = pd.to_datetime(df["Date of Birth"]).min()
    endDate = pd.to_datetime(df["Date of Birth"]).max()

    with col1:
        date1 = pd.to_datetime(st.date_input("Start Date", startDate))
      
    with col2:
        date2 = pd.to_datetime(st.date_input("End Date", endDate))

#df = df[(df["Date of Birth"] >= date1) & (df["Date of Birth"]) <= date2].copy

