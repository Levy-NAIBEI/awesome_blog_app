from flaskblog import create_app

#init app
app = create_app()

#run server
if __name__ == '__main__':
    app.run(debug=True)