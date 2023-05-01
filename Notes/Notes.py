class Note:
    def __init__(self, id_, heading, body, timedate):
        self.id_ = id_
        self.heading = heading
        self.body = body
        self.timedate = timedate

    # Setters

    def set_id(self, id_):
        self.id_ = id_

    def set_heading(self, heading):
        self.heading = heading

    def set_body(self, body):
        self.body = body

    def set_timedate(self, timedate):
        self.timedate = timedate

    # Getters

    def get_id(self):
        return self.id_

    def get_heading(self):
        return self.heading

    def get_body(self):
        return self.body

    def get_timedate(self):
        return self.timedate

    def to_string(note):
        return note.id_ + ';' + note.heading + ';' + note.body + ';' + note.timedate

    def __str__(self):
        return f"Идентификатор заметки: {self.id_} Заголовок: {self.heading} " \
               f"Заметка: {self.body} Время создания: {self.timedate}"
