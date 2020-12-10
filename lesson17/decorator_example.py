from functools import wraps

def stop_words(words):
    def stop_words_dec(func):
        @wraps(func)
        def wrap(*args):
            result = func(*args)
            for word in words:
                result = result.replace(word, '*')
            return result
        return wrap
    return stop_words_dec

@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"

