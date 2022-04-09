import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
df = pd.read_csv('C:/Users/yena0/Downloads/Python/class 107/data.csv')
level = df.groupby(['student_id','level'],as_index=False)['attempt'].mean()
graph = px.scatter(level,x = 'student_id',y = 'level',size='attempt',color='attempt')
graph.show()