import pandas as pd

from flask import Flask, render_template,request
import pickle
import numpy as np

popular_df =pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def about():
    return render_template('register.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_products',methods=['post'])
def recommend():
    user_input = request.form.get('user_input')

    def Recommendranking(pf_list, recomend_list, top_list):
        dic = {}
        # out=[None]*len(recomend_list)
        for i in range(len(recomend_list)):
            for j in range(len(pf_list)):
                if pf_list[j] == recomend_list[i]:
                    dic[recomend_list[i]] = j
                    break
        out = sorted(dic)
        # for i in range(len(recomend_list)):
        #     if dic.get(recomend_list[i])!=None:
        #         out[dic[recomend_list[i]]]=recomend_list[i]
        dic2 = {}
        # max_value=max(dic.values())
        for i in range(len(recomend_list)):
            if dic.get(recomend_list[i]) == None:
                for j in range(len(top_list)):
                    if top_list[j] == recomend_list[i]:
                        dic2[recomend_list[i]] = j
                        break
        out1 = sorted(dic2)
        print(out + out1)

        return render_template('recommend.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ == "__main__":
    app.run(debug=True)
