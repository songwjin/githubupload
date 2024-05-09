from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px
import MySQLdb

db=MySQLdb.connect(host='localhost',user='root', password='1234', db='izen')
cur= db.cursor()


app = Flask(__name__)

@app.route('/')
def bar_with_plotly():
# Students data available in a list of list
    students = [['Akash', 34, 'Sydney', 'Australia'],
                ['Rithika', 30, 'Coimbatore', 'India'],
                ['Priya', 31, 'Coimbatore', 'India'],
                ['Sandy', 32, 'Tokyo', 'Japan'],
                ['Praneeth', 16, 'New York', 'US'],
                ['Praveen', 17, 'Toronto', 'Canada']]
    sql = "select * from tbl_plot"
    cur.execute(sql)
    datas = cur.fetchall();
    for i in datas:
        print(i)
    df =pd.DataFrame(datas, columns=['num','Name','Age','City','Country'], index=['a','b','c','d','e','f','g'])
    #Bar chart 생성
    fig = px.bar(df, x='Name', y='Age', color='City', barmode='group')

    #graphJson 생성
    graphJson = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('bar.html',graphJson=graphJson)
if __name__=='__main__':
    app.run(debug=True)