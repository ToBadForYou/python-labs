import lab7a

db = [[['författare', ['john', 'zelle']],
       ['titel', ['python', 'programming', 'an', 'introduction', 'to',
                  'computer', 'science']],
       ['år', 2010],
       ['genre', "programmering"]],
      [['författare', ['armen', 'asratian']],
       ['titel', ['diskret', 'matematik']],
       ['år', 2012],
       ['genre', "matematik"]],
      [['författare', ['j', 'glenn', 'brookshear']],
       ['titel', ['computer', 'science', 'an', 'overview']],
       ['år', 2011],
       ['genre', "matematik"]],
      [['författare', ['john', 'zelle']],
       ['titel', ['data', 'structures', 'and', 'algorithms', 'using', 'python',
                  'and', 'c++']],
       ['år', 2009],
       ['genre', "programmering"]],
      [['författare', ['anders', 'haraldsson']],
       ['titel', ['programmering', 'i', 'lisp']],
       ['år', 1993],
       ['genre', "programmering"]]]


def test():
    expected_results = [[db[0], db[3]], [db[0], db[2]], []]

    result = lab7a.search(['författare', ['john', '&']], db)
    assert result == expected_results[0]

    result = lab7a.search(['titel', ['--', 'an', '--']], db)
    assert result == expected_results[1]

    result = lab7a.search(['år', 2007], db)
    assert result == expected_results[2]

    result = lab7a.search([['författare', ['&', '&']], ['titel',
                          ['--', 'python', '--']], ['år', "&"],
                          ['genre', "programmering"]], db)
    assert result == expected_results[0]

    result = lab7a.search([['författare', ['&', 'zelle']], ['titel',
                          ['--', 'python', '--']], ['genre', "svenska"]], db)
    assert result == expected_results[2]

    result = lab7a.search([], db)
    assert result == expected_results[2]

    result = lab7a.search(['genre', "&"], db)
    assert result == db
    print("Passed all tests")


test()
