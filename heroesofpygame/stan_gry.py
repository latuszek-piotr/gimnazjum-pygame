

class StanGry(object):
    def __init__(self):
        self.zaczety = False
        self.zakonczony = False

    def on_entry(self):
        '''Akcje wykonywane gdy zaczyna sie dany stan gry'''
        self.zaczety = True

    def on_exit(self):
        '''Akcje wykonywane gdy konczy sie dany stan gry'''
        self.zakonczony = True

    def on_clock_tick(self):
        '''
        Obsluga "tykniecia" zegara gry
        Zwraca albo nazwe biezacego stanu gry (gdy stan sie nie zmienia)
        albo nazwe nowego stanu gry ktory wynika z obslugi "tykniecia" zegara
        '''
        return "nieznany"

    def on_event(self, event):
        '''
        Obsluga eventu pygame w grze
        Zwraca albo nazwe biezacego stanu gry (gdy stan sie nie zmienia)
        albo nazwe nowego stanu gry ktory wynika z obslugi eventu
        '''
        return "nieznany"
