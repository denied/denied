from deny import *

database = 'guestbook.txt'


def get_all_notes():
    f = open(database)
    try:
        return map(parse_json, f)
    finally:
        f.close()


def add_note(title, text):
    f = open(database, 'a')
    try:
        f.write('%s\n' % dump_json(dict(
            title=title,
            text=text
        )))
    finally:
        f.close()


@route('/')
def show_notes():
    return render_template(notes=get_all_notes())


@route('/create')
def create_note():
    add_note(request.values['title'],
             request.values['text'])
    return redirect(url_for('show_notes'))


if __name__ == '__main__':
    run()
