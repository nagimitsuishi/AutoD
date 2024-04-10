from flask import Flask, render_template, request, jsonify, send_file
#from service.search_work import query,get_json_data
import newChat
app = Flask(__name__)


pdf_files = [
    './static/others/1.pdf',
    './static/others/2.pdf',
    './static/others/3.pdf',
    './static/others/4.pdf',
    './static/others/5.pdf',
    './static/others/6.pdf',
    './static/others/7.pdf',
    './static/others/8.pdf',
    './static/others/9.pdf',
    './static/others/10.pdf'
]

@app.route('/get-pdf/<int:pdf_id>')
def get_pdf(pdf_id):
    if pdf_id >= 1 and pdf_id <= len(pdf_files):
        pdf_path = pdf_files[pdf_id - 1]
        return send_file(pdf_path, as_attachment=True)
    else:
        return "Invalid PDF ID"

@app.route('/', methods=['GET', 'POST'])

@app.route('/index', methods=['GET', 'POST'])
def index(name=None):
    return render_template('index.html', name = name)

@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')

@app.route('/ADQA', methods=['GET', 'POST'])
def ADQA():
    return render_template('ADQA.html')

@app.route('/generic', methods=['GET', 'POST'])
def generic():
    return render_template('generic.html')


@app.route('/elements', methods=['GET', 'POST'])
def elements():
    return render_template('elements.html')

@app.route('/get_all_graph', methods=['GET', 'POST'])
def get_all_graph():
    return render_template('all_graph.html')

@app.route('/stu_source', methods=['GET', 'POST'])
def stu_source():
    return render_template('stu_source.html')

@app.route('/ADQA_answer', methods=['POST'])
def KGQA_answer():
    try:
        question = request.json.get('question', '')
        print('Received question:', question)
        json_data = newChat.ask_question(question)
        print('Generated answer:', json_data)
        return jsonify({'answer': json_data})
    except Exception as e:
        print('Error:', e)
        return jsonify({'error': str(e)})


@app.route('/search_name', methods=['GET', 'POST'])
def search_name():
    name = request.args.get('name')
    json_data=get_json_data(name,query(name))
    return jsonify(json_data)

@app.route('/detail-page-0')
def detail_page0():
    return render_template('detail-page-0.html')

@app.route('/detail-page-1')
def detail_page1():
    return render_template('detail-page-1.html')

@app.route('/detail-page-2')
def detail_page2():
    return render_template('detail-page-2.html')

@app.route('/detail-page-3')
def detail_page3():
    return render_template('detail-page-3.html')

@app.route('/detail-page-4')
def detail_page4():
    return render_template('detail-page-4.html')

@app.route('/detail-page-5')
def detail_page5():
    return render_template('detail-page-5.html')

@app.route('/detail-page-6')
def detail_page6():
    return render_template('detail-page-6.html')

@app.route('/detail-page-7')
def detail_page7():
    return render_template('detail-page-7.html')

@app.route('/detail-page-8')
def detail_page8():
    return render_template('detail-page-8.html')

@app.route('/detail-page-9')
def detail_page9():
    return render_template('detail-page-9.html')

@app.route('/detail-page-10')
def detail_page10():
    return render_template('detail-page-10.html')

@app.route('/detail-page-11')
def detail_page11():
    return render_template('detail-page-11.html')

if __name__ == '__main__':
    app.debug=True
    app.run()
