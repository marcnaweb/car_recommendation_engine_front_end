import streamlit as st

st.title("Preprocessing Data")

st.code(
"""     import pandas as pd
    import numpy as np

    data = pd.read_csv('raw_data/car_files_4c_en.csv')
    df = data.copy()
    df.head()""",
        language='python')

st.markdown("""<div style="overflow-x: auto;">
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0.1</th>
      <th>Unnamed: 0</th>
      <th>Hot air</th>
      <th>Volumetric anti -first alarm</th>
      <th>Harman Kardon Sound System</th>
      <th>Track change alert</th>
      <th>Carbonaceramic brake disc</th>
      <th>Arconditional Zones 2</th>
      <th>Reclinarinar rear seat</th>
      <th>Maximum rotation</th>
      <th>...</th>
      <th>Folding rear seat</th>
      <th>Free wheel</th>
      <th>Shaker Pro Audio Sound System</th>
      <th>Maximum speed electric mode</th>
      <th>Electronic noise cancellation</th>
      <th>Steering wheel adjustment in depth</th>
      <th>Facial recognition camera</th>
      <th>Carcode</th>
      <th>Perimeter anti theft alarm</th>
      <th>Track centralization assistant</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 291 columns</p>
</div>
            """,unsafe_allow_html=True)
st.markdown("""<h2 style="font-size: 24px;">Too many features with NaN's,
            remove columns which have more than 15000 NaN's in a column</h2>""",
            unsafe_allow_html=True)
st.code("""
        # Rename Carcode column to car_code (we have another df, it should have same name)
df.rename(columns={'Carcode': 'car_code'}, inplace=True)
# Set car_code as index
df.set_index('car_code', inplace=True)

filtered_columns = df.columns[df.isna().sum() < 15000]
filtered_df = df[filtered_columns]""",language='python')
st.markdown("""<h2 style="font-size: 24px;">Check how much % is NaN in every column and check Dtype</h2>""",
            unsafe_allow_html=True)
st.code("""
        nan_percentage_per_column = test_filtered_df.isnull().mean() * 100

# Create a new DataFrame with column names and NaN percentages and Dtypes
nan_info_df = pd.DataFrame({
    'Column Name': nan_percentage_per_column.index,
    'NaN Percentage': nan_percentage_per_column.values,
    'Data Type': test_filtered_df.dtypes
})

# Display the new DataFrame
nan_info_df""",language='python')
st.markdown("""
            <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Column Name</th>
      <th>NaN Percentage</th>
      <th>Data Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Unnamed: 0.1</th>
      <td>Unnamed: 0.1</td>
      <td>0.000000</td>
      <td>int64</td>
    </tr>
    <tr>
      <th>Hot air</th>
      <td>Hot air</td>
      <td>46.233340</td>
      <td>object</td>
    </tr>
    <tr>
      <th>Acceleration</th>
      <td>Acceleration</td>
      <td>0.000000</td>
      <td>object</td>
    </tr>
    <tr>
      <th>Length</th>
      <td>Length</td>
      <td>0.000000</td>
      <td>object</td>
    </tr>
    <tr>
      <th>Maximum torque</th>
      <td>Maximum torque</td>
      <td>0.709871</td>
      <td>object</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Platform</th>
      <td>Platform</td>
      <td>42.944756</td>
      <td>object</td>
    </tr>
    <tr>
      <th>Year</th>
      <td>Year</td>
      <td>0.125555</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Radio</th>
      <td>Radio</td>
      <td>49.565385</td>
      <td>object</td>
    </tr>
    <tr>
      <th>Folding rear seat</th>
      <td>Folding rear seat</td>
      <td>52.796021</td>
      <td>object</td>
    </tr>
    <tr>
      <th>Perimeter anti theft alarm</th>
      <td>Perimeter anti theft alarm</td>
      <td>56.475758</td>
      <td>object</td>
    </tr>
  </tbody>
</table>
<p>98 rows × 3 columns</p>
</div>""",unsafe_allow_html=True)
st.markdown("""
            <h2 style="font-size: 24px;">After analysing all features,
            decided to remove some of them.</h2>""",unsafe_allow_html=True)
st.markdown("Neither they don't give information, or they are hard to preprocess.")
st.code("""
        column_to_remove = ['Unnamed: 0.1','Assistance','Aspiration', 'Rear tires', 'Spare tire', 'Front tires', 'Tuching',
                    'Urban autonomy', 'Generation', 'Front suspension', 'Rear suspension', 'Coupling', 'Valve command',
                    'Places', 'Disposition', 'Cylinders', 'Elastic element', 'Ipva R', 'Frontal area A', 'Engine code',
                    'Traction', 'Installation', 'Road autonomy', 'Engine power supply', 'Engine control activation',
                    'Gear change code', 'Corrected frontal area', 'Platform']""",
                    language='python')
st.code("""
        new_filtered_df = test_filtered_df.drop(columns=column_to_remove)
len(new_filtered_df.columns)""",
                    language='python')
st.markdown("70")
st.markdown("""<h2 style="font-size: 24px;">Preprocessing Features</h2>""",
            unsafe_allow_html=True)
st.markdown("""<h3 style="font-size: 21px;">Preprocessing All features with [Nan, standart equipment, optinal equipment]</h3>""",
            unsafe_allow_html=True)
st.code("""
        preprocessing_df = new_filtered_df.copy()

columns_to_transform = ['Hot air', 'Rev counter', 'Assisted direction', 'ABS brakes', 'Rear window', 'Central locking of the doors',
                        'Headrest for all occupants', 'Electric rearview mirror adjustment', 'Air conditioning',
                        'Bluetooth connection', 'Frontal Airbags', 'Steering wheel adjustment height',
                        'Electric front window control', 'Multifunctional steering wheel', 'Driver s seat with height adjustment',
                        'On board computer', 'Light in the trunk', 'Alloy wheels', 'USB connection', 'Radio',
                        'Folding rear seat', 'Perimeter anti theft alarm', 'Cooling liquid thermometer']

# Replace NaN with 0 and other values with 1
preprocessing_df[columns_to_transform] = preprocessing_df[columns_to_transform].applymap(lambda x: 0 if pd.isnull(x) else 1)""",
                    language='python')
st.markdown("""<h2 style="font-size: 24px;">Preprocessing [Acceleration]</h2>""",
            unsafe_allow_html=True)
st.code("""
        # Preprocess Acceleration (0100 km/h 3,8 s = 3.8(From string to Float))
preprocessing_df['Acceleration'] = preprocessing_df['Acceleration'].str.extract(r'(\d+\,\d+)')

# Replace ',' with '.' and convert to float
preprocessing_df['Acceleration'] = preprocessing_df['Acceleration'].str.replace(',', '.').astype(float)
# Rename Column
preprocessing_df = preprocessing_df.rename(columns={'Acceleration': 'Acceleration 0100 km/h in S'})""",
                    language='python')
st.markdown("""<h2 style="font-size: 24px;">Preprocessing, Transform all strings to float</h2>""",
            unsafe_allow_html=True)
st.code("""
        def extract_float_value(value):
    try:
        if isinstance(value, float):
            return value
        else:
            float_value = value.split()[0].replace(',', '.')
            return float(float_value)
    except (ValueError, IndexError):
        return np.nan

for column in preprocessing_df[['Weight/Torque', 'Weight', 'Weight/power', 'Max power regime.', 'Cylinder diameter',
                      'Fuel tank', 'Specific power', 'Maximum power', 'Length', 'Maximum torque', 'Width', 'Height',
                      'Specific torque', 'Minimum height from the ground', 'Piston course', 'Front gauge', 'Displacement',
                      'Turns diameter', 'Rear gauge', 'Length between the axis', 'Maximum speed', 'Road consumption',
                      'Max torque regime', 'Car payload', 'Sidewall height', 'Unit displacement', 'Trunk', 'Urban',
                      'Guarantee', 'Reader score', 'Compression ratio', 'Drag coefficient', 'Price R', 'Devaluation',
                      'CNW Index']]:
    preprocessing_df[column] = preprocessing_df[column].apply(extract_float_value)""",
                    language='python')
st.markdown("""<h2 style="font-size: 24px;">Rename some columns, to be more readable</h2>""",
            unsafe_allow_html=True)
st.code("""
       # Rename columns
preprocessing_df = preprocessing_df.rename(columns={'Length': 'Length mm',
                                                    'Width': 'Width mm',
                                                    'Maximum torque': 'Maximum torque kgfm'})""",
                                                    language='python')
st.markdown("""<h2 style="font-size: 24px;">Creating Pipeline</h2>""",
            unsafe_allow_html=True)
st.code("""
        from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import make_column_selector
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import FunctionTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler""",
language='python')
st.code("""
        def binarize_column(column):
    binarizer = LabelBinarizer()
    return binarizer.fit_transform(column)
    columns_to_encode = ['Propulsion', 'Car gearbox', 'Fuel', 'Settings', 'Car size']

numeric_columns = preprocessing_df.select_dtypes(include=['number'])

numeric_column_names = numeric_columns.columns.tolist()
len(numeric_column_names)""",language='python')
st.code("""
        # pipelne for whole df

pipeline = Pipeline([
    ('preprocessor', ColumnTransformer([
        ('onehot', OneHotEncoder(), columns_to_encode),  # Apply one-hot encoding to specified columns
        ('binarize', FunctionTransformer(binarize_column, validate=False), ['Provenance']),  # Binarize the binary column
        ('imputer', SimpleImputer(strategy='median'), numeric_column_names),  # Impute missing values
    ], remainder='passthrough')),
    ('scaler', MinMaxScaler())
])
pipeline""",language='python')
st.markdown("""
            """,unsafe_allow_html=True)
st.code("""
        testing_pipe_df = preprocessing_df.copy()

testing_pipe_df_end = pipeline.fit_transform(testing_pipe_df)

# Get the names of the transformed features after one-hot encoding
encoded_feature_names = pipeline.named_steps['preprocessor'].named_transformers_['onehot'].get_feature_names_out(input_features=columns_to_encode)

# Get the names of the remaining columns
remaining_column_names = list(pipeline.named_steps['preprocessor'].transformers_[-1][2])  # Get the names of passthrough columns

# Combine all column names
all_column_names = list(encoded_feature_names) + ['Provenance'] + remaining_column_names

testing_pipe_df_end = pd.DataFrame(testing_pipe_df_end, columns=all_column_names)

testing_pipe_df_end.index = preprocessing_df.index

testing_pipe_df_end""",language='python')
st.markdown("""<div style="overflow-x: auto;">
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Propulsion_Combustion</th>
      <th>Propulsion_Electric</th>
      <th>Propulsion_Hybrid</th>
      <th>Propulsion_Light Hybrid</th>
      <th>Propulsion_Plug-in hybrid</th>
      <th>Car gearbox_Automated</th>
      <th>Car gearbox_Automatic</th>
      <th>Car gearbox_CVT</th>
      <th>Car gearbox_Manual</th>
      <th>Fuel_Alcohol</th>
      <th>...</th>
      <th>Maximum power</th>
      <th>Unit displacement</th>
      <th>Trunk</th>
      <th>USB connection</th>
      <th>Gear speed transmissions</th>
      <th>Urban</th>
      <th>Year</th>
      <th>Radio</th>
      <th>Folding rear seat</th>
      <th>Perimeter anti theft alarm</th>
    </tr>
    <tr>
      <th>car_code</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.302210</td>
      <td>0.517060</td>
      <td>0.003001</td>
      <td>0.0</td>
      <td>0.545455</td>
      <td>0.002481</td>
      <td>0.607143</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.012707</td>
      <td>0.249986</td>
      <td>0.019006</td>
      <td>0.0</td>
      <td>0.454545</td>
      <td>0.191067</td>
      <td>0.607143</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.046409</td>
      <td>0.500995</td>
      <td>0.024341</td>
      <td>0.0</td>
      <td>0.454545</td>
      <td>0.121588</td>
      <td>0.607143</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.065193</td>
      <td>0.445773</td>
      <td>0.021674</td>
      <td>0.0</td>
      <td>0.454545</td>
      <td>0.111663</td>
      <td>0.607143</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.055249</td>
      <td>0.437741</td>
      <td>0.024341</td>
      <td>0.0</td>
      <td>0.454545</td>
      <td>0.166253</td>
      <td>0.607143</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>23884</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.048619</td>
      <td>0.333321</td>
      <td>0.019673</td>
      <td>1.0</td>
      <td>0.545455</td>
      <td>0.148883</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>23885</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.048619</td>
      <td>0.333321</td>
      <td>0.019673</td>
      <td>1.0</td>
      <td>0.545455</td>
      <td>0.148883</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>23893</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.048619</td>
      <td>0.333321</td>
      <td>0.019673</td>
      <td>1.0</td>
      <td>0.545455</td>
      <td>0.166253</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>23905</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.059669</td>
      <td>0.546177</td>
      <td>0.766589</td>
      <td>1.0</td>
      <td>0.545455</td>
      <td>0.191067</td>
      <td>0.982143</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>23906</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.059669</td>
      <td>0.546177</td>
      <td>0.866622</td>
      <td>1.0</td>
      <td>0.545455</td>
      <td>0.191067</td>
      <td>0.982143</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
<p>20708 rows × 100 columns</p>
</div>
            """,unsafe_allow_html=True)
