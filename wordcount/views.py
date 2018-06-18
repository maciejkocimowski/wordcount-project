from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    wordcoutdict = {}
    for word in wordlist:
        if word in wordcoutdict:
            wordcoutdict[word] += 1
        else:
            wordcoutdict[word] = 1

    sortedwords = sorted(wordcoutdict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',
                  {'fulltext': fulltext,
                   'count': len(wordlist),
                   'wordcountdict': sortedwords})


def about(request):
    return render(request, 'about.html')
