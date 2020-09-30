import enchant
from itertools import permutations, combinations
from flask import Flask, request, render_template as render

app = Flask(__name__)
spellbook = enchant.Dict("en_US")

def sort_key(str):
    return len(str), str.lower()

@app.route('/', methods=['POST'])
def crack():
    post_word = request.form.get('word').lower()
    post_counts = [
        request.form.get('count-2') == 'on',
        request.form.get('count-3') == 'on',
        request.form.get('count-4') == 'on',
        request.form.get('count-5') == 'on',
        request.form.get('count-6') == 'on',
        request.form.get('count-7') == 'on',
        request.form.get('count-8') == 'on',
        request.form.get('count-9') == 'on',
    ]
    counts = [ c+2 for c in range(len(post_counts)) if post_counts[c]]
    comboz = [ ''.join(l) for i in range(len(post_word)) for l in combinations(post_word, i+1)]
    permz = [ ''.join(p) for c in comboz for p in permutations(c)]
    result = list(set([word for count in counts for word in permz if (len(word) == count) if spellbook.check(word)]))
    result.sort(key=sort_key)
    return render('index.html', result=result, word=post_word)


@app.route('/')
def index():
    return render('index.html')
