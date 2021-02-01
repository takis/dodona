Schrijf een functie badcrypt die een string parameter cleartext heeft
en als resultaat een geencrypteerde string teruggeeft.

Hint: Je kan de string-method "replace" gebruiken, om achtereenvolgens
alle letters in de invoertekst om te zetten:
a -> B
b -> C
c -> D
...
x -> Y
y -> Z
z -> A

Al de andere letters hoef je niet te vervangen.

### Input

Een string met enkel kleine letters.

### Output

De "geencrypteerde" versie ervan, waarbij je iedere letter
vervangt door de volgende letter in het alfabet, als hoofdletter.

### Example

**Input:**

      abc      

**Output:**

      BCD


### Example

**Input:**

      xyz

**Output:**

      YZA


### Example

**Input:**

      ik heet bert

**Output:**

      JL IFFU CFSU

