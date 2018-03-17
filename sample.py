from flask import Flask

# Your Code Goes Here.

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
	
if __name__ == '__main__':
  app.debug = True	
  app.run(port=33507)

