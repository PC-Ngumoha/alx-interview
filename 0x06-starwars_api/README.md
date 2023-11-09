# Star Wars A.P.I

## My Thought Process

PSEUDOCODE:

Approach #1:

```
set MovieId = Argv[0]
set MovieUrl = URL OF THE MOVIE ENDPOINT + MovieId

Request(MovieURL, data).on('data'){
  characterURLs = data.characters;
  FOREACH characterURL in characterURLs{
    Request(characterURL, data).on('data') {
      PRINT data.name
    }
  }
}
```

This algorithm worked in retrieving the list of characters but the order of the list was not maintained. This was caused by the fact that the request module runs code asynchronously and not synchronously. Essentially, request was not going through the list of character URLs one after the other and resolving them, instead, it went through all of them at somewhat the same time and then whichever one resolved first was first printed.

An idea I'm having is to tap into the power of recursion to force the request module to go through the list synchronously and this will form the basis for my second approach.


Approach #2:

```
set MovieId = Argv[0]
set MovieUrl = URL OF THE MOVIE ENDPOINT + MovieId

Request(MovieURL, data).on('data'){
  characterURLs = data.characters;
  CALL displayCharacterName(characterURLs, 0);
}

DEFINE displayCharacterName(characterURLs, index) {
  If index >= LENGTH(characterURLS), Then:
    RETURN;
  Request(characterURLs[index], character).on('character'){
    PRINT character.name;
    displayCharacterName(characterURLs, index + 1);
  }
}
```

This seems to work as the order of characters on the list is preserved while being retrieved.