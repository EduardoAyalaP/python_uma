import pickle
from os.path import realpath, join, dirname
from os import getcwd

__location__ = realpath(join(getcwd(), dirname(__file__)))

def validate_reg2(list_words):
    """
    Función para validar que cada elemento dentro de
    `list_words` pertenezca a 'pos'
    y ningún otro elemento se encuentre en 'neg'.

    Parametro
    ---------
    list_words: lista de palabras a validar

    Regresa: bool
    """
    labels = {'pos': ['afoot', 'catfoot', 'dogfoot', 'fanfoot', 'foody',
                      'foolery', 'foolish', 'fooster', 'footage', 'foothot',
                      'footle', 'footpad', 'footway', 'hotfoot', 'jawfoot',
                      'mafoo', 'nonfood', 'padfoot', 'prefool', 'sfoot',
                      'unfool'],
              'neg': ['Atlas', 'Aymoro', 'Iberic', 'Mahran', 'Ormazd',
                      'Silipan', 'altared', 'chandoo', 'crenel', 'crooked',
                      'fardo', 'folksy', 'forest', 'hebamic', 'idgah',
                      'manlike', 'marly', 'palazzi', 'sixfold', 'tarrock',
                      'unfold']}
    all_pos = all(pos in list_words for pos in labels["pos"])
    none_neg = all(neg not in list_words for neg in labels["neg"])
    return all_pos and none_neg

def validate_reg4(users):
    """
    Función para validar el cuarto ejercicio de regex dentro de Lec05.ipynb
    """
    filepath = join(__location__, "users.pkl")
    real_users = pickle.load(open(filepath, "rb"))
    return all([u == ru for u, ru in zip(users, real_users)])
