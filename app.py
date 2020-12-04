from flask import Flask,render_template,redirect,request
import describe_it

#__name__==__main__
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def marks():
    if request.method=='POST':
        f = request.files['userfile']
        path = "./static/{}".format(f.filename)
        f.save(path)

        caption = describe_it.caption_this_image(path)
        #print(caption)

        result_dic = {
            'image' : path,
            'caption' : caption
        }

    return render_template("index.html",your_result=result_dic)


if __name__ == "__main__":
    #app.debug = True
    app.run(debug = True)